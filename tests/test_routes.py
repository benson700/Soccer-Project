from routes import app
from football.models import Player, Team
import json

def test_add_player():
    player = Player(
        player_name='Peter Pieper',
        player_nationality='Canada',
        player_number=8
    )

    assert player.player_name == 'Peter Pieper'
    assert type(player.player_nationality) is str
    assert type(player.player_number) is int



def test_add_team():
    
    team = Team(
        team_name='Boston City',
        team_coach='John Doe',
        team_location='Boston',
        players= 'Michael Davi'
    )

    assert team.team_name == 'Boston City'
    assert team.team_coach == 'John Doe'
    assert team.team_location != None 
    assert type(team.players) is str
    


def test_get_players():
    res = app.test_client().get('/players')
    assert res.status_code == 200
    print(res.data)
    assert type(res.data[0]) is int
    assert b"Something" not in res.data


def test_get_player_by_id():
    res = app.test_client().get('/players/1')
    assert json.loads(res.data.decode('utf-8')).get('player_nationality') == 'Mexico'
    assert json.loads(res.data.decode('utf-8')).get('player_name') == 'John Doe'
    assert json.loads(res.data.decode('utf-8')).get('player_number') == 9
    assert res.status_code == 200