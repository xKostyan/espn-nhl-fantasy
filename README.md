# espn-nhl-fantasy
## Description
Applets to work with ESPN NHL fantasy data. Tools are designed to help analyze players values in salary cap leagues with Auction type draft.

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