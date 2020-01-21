from collections import defaultdict
from copy import deepcopy
from datetime import date, timedelta
from math import ceil
import logging

import yaml


nested_dict = lambda: defaultdict(nested_dict)

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


class ProperDate:
    def __init__(self):
        self.dates = nested_dict()
        # PI > sprint > team
        self.dates[10][1]['x'] = date(2019, 10, 2)
        self.dates[11][1]['x'] = date(2019, 11, 27)
        self.dates[12][1]['x'] = date(2020, 2, 5)

    def calculate_pi_start(self, pi, sprint):
        return self.dates[pi][1]['x'] + timedelta(days=14 * (sprint - 1))

    @staticmethod
    def add_days_skipping_weekends(adate, days):
        for i in range(days):
            adate += timedelta(days=1 if adate.weekday else 3)
        return adate

    def get_date_from_pi_sprint(self, pi, sprint=2, duration=1, team='x'):
        if pi is None:
            pi = 11
        if sprint is None:
            sprint = 4
        start = self.dates.get(pi, {}).get(sprint, {}).get(team, self.calculate_pi_start(pi, sprint))
        cpis = self.add_days_skipping_weekends(start, duration)
        self.dates[pi][sprint][team] = cpis
        return str(start)


def dump(data):
    return yaml.dump(data, default_flow_style=False)


def save_yaml_file(data, file_name):
    with open("./tasks/{}.yaml".format(file_name), 'w') as file:
        file.write(data)
pd = ProperDate()

def process(data, velocity=10, area="x"):
    global pd
    for line in data:
        line["type"] = "project"
        story_points = line.get('story_points', 0)
        status = line['status']
        # duration
        if line.get("duration") is None:
            global_days_lengh = 14 if 'Sprint' in line['title'] or 'SP' in line['title'] else 0
            if global_days_lengh == 0:
                days_lengh = ceil(int(story_points if story_points else 1) / (velocity / 10))
                logging.debug(f"SP:{story_points} days_lengh:{days_lengh}")
            else:
                days_lengh = global_days_lengh
                days_to_add = days_lengh
            dl = days_lengh if days_lengh > 0 else 1
            line["duration"] = dl * 24 * 3600 * 1000
        else:
            days_to_add = line.get("duration")
            if days_to_add < 1000:
                line["duration"] = days_to_add * 24 * 3600 * 1000
        # percent
        if line.get("percent") is None:
            line["percent"] = percent.get(status, 0)
        # tags
        if line.get('dependenton'):
            line['dependentOn'] = [int(a) for a in line.get('dependenton').split(',')]
            line.pop('dependenton')

        if line.get('tags'):
            tags = line.get('tags').split(';')
            for tag in tags:
                tag = tag.strip().lower()
                if tag.startswith('milestone'):
                    line['milestone'] = tag[-1].upper()
                elif tag.startswith('sprint'):
                    line['sprint'] = int(tag[-1])
                elif tag.startswith('pi'):
                    line['pi'] = int(tag[2:])
        # style
        if status.lower() != 'blocked':
            line['style'] = deepcopy(styles.get(status))
        line['team'] = area
        # start
        if line.get("start") is None:
            line['start'] = pd.get_date_from_pi_sprint(
                line.get('pi'),
                line.get('sprint'),
                days_lengh,
                team=area
            )
    return dump(data)
