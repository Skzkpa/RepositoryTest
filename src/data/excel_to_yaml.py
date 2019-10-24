import yaml
from copy import deepcopy
from datetime import date, timedelta
from collections import defaultdict

### User input

velocity = 30
input_data = """


<< Pass the data here >>


"""



### Script is below

styles = {
    "apes": {
        "base": {
            "fill": "#0287D0",
            "stroke": "#0077C0"
        }
    },
    "monkeys": {
        "base": {
            "fill": "#8E44AD",
            "stroke": "#7E349D"
        }
    },
    "apes&monkeys": {
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


def process(data, global_days_lengh=0, start=None):
    full_data = []
    data = data.split('\n')
    all_data = defaultdict(list)
    current_date = start if start else date(2019, 10, 16)
    for line in data:
        if not line:
            continue
        ticket, atitle, team, release, po, status, story_points = line.split('\t')
        if global_days_lengh == 0:
            days_lengh = round(int(story_points if story_points else 1) / (velocity / 10))
            days_to_add = days_lengh if days_lengh > 0 else 1
        else:
            days_lengh = global_days_lengh
            days_to_add = days_lengh
        cdate = current_date
        current_date = add_days_skipping_weekends(current_date, days_to_add)
        base = {
            "label": atitle,
            "user": 2,
            "team": team,
            "ticket": ticket,
            "start": str(cdate),
            "duration": days_lengh if days_lengh > 0 else 1,
            "story_points": story_points,
            "status": status,
            "percent": percent.get(status, 0),
            "type": "project",
            "style": deepcopy(styles.get(status, styles.get(team.lower() if team else "apes&monkeys")))
        }
        all_data[team].append(base)

        i = 0
        for k, val in all_data.items():
            for v in val:
                v["id"] = i
                i += 1
            full_data += val
        return yaml.dump(full_data, default_flow_style=False)


print(process(input_data))
