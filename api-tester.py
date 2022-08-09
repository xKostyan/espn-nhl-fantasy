import json

from espn_api.hockey import League

# league_21 = League(league_id=41610, year=2021, espn_s2='AEADOJun9D920hFg9bVRD62KG9%2BSh7%2FpJrSlI%2BdBMlaBpVSCZQU5H%2BwbrBi%2BRhJb7M95FLt4mKhPjkU1h4kIzed3fsJ5Nj2RcmFQbQWbmDd2TUlBthkSpFuOVNbXnobQ4%2FxWT6vGEJwyrsaGByB6OGAgHDTQw%2BGLOAYvoXrPqq6V4rWUi73Y8NqHb86nnR0OosGwr9V2XZJv59p%2Fpp4htijMynxTOGsKTB349WvzDbTWOeD9QSHniodDLyF4SZ6HiIouD1U7OBYsV9zE5qX7F91jsRBcOn2LtIljA%2FsUiqweog%3D%3D', swid='{0F6AF922-7F7D-42DF-AFFF-30995AF832B6}')
# fa_21 = league_21.free_agents(size=3000)
#
# league_23 = League(league_id=41610, year=2023, espn_s2='AEADOJun9D920hFg9bVRD62KG9%2BSh7%2FpJrSlI%2BdBMlaBpVSCZQU5H%2BwbrBi%2BRhJb7M95FLt4mKhPjkU1h4kIzed3fsJ5Nj2RcmFQbQWbmDd2TUlBthkSpFuOVNbXnobQ4%2FxWT6vGEJwyrsaGByB6OGAgHDTQw%2BGLOAYvoXrPqq6V4rWUi73Y8NqHb86nnR0OosGwr9V2XZJv59p%2Fpp4htijMynxTOGsKTB349WvzDbTWOeD9QSHniodDLyF4SZ6HiIouD1U7OBYsV9zE5qX7F91jsRBcOn2LtIljA%2FsUiqweog%3D%3D', swid='{0F6AF922-7F7D-42DF-AFFF-30995AF832B6}')
# fa_23 = league_23.free_agents(size=3000)
#
# league_22 = League(league_id=41610, year=2022, espn_s2='AEADOJun9D920hFg9bVRD62KG9%2BSh7%2FpJrSlI%2BdBMlaBpVSCZQU5H%2BwbrBi%2BRhJb7M95FLt4mKhPjkU1h4kIzed3fsJ5Nj2RcmFQbQWbmDd2TUlBthkSpFuOVNbXnobQ4%2FxWT6vGEJwyrsaGByB6OGAgHDTQw%2BGLOAYvoXrPqq6V4rWUi73Y8NqHb86nnR0OosGwr9V2XZJv59p%2Fpp4htijMynxTOGsKTB349WvzDbTWOeD9QSHniodDLyF4SZ6HiIouD1U7OBYsV9zE5qX7F91jsRBcOn2LtIljA%2FsUiqweog%3D%3D', swid='{0F6AF922-7F7D-42DF-AFFF-30995AF832B6}')
# fa_22 = league_22.free_agents(size=3000)
# standing = league_22.standings()
# draft = league_22.espn_request.get_league_draft()


years = [2021, 2022, 2023]
kwargs = {
    'league_id': 41610,
    'espn_s2': 'AEADOJun9D920hFg9bVRD62KG9%2BSh7%2FpJrSlI%2BdBMlaBpVSCZQU5H%2BwbrBi%2BRhJb7M95FLt4mKhPjkU1h4kIzed3fsJ5Nj2RcmFQbQWbmDd2TUlBthkSpFuOVNbXnobQ4%2FxWT6vGEJwyrsaGByB6OGAgHDTQw%2BGLOAYvoXrPqq6V4rWUi73Y8NqHb86nnR0OosGwr9V2XZJv59p%2Fpp4htijMynxTOGsKTB349WvzDbTWOeD9QSHniodDLyF4SZ6HiIouD1U7OBYsV9zE5qX7F91jsRBcOn2LtIljA%2FsUiqweog%3D%3D',
    'swid': '{0F6AF922-7F7D-42DF-AFFF-30995AF832B6}'
}

# dump data to files
for year in years:
    kwargs['year'] = year
    league = League(**kwargs)
    fa = league.free_agents(size=10000)
    draft = league.espn_request.get_league_draft()
    print()
    with open('{}-player-year-to-year.txt'.format(year), 'w') as f:
        json.dump(fa, f, indent=2)