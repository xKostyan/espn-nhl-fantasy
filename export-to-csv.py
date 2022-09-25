# This script takes existing players data and converts it into a flat table (as csv file)
# so it can be used in 'tables' tools
from json import load
import argparse

import pandas
import pandas as pd


def get_args() -> argparse.Namespace:
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(description='Exports players data into csv file')
    parser.add_argument('--league_id', type=int, help='Id of the fantasy league', required=True)
    return parser.parse_args()


def load_json(_league_id) -> dict:
    with open('espn-data/{}/player-draft-data.json'.format(_league_id), 'r') as _f:
        full_data = load(_f)
    return full_data


def get_player_df(_player_data) -> pandas.DataFrame:
    position = str()
    if 'id' not in _player_data:
        print(_player_data)
    data = {
        'id': [_player_data['id']],
        'name': [_player_data['name']],
        'position': [_player_data['position']]
    }
    tmp_df = pd.DataFrame(data)
    return tmp_df


def main(_league_id):
    """
    Main
    :param int _league_id: Fantasy league ID
    """

    dict_data = load_json(_league_id)
    df = pd.DataFrame()

    for pid in dict_data['players']:
        print('debug ' + str(pid))
        _tmp = get_player_df(dict_data['players'][pid])
        df = pd.concat([df, _tmp])

    print(df)
    # for years in full_data['years']:
    # pd_data = pandas
    # for player in full_data['players']:
    #     pd_player = pandas.DataFrame.from_dict(full_data['players'][player], orient='index')
    #     pd_data = pandas.concat(pd_player)
    # print(pd_data)


if __name__ == '__main__':
    args = get_args()
    main(args.league_id)
