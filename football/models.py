from football import db


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key = True)
    player_name = db.Column(db.String(30))
    player_nationality = db.Column(db.String(30))
    player_number = db.Column(db.Integer)
    

    def __str__(self):
        return self.player_name



class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.relationship('Player', backref=db.backref('player', uselist=False))
    team_name = db.Column(db.String(30))
    team_coach = db.Column(db.String(30))
    team_location = db.Column(db.String(30))
    players = db.Column(db.String(30))
    
    def __str__(self):
        return self.team_name