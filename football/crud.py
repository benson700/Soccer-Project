from football.models import Team, Player
from football import db
import json

'''
a module for CRUD operations
'''


def player_json(self):
    '''
    a method to parse the output in json format
    '''
    data = {
        'id': self.id,
        'player_name': self.player_name,
        'player_nationality': self.player_nationality,
        'player_number': self.player_number
    }
    return data


def add_player(name, nationality, number):
    '''
    create a player - CREATE
    '''
    player = Player(
        player_name=name,
        player_nationality=nationality,
        player_number=number
    )

    db.session.add(player)
    db.session.commit()


def get_all_players():
    '''
    get all players - RETRIEVE
    '''
    return [player_json(player) for player in Player.query.all()]


def get_player(id):
    '''
    get a single player - RETRIEVE
    '''
    player = Player.query.filter_by(id=id).first()
    return player_json(player)


def delete_player(id):
    Player.query.filter_by(id=id).delete()
    db.session.commit()


def update_player(id, player_number):
    update = Player.query.filter_by(id=id).first()
    update.player_number = player_number
    db.session.commit()


def add_team(name, coach, location):
    team = Team(
        team_name=name,
        team_coach=coach,
        team_location=location
    )

    db.session.add(team)
    db.session.commit()



def add_player_to_team(team, player):
    team = Team.query.filter_by(team_name=team)
    print(team.player.player_name)
    team.player.player_name = player
    db.session.commit()