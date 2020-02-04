from nflstats import sched
from nflstats import elo_regression
from nflstats import get_game_codes
from nflstats import team_dict
import team_object as teamobj
import json


def test_sched():
    with open('miscjson.txt') as file:
        data = json.load(file)
    assert sched("Los Angeles Chargers", 2019) == data['schedule_test']


def test_elo_regression():
    teams = {}
    tst_team1 = teamobj.NflTeam('Los Angeles Chargers', 'SDG')
    tst_team2 = teamobj.NflTeam('New England Patriots', 'NWE')
    tst_team1.elo = 1800
    tst_team2.elo = 1200
    teams.update({team_dict[tst_team1.name]: tst_team1})
    teams.update({team_dict[tst_team2.name]: tst_team2})
    # test to see that the Chargers regressed 33% to the mean giving them 1700 elo
    # as well as the Patriots regressing to 1300 elo
    teams = elo_regression(teams)
    assert teams['SDG'].elo == 1700
    assert teams['NWE'].elo == 1300


def test_get_game_codes():
    codes = get_game_codes(1, 2019)
    with open('miscjson.txt') as file:
        tst_codes = json.load(file)
    assert codes == tst_codes['codes']
