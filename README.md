# espn-nhl-fantasy
## Description
Applets to work with ESPN NHL fantasy data. Tools are designed to help analyze players values in salary cap leagues with Auction type draft.

---

## Usage

### Step 1 - setup your league.
Run 'init-new-league.py'
This script will interactively walk you through your fantasy league scoring values. 
This will create a file with how your league calculates scoring.<br>
Data is stored in 'espn-data/<your_league_id>/league-scoring-config.json'

### Step 2 - get authentication values for your league.
This is required to authenticate on espn and access your leagues' data. 2 values are required:
- espn_s2  
- swid

Get credential values by loging into espn league 
- -> inspect page in your browser
- -> go to 'Application' tab 
- -> go to 'Storage' 
- -> go to 'Cookies' 
- -> Find "http://fantasy.espn.com".
- -> Find required values in the list and save them for usage in Step 3

### Step 3 - get players data.
Run 'get-players-base-data.py'
This script requires couple arguments to work:
- --league_id <your-league-id>
- --espn_s2 "<espn_s2_value>"  
- --swid "{<swid_value>}"

Data will be stored in the folder for your league 'espn-data/<your_league_id>/player-draft-data.json'

---
<details>
  <summary>JSON Data snippet:</summary>

  ```
{
	"years": [
		2023,
		2022,
		2021
	],
	"draft": {
		"draft_years": [
			2022,
			2021
		],
		"2022": {
			"salary_cap": 815
		},
		"2021": {
			"salary_cap": 815
		}
	},
	"players": {
		"2555316": {
			"name": "Calle Jarnkrok",
			"2023": {
				"proTeam": "Toronto Maple Leafs",
				"stats": {
					"Projected 2023": {
						"total": {
							"MIN ?": 60858.0,
							"G": 12.0,
							"A": 16.0,
							"+/-": 8.0,
							"16": 28.0,
							"PIM": 10.0,
							"PPG": 1.0,
							"19": 3.0,
							"SHG": 1.0,
							"SHA": 1.0,
							"25": 355.0,
							"ATOI": 882.0,
							"SOG": 112.0,
							"30": 69.0,
							"HIT": 35.0,
							"BLK": 23.0,
							"GP": 69.0,
							"PPP": 4.0,
							"SHP": 2.0,
							"f_avg": 1.76,
							"f_total": 121.5
						}
					}
				}
			},
			"position": "Forward",
			"id": 2555316,
			"2022": {
				"proTeam": "Calgary Flames",
				"stats": {
					"Total 2022": {
						"total": {
							"G": 12.0,
							"A": 18.0,
							"+/-": -14.0,
							"16": 30.0,
							"PIM": 6.0,
							"PPG": 2.0,
							"19": 4.0,
							"SHG": 0.0,
							"SHA": 0.0,
							"GWG": 1.0,
							"FOW": 239.0,
							"FOL": 228.0,
							"25": 1473.0,
							"TTOI ?": 63505.0,
							"ATOI": 962.1969697,
							"SOG": 101.0,
							"30": 66.0,
							"HIT": 38.0,
							"BLK": 17.0,
							"GP": 66.0,
							"35": 2.0,
							"36": 4.0,
							"37": 6.0,
							"PPP": 6.0,
							"SHP": 0.0,
							"f_avg": 1.78,
							"f_total": 117.55
						}
					},
					"Projected 2022": {
						"total": {
							"MIN ?": 66096.0,
							"G": 16.0,
							"A": 21.0,
							"+/-": 11.0,
							"16": 37.0,
							"PIM": 18.0,
							"PPG": 3.0,
							"19": 8.0,
							"SHG": 2.0,
							"25": 312.0,
							"ATOI": 972.0,
							"SOG": 127.0,
							"30": 68.0,
							"HIT": 42.0,
							"BLK": 20.0,
							"GP": 68.0,
							"PPP": 11.0,
							"SHP": 2.0,
							"f_avg": 2.29,
							"f_total": 155.95
						}
					}
				}
			},
			"2021": {
				"proTeam": "Seattle Kraken",
				"stats": {
					"Total 2021": {
						"total": {
							"G": 13.0,
							"A": 15.0,
							"+/-": 13.0,
							"16": 28.0,
							"PIM": 14.0,
							"PPG": 2.0,
							"19": 6.0,
							"SHG": 1.0,
							"SHA": 0.0,
							"GWG": 2.0,
							"FOW": 41.0,
							"FOL": 54.0,
							"25": 1067.0,
							"TTOI ?": 49388.0,
							"ATOI": 1007.91836735,
							"SOG": 91.0,
							"30": 49.0,
							"HIT": 30.0,
							"BLK": 15.0,
							"GP": 49.0,
							"35": 3.0,
							"36": 6.0,
							"37": 9.0,
							"PPP": 8.0,
							"SHP": 1.0,
							"f_avg": 2.41,
							"f_total": 118.25
						}
					}
				}
			}
		}
	}
}
```

</details>

---

### Step 4 - convert player data to csv flat table
Run 'export_to_csv.py'
This script requires an argument:
- --league_id <your-league-id>

Data will be stored in the folder for your league 'espn-data/<your_league_id>/player-draft-data.csv'

---

<details>
  <summary>CSV Data snippet:</summary>
Row 1 and 2 are table headers. Column one is index (espn players_id) </br></br>

```
,info,info,2021,2021,2021,2021,2021,2021,2021,2022,2022,2022,2022,2022,2022,2022,2023,2023,2023,2023,2023,2023,2023
,name,position,keeper,price,cap%,avg_proj,avg,proj_total,total,keeper,price,cap%,avg_proj,avg,proj_total,total,keeper,price,cap%,avg_proj,avg,proj_total,total
2555316,Calle Jarnkrok,Forward,,,,,2.41,,118.25,,,,2.29,1.78,155.95,117.55,,,,1.76,,121.5,
2555315,Charlie Coyle,Forward,,,,2.43,1.77,136.25,90.45,,,,2.32,2.35,183.45,192.65,,,,2.26,,178.25,
3095975,Charlie Lindgren,Goalie,,,,,,,,,,,,12.06,,48.25,,,,6.82,,177.25,
3096115,Mike Vecchione,Forward,,,,,,,,,,,,0.75,,0.75,,,,,,,
4832877,Olle Alsing,Defense,,,,,0.41,,1.65,,,,,,,,,,,,,,
3096102,Troy Stecher,Defense,,,,,1.86,,82.05,,,,,1.77,,51.3,,,,,,,
3096186,Trevor Moore,Forward,,,,,1.81,,101.3,,,,,2.59,,209.9,,,,2.42,,198.7,
3096177,Casey Nelson,Defense,,,,,,,,,,,,,,,,,,,,,
2555470,Mark Borowiecki,Defense,,,,,2.29,,50.4,,,,,2.82,,157.75,,,,,,,
3096249,Devon Toews,Defense,,,,2.76,3.66,154.7,194.15,False,25,3.07,3.51,4.42,259.8,291.4,,,,3.93,,278.9,
3096237,Noel Acciari,Forward,,,,,2.32,,95.1,,,,,2.31,,46.3,,,,,,,
3096236,Brandon Tanev,Forward,,,,2.22,2.94,122.25,94.15,,,,2.92,2.87,198.3,86.05,,,,2.58,,162.85,
3096235,Kevin Rooney,Forward,,,,,2.06,,111.0,,,,,1.42,,86.4,,,,,,,
3096263,Joe Gambardella,Forward,,,,,,,,,,,,,,,,,,,,,
4226783,Radim Simek,Defense,,,,,1.65,,66.1,,,,,1.29,,46.35,,,,,,,
4423398,Emil Bemstrom,Forward,,,,,1.48,,29.5,,,,,1.3,,53.1,,,,,,,
3096217,Thatcher Demko,Goalie,True,3,0.37,7.8,6.69,163.75,234.25,True,16,1.96,7.2,7.24,345.75,441.75,,,,7.45,,469.5,
4062934,Alexandre Fortin,Forward,,,,,,,,,,,,,,,,,,,,,
4341584,Kevin Lankinen,Goalie,,,,,6.8,,251.75,False,1,0.12,7.23,5.09,224.0,147.75,,,,6.23,,99.75,
4063242,Garrett Pilon,Forward,,,,,0.0,,0.0,,,,,1.73,,3.45,,,,,,,
4063240,Beck Malenstyn,Forward,,,,,,,,,,,,1.41,,16.9,,,,,,,
4063231,Tanner Fritz,Forward,,,,,,,,,,,,,,,,,,,,,
4063228,Janne Kuokkanen,Forward,,,,,1.89,,94.25,,,,,1.39,,79.3,,,,,,,
4063294,Cam Dineen,Defense,,,,,,,,,,,,1.77,,60.2,,,,,,,
3571762,Ben Hutton,Defense,,,,,1.55,,58.9,,,,,2.04,,118.4,,,,,,,
4063288,David Rittich,Goalie,True,6,0.74,6.77,5.48,142.25,82.25,,,,6.43,6.79,180.0,81.5,,,,6.19,,111.5,
4063279,Nathan Bastian,Forward,,,,,1.73,,71.1,,,,,2.09,,150.25,,,,,,,
4063280,Jacob Moverare,Defense,,,,,,,,,,,,1.2,,22.85,,,,,,,
4063267,Kale Clague,Defense,,,,,1.86,,33.4,,,,,1.75,,62.9,,,,,,,
4063268,Dillon Dube,Forward,,,,,2.04,,103.9,,,,,1.92,,151.45,,,,,,,
4063257,Josh  Currie,Forward,,,,,0.0,,0.0,,,,,,,,,,,,,,
4063258,Tyler Benson,Forward,,,,,,,,,,,,0.84,,24.5,,,,,,,
4063253,Connor Bunnaman,Forward,,,,,0.71,,12.85,,,,,0.48,,7.2,,,,,,,
4063251,Markus Niemelainen,Defense,,,,,,,,,,,,1.29,,25.7,,,,,,,
4063250,Carsen Twarynski,Forward,,,,,0.67,,4.7,,,,,,,,,,,,,,
3096605,Ryan Carpenter,Forward,,,,,1.39,,55.55,,,,,1.49,,99.85,,,,,,,
4227208,Victor Antipin,Defense,,,,,,,,,,,,,,,,,,,,,
4587557,Ivan Prosvetov,Goalie,,,,,0.5,,0.5,,,,,3.25,,9.75,,,,,,,
4587568,Jan Jenik,Forward,,,,,3.48,,6.95,,,,,1.88,,24.5,,,,,,,
4046946,Michal Kempny,Defense,,,,,,,,,,,,1.95,,29.2,,,,,,,
4046937,Vadim Shipachyov,Forward,,,,,,,,,,,,,,,,,,,,,
4587580,Matias Maccelli,Forward,,,,,,,,,,,,1.13,,25.95,,,,,,,
4587588,Pavel Dorofeyev,Forward,,,,,,,,,,,,0.88,,1.75,,,,,,,
4063433,Alex DeBrincat,Forward,False,16,1.96,3.18,4.41,177.8,229.25,False,102,12.52,4.04,4.01,318.85,328.6,,,,3.76,,308.35,
4063429,Libor Hajek,Defense,,,,,1.25,,54.85,,,,,1.39,,23.7,,,,,,,
145,Zdeno Chara,Defense,,,,,2.06,,113.05,,,,,2.28,,164.25,,,,,,,
4063420,Sean Day,Defense,,,,,,,,,,,,0.2,,0.2,,,,,,,
4063414,Tim Gettinger,Forward,,,,,0.75,,1.5,,,,,0.59,,4.75,,,,,,,
4063401,Samuel Girard,Defense,,,,2.78,3.38,155.95,162.35,True,13,1.6,3.21,2.61,256.95,174.75,,,,2.52,,171.5,
```

</details>

---
