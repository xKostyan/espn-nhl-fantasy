# This script takes existing players data and converts it into a flat table (as csv file)
# so it can be used in 'tables' tools
from json import load
import argparse

import pandas


YEAR_COLUMNS = ['keeper','price','cap%','avg_proj','avg','proj_total','total']
YEAR_VALUES =  [
    'draft_keeper',
    'draft_price',
    'draft_cap_percentage',
    '',
    '',
    '',
    ''
    ]

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


def setup_df(_full_data) -> pandas.DataFrame:
    """Converts players data into a dataframe

    :param dict _player_data: Dictionary of a single player data
    :return pandas.DataFrame: Data as pandas dataframe
    """
    # setup players
    df = pandas.DataFrame()
    for pid in _full_data['players']:
        data = {
            'id': [_full_data['players'][pid]['id']],
            'name': [_full_data['players'][pid]['name']],
            'position': [_full_data['players'][pid]['position']]
        }
        tmp_df = pandas.DataFrame(data).set_index('id')
        df = pandas.concat([df, tmp_df])

    # expand dataframe with columns for players. all cells have NaN
    header_values = [reversed(_full_data['years']), YEAR_COLUMNS]
    header = pandas.MultiIndex.from_product(header_values)
    years_df = pandas.DataFrame(columns=header)

    # convert to multilevel column names to have same column stucture as yearly data
    df.columns = pandas.MultiIndex.from_tuples([('info','name'), ('info','position')])
    df = pandas.concat([df, years_df])
    return df


# def get_players_data_as_df(_players_data, _years) -> pandas.DataFrame:

#     # print(player_df)
#     # _indx_df = pandas.DataFrame({'id': [_players_data['id']], 'name':[_players_data['name']]}).set_index('id')
#     # print(_indx_df)

#     # _data_schema_df = dict()
#     # _data_schema_df[_year] = pandas.DataFrame(
#     #     columns=['keeper','price','cap%','avg proj','avg','proj total','total'],
#     #     data=[[False, None, None, None, None, None, None]]
#     # )
#     # print(_data_schema_df)
#     # df = pandas.concat([_indx_df, _data_schema_df])
#     # print(df)
#     # if not _players_data[_year]['stats']:
#     #     # handler for stats
#     #     pass
#     # else:
#     #     # handler for no stats
#     #     pass
#     return player_df
    

def save_to_csv(_df, _league_id):
    """Dump pandas DataFrame into csv file

    :param pandas.DataFrame _df: DataFrame with all the data
    :param int _league_id: League id
    """
    _f = 'espn-data/{}/player-draft-data.csv'.format(_league_id)
    _df.to_csv(_f, sep=',', encoding='utf-8')



def main(_league_id) -> pandas.DataFrame:
    """
    Main
    :param int _league_id: Fantasy league ID
    """

    dict_data = load_json(_league_id)
    df = setup_df(dict_data)
    idx = pandas.IndexSlice
    
    for pid in dict_data['players']:
        player_dict = dict_data['players'][pid]
        for year in dict_data['years']:
            try:
                if player_dict[str(year)]['stats']:
                    yd = dict(player_dict[str(year)])
                    values = list()

                    values.append(yd['draft_keeper']) if 'draft_keeper' in yd.keys() else values.append('')
                    values.append(yd['draft_price']) if 'draft_price' in yd.keys() else values.append('')
                    values.append(yd['draft_cap_percentage']) if 'draft_cap_percentage' in yd.keys() else values.append('')

                    values.append(yd['stats']['Projected {}'.format(year)]['total']['f_avg']) if 'Projected {}'.format(year) in yd['stats'].keys() else values.append('')
                    values.append(yd['stats']['Total {}'.format(year)]['total']['f_avg']) if 'Total {}'.format(year) in yd['stats'].keys() else values.append('')
                    values.append(yd['stats']['Projected {}'.format(year)]['total']['f_total']) if 'Projected {}'.format(year) in yd['stats'].keys() else values.append('')
                    values.append(yd['stats']['Total {}'.format(year)]['total']['f_total']) if 'Total {}'.format(year) in yd['stats'].keys() else values.append('')

                    df.loc[int(pid), idx[year, YEAR_COLUMNS]] = values
                    # print(df.loc[int(pid)])
                    # print(df)
                    # print()
                else:
                    # empty stats data for the year
                    continue
            except KeyError as ex:
                # print(ex)
                # no stats data for the year
                continue
        # df.loc[]

        # player_data = get_players_data_as_df(dict_data['players'][pid], dict_data['years'])
        # df = pandas.concat([df, player_data])
        # print(df)
        # pass



    print(df)
    return df


if __name__ == '__main__':
    args = get_args()
    pandas_data = main(args.league_id)
    save_to_csv(pandas_data, args.league_id)
