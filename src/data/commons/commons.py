import yaml
from copy import deepcopy
from datetime import date, timedelta
from collections import defaultdict

styles = {
    "New": {
        "base": {
            "fill": "#0287D0",
            "stroke": "#0077C0"
        }
    },
    "Active": {
        "base": {
            "fill": "#8E44AD",
            "stroke": "#7E349D"
        }
    },
    "Closed": {
        "base": {
            "fill": "#1EBC61",
            "stroke": "#0EAC51"
        }
    },
    "blocked": dict(),
}
percent = {
    "New": 0,
    "Closed": 100,
    "Active": 20,
    "Blocked": 0,
}


def add_days_skipping_weekends(adate, days):
    for i in range(days):
        adate += timedelta(days=1 if adate.weekday else 3)
    return adate


def dump(data):
    return yaml.dump(data, default_flow_style=False)


def save_yaml_file(data, file_name):
    with open("{}.yaml".format(file_name), 'w') as file:
        file.write(data)


def process(data, velocity=10, global_days_lengh=0, start=None):
    current_date = start if start else date(2019, 10, 16)
    for line in data:
        story_points = line['story_points']
        status = line['status']
        if global_days_lengh == 0:
            days_lengh = round(int(story_points if story_points else 1) / (velocity / 10))
            days_to_add = days_lengh if days_lengh > 0 else 1
        else:
            days_lengh = global_days_lengh
            days_to_add = days_lengh
        cdate = current_date
        current_date = add_days_skipping_weekends(current_date, days_to_add)
        line.update({
            "start": str(cdate),
            "duration": days_lengh if days_lengh > 0 else 1,
            "percent": percent.get(status, 0),
            "type": "project",
        })
        if status.lower() != 'blocked':
            line['style'] = deepcopy(styles.get(status))
    return dump(data)
