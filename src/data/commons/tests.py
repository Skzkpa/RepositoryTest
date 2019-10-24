from commons import process

velocity = 30
input_data = """


135457	F223: Complete Message Provenance - Extend Message Catalogue to Include External Packages in DPF	Apes&Monkeys	CSME MVP	Roy Grandfield	Closed	0
137195	Release Pipeline Support - IP10.2 - Apes	Apes	CSME MVP	Faisal	Active	8
132639	Relation based deployment	Apes	CSME MVP	Faisal	Blocked	20

"""

excpeted_output = """- duration: 1
  id: 0
  label: 'F223: Complete Message Provenance - Extend Message Catalogue to Include
    External Packages in DPF'
  percent: 100
  start: '2019-10-16'
  status: Closed
  story_points: '0'
  style:
    base:
      fill: '#1EBC61'
      stroke: '#0EAC51'
  team: Apes&Monkeys
  ticket: '135457'
  type: project
  user: 2
- duration: 3
  id: 1
  label: Release Pipeline Support - IP10.2 - Apes
  percent: 20
  start: '2019-10-17'
  status: Active
  story_points: '8'
  style:
    base:
      fill: '#0287D0'
      stroke: '#0077C0'
  team: Apes
  ticket: '137195'
  type: project
  user: 2
- duration: 7
  id: 2
  label: Relation based deployment
  percent: 0
  start: '2019-10-20'
  status: Blocked
  story_points: '20'
  style:
    base:
      fill: '#0287D0'
      stroke: '#0077C0'
  team: Apes
  ticket: '132639'
  type: project
  user: 2
"""

assert process(input_data, velocity) == excpeted_output

