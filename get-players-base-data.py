from datetime import date, datetime
from typing import Tuple
import argparse
import json

from espn_api import requests
from espn_api.hockey import League


def get_args():
    parser = argparse.ArgumentParser(description='Get credential values by loging into espn league, inspect page, '
                                                 'Application tab -> Storage -> Cookies -> "http://fantasy.espn.com". '
                                                 'Find required values in the list.')
    parser.add_argument('--league_id', type=int, help='Id of the fantasy league', required=True)
    parser.add_argument('--espn_s2', type=str, help='expn_s2 credentials value', required=True)
    parser.add_argument('--swid', type=str, help='swid credentials value', required=True)
    return parser.parse_args()


def get_league_config(_league_id) -> dict:
    """
    Return config for provided league
    :param int _league_id: ID of the espn league. League must be setup with 'init-new-league.py' prior to this.
    """
    with open('espn-data/{}/league-config.json'.format(_league_id)) as _f:
        return json.load(_f)


def get_years() -> list:
    """
    Generate a list of years to get data about players for.
    It starts at 2019 due to the fact that current API does not support earlier years.
    """
    init_year = 2019
    current_year = date.today().year
    current_month = date.today().month

    # next year season is generated by espn somewhere in August
    # predictions for the next season are generated by espn somewhere in September
    # hence the range offset, otherwise if run during Jan - July
    # it would try to request data for the year that does not exist
    offset = 2
    if current_month in range(1, 7):
        offset = 1

    ret = list(range(init_year, current_year+offset))
    # need to reverse the range, as current year is used as 'init' for the data schema
    # and uses players map from a current year
    ret.reverse()
    return ret


def setup_schema(_league_args) -> dict:
    """
    Returns a top level data structure (dict). Use with 'current year'.
    :param dict _league_args: Dict with values to use as **kvargs to get league info.
    :return: Dictionary with defined player ids.
    """
    league = League(**_league_args)
    schema = dict()
    schema['years'] = list()
    schema['players'] = {key: dict() for key in league.player_map.keys() if isinstance(key, int)}
    for key in schema['players']:
        schema['players'][key]['name'] = league.player_map[key]
    return schema


def get_fantasy_avg(_stats, _league_config, _is_goalie, _name) -> Tuple[float, float]:
    """
    returns fantasy avg value for players stats based on league scoring
    :param dict _stats: stats dictionary of a player.
    :param dict _league_config: League config dictionary to calculate points
    """

    avg = 0.0
    total = 0.0
    try:
        if _is_goalie:
            scoring = _league_config['scoring']['goaltenders']
        else:
            scoring = _league_config['scoring']['skaters']

        for key in scoring:
            if key not in _stats.keys():
                continue
            total += scoring[key] * _stats[key]
        if _is_goalie:
            avg = total / _stats['GS']
        else:
            avg = total/_stats['GP']
    except KeyError as ex:
        print(ex)
        print('Error: {name}\n{stat}'.format(name=_name, stat=_stats))
        return 0.0, 0.0
    return avg, total


def del_key(_dict, _key):
    if _key in _dict:
        del _dict[_key]


def aggregate_data(_full_data, _league_config, _free_agents, _draft, _year) -> dict:
    for player in _free_agents:
        is_goalie = False
        avg = 0.0
        total = 0.0
        player_dict = clean_player_dict(vars(player))
        if player_dict['position'] == 'Goalie':
            is_goalie = True

        for stat in player_dict['stats']:
            avg, total = get_fantasy_avg(player_dict['stats'][stat]['total'], _league_config, is_goalie, player_dict['name'])
            player_dict['stats'][stat]['total']['f_avg'] = avg
            player_dict['stats'][stat]['total']['f_total'] = total
        _full_data['players'][player.playerId][_year] = player_dict
    return _full_data


def clean_player_dict(_player_dict) -> dict:
    del_key(_player_dict, 'lineupSlot')
    del_key(_player_dict, 'eligibleSlots')
    del_key(_player_dict, 'acquisitionType')
    del_key(_player_dict, 'injuryStatus')
    del_key(_player_dict, 'injured')
    for stat in _player_dict['stats']:
        if 'Total' or 'Projected' in stat:
            pass
        else:
            del_key(_player_dict['stats'], stat)
    return _player_dict


def main():
    args = get_args()
    kwargs = {
        'league_id': args.league_id,
        'espn_s2': args.espn_s2,
        'swid': args.swid
    }

    league_config = dict()
    try:
        league_config = get_league_config(kwargs['league_id'])
    except FileNotFoundError:
        print('Unable to locate configuration for League_id: {}.'
              '\nSetup with "init-new-league.py"'.format(kwargs['league_id']))
        exit(-1)

    years = get_years()
    kwargs['year'] = years[0]
    full_data = setup_schema(kwargs)
    for year in years:
        print('Getting data for year {} ...'.format(year))
        kwargs['year'] = year
        try:
            league = League(**kwargs)
            full_data['years'].append(year)
            fa = league.free_agents(size=10000)
            draft = league.espn_request.get_league_draft()
            full_data = aggregate_data(full_data, league_config, fa, draft, year)

        except requests.espn_requests.ESPNAccessDenied:
            print("Logged-in user does not have access to year {}".format(year))
            pass


if __name__ == '__main__':
    main()



