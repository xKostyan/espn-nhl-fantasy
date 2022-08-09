import ast
import json
from os import makedirs


def get_league_schema():
    schema = {
      "id": int(),
      "name": str(),
      "key-map": {
        "G": "Goals",
        "A": "Assists",
        "PIM": "Penalty Minutes",
        "PPG": "Power Play Goals",
        "PPA": "Power Play Assists",
        "SHG": "Short Handed Goals",
        "SHA": "Short Handed Assists",
        "GWG": "Game-Winning Goals",
        "HAT": "Hat Tricks",
        "SOG": "Shots on Goal",
        "HIT": "Hits",
        "BLK": "Blocked Shots",
        "DEF": "Defensemen Points",
        "W": "Wins",
        "L": "Losses",
        "GA": "Goals Against",
        "SV": "Saves",
        "SO": "Shutouts",
        "OTL": "Overtime Losses"
      },
      "scoring": {
        "skaters": {
          "G": float(),
          "A": float(),
          "PIM": float(),
          "PPG": float(),
          "PPA": float(),
          "SHG": float(),
          "SHA": float(),
          "GWG": float(),
          "HAT": float(),
          "SOG": float(),
          "HIT": float(),
          "BLK": float(),
          "DEF": float()
        },
        "goaltenders": {
          "W": float(),
          "L": float(),
          "GA": float(),
          "SV": float(),
          "SO": float(),
          "OTL": float()
        }
      }
    }
    return schema


def save_schema(_schema):
    try:
        makedirs('espn-data/{}'.format(_schema['id']))
    except FileExistsError:
        pass
    f_path = 'espn-data/{}/league-config.json'.format(_schema['id'])
    with open(f_path, 'w') as _file:
        json.dump(_schema, _file, indent=2)
        print('Data saved into \'{}\''.format(f_path))


def take_input(_keys, _schema):
    for key in _keys:
        _keys[key] = input_detect('{0} ({1}): '.format(_schema['key-map'][key], key))


def input_detect(prompt):
    return ast.literal_eval(input(prompt))


def main():
    schema = get_league_schema()
    schema['name'] = input('League name: ')
    schema['id'] = int(input('League id: '))
    print('Input league scoring values for skaters:')
    take_input(schema['scoring']['skaters'], schema)
    print('Input league scoring values for goalies:')
    take_input(schema['scoring']['goaltenders'], schema)
    save_schema(schema)


if __name__ == '__main__':
    main()
