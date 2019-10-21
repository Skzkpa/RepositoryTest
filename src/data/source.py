import yaml
from copy import deepcopy
from datetime import date, timedelta
from collections import defaultdict

data = """135457	F223: Complete Message Provenance - Extend Message Catalogue to Include External Packages in DPF			CLE	Roy Grandfield	Closed	0
132728	F075f: Azure Event Hub and Blob Connector 			CLE	Roy Grandfield	Closed	
134173	{F143 [SUF File Generation] - API to access Fleet Store			CSME	John Greenwood	Closed	0
135458	{F274} CDA - Add EEC software version to the config schema identification			CSME		Closed	0
106727	Integration of SORTT SFTP Uploader into Release Pipeline	keep	Monkeys	CLE MVP	Faisal	Active	8
127248	[Automation]: Terraform network adjustments	Faisal would like to stick to MS tooling - powershell, as it makes deployments harder. Could live without this as there is a workaround although this requires manual intervention. Manual intervention requires elevated privileges which are difficult to get. To discuss with MS.	Monkeys	CSME MVP	Faisal	Active	30
134174	DA adjustments	keep   	Monkeys	CSME MVP	Faisal	Closed	3
134169	Migrate to feature branch delivery	keep	Apes	CSME MVP	Faisal	Active	40
136171	Splitting App service plan		Apes	CSME MVP	Faisal	Active	13
XXX	Documentation LLD etc.	Could be 40. Buzzards need more direction to give a better estimat	Apes&Monkeys	BOTH	Faisal	Blocked	80
69221	Update "Continuous Integration & Delivery" LLD		Monkeys	CSME MVP	Faisal	New	8
136604	Shared Services Integration	NotEstimated (will be substracted from one below); waiting for input from Faisal	Apes	CSME MVP	Faisal	New	0
Many US's	Security compliance IP10-IP11.2	Output from integration with shared services and environment lock down. 30 sounds quite high, very similar with Pen test story.	Apes	CSME MVP	Faisal	New	30
136603	Pentest adjustments 	Bulpark estimate / buffer - can go down	Apes	CSME MVP	Faisal	New	36
134672	[Automation] Tableau pipeline adjustments for automation	keep. It's another manual process, but we don't deploy it every time.	Monkeys	CSME MVP	Faisal	New	5
135804	EPS Adjustments		Monkeys	CSME MVP	Faisal	New	13
136595	DR adjustments and support	Bulpark estimate / buffer	Apes	CSME MVP	Faisal	Active	36
132639	Relation based deployment	must do	Apes	CSME MVP	Faisal	Active	20
126794	Automation of provisioning subscriptions: Config Adjustments (read/write), configuration design		Monkeys	CSME MVP	Faisal	New	30
136564	Release 1.2 support	NotEstimated (will be substracted from one below)	Monkeys	CSME MVP	Faisal	Active	8""".split('\n')
supp_tasks = """135452	Release Pipeline Support - IP10.1		Apes&Monkeys	CSME MVP	Faisal	Closed	13
137056	Release Pipeline Support - IP10.2 - Monkeys		Monkeys	CSME MVP	Faisal	Active	7
137195	Release Pipeline Support - IP10.2 - Apes		Apes	CSME MVP	Faisal	Active	8
	Release Pipeline Support - IP10.3 - Monkeys		Monkeys	CSME MVP	Faisal	Active	7
	Release Pipeline Support - IP10.3 - Apes		Apes	CSME MVP	Faisal	Active	8
	Release Pipeline Support - IP10.4 - Monkeys		Monkeys	CSME MVP	Faisal	Active	7
	Release Pipeline Support - IP10.4 - Apes		Apes	CSME MVP	Faisal	Active	8
	Release Pipeline Support - IP11.1 - Monkeys		Monkeys	CSME MVP	Faisal	Active	7
	Release Pipeline Support - IP11.1 - Apes		Apes	CSME MVP	Faisal	Active	8
	Release Pipeline Support - IP11.2 - Monkeys		Monkeys	CSME MVP	Faisal	Active	7
	Release Pipeline Support - IP11.2 - Apes		Apes	CSME MVP	Faisal	Active	8""".split('\n')

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
full_data = []

all_data = defaultdict(list)


def add_days_skipping_weekends(adate, days):
    for i in range(days):
        adate += timedelta(days=1 if adate.weekday else 3)
    return adate


def process(data, global_days_lengh=0, start=None):
    global all_data
    current_date = start if start else date(2019, 10, 2)
    apes_current_date = start if start else date(2019, 10, 2)
    monkeys_current_date = start if start else date(2019, 10, 2)
    for idx, line in enumerate(data):
        ticket, atitle, comments, team, release, po, status, story_points = line.split('\t')
        team = team.lower() if team else "apes&monkeys"
        if global_days_lengh == 0:
            days_lengh = round(int(story_points if story_points else 1) * 4 / 5) + 1
            days_to_add = days_lengh // 2
        else:
            days_lengh = global_days_lengh
            days_to_add = days_lengh
        if team == 'apes':
            cdate = apes_current_date
            apes_current_date = add_days_skipping_weekends(apes_current_date, days_to_add)
        elif team == "monkeys":
            cdate = monkeys_current_date
            monkeys_current_date = add_days_skipping_weekends(monkeys_current_date, days_to_add)
        else:
            cdate = current_date
            current_date = add_days_skipping_weekends(current_date, days_to_add)
        base = {
            "label": atitle,
            "user": 2,
            "team": team,
            "start": str(cdate),
            "duration": days_lengh,
            "story_points": story_points,
            "percent": percent.get(status, 0),
            "type": "project",
            "collapsed": False,
            "style": deepcopy(styles.get(team.lower() if team else "apes&monkeys"))
        }
        all_data[team].append(base)


process(data)
process(supp_tasks, global_days_lengh=14, start=date(2019, 10, 16))

i = 0
for k, val in all_data.items():
    for v in val:
        v["id"] = i
        i += 1
    full_data += val
print(yaml.dump(full_data, default_flow_style=False))
