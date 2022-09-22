# This script takes existing players data and converts it into a flat table (as csv file)
# so it can be used in 'tables' tools
from json import load
import argparse
import pandas


def get_args() -> argparse.Namespace:
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(description='Exports players data into csv file')
    parser.add_argument('--league_id', type=int, help='Id of the fantasy league', required=True)
    return parser.parse_args()


def main(_league_id):
    """
    Main
    :param int _league_id: Fantasy league ID
    """
    with open('espn-data/{}/player-draft-data.json'.format(_league_id), 'r') as _f:
        full_data = load(_f)

    # for years in full_data['years']:
    # pd_data = pandas
    # for player in full_data['players']:
    #     pd_player = pandas.DataFrame.from_dict(full_data['players'][player], orient='index')
    #     pd_data = pandas.concat(pd_player)
    # print(pd_data)


if __name__ == '__main__':
    args = get_args()
    main(args.league_id)
