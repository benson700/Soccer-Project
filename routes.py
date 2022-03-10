from flask import request, Response, jsonify
from football import app
from football import crud, db
from football.models import Player


'''
a module for API routes(endpoints) which perform CRUD operations for both 
two tables (models) interactively (Player and Team)
'''


@app.route('/player', methods=['POST'])
def create_player():
    '''
    add player endpoint - CREATE
    '''
    data = request.get_json()
    player = crud.add_player(
        name=data['player_name'],
        nationality=data['player_nationality'],
        number=data['player_number'],
    )
    return Response("Player added", 201, mimetype='application/json')
    


@app.route('/players', methods=['GET'])
def get_players():
    '''
    get all players endpoint - RETRIEVE
    '''
    data = crud.get_all_players()
    return jsonify(data)


@app.route('/players/<int:id>', methods=['GET'])
def get_player_by_id(id):
    '''
    get a single player by id - RETRIEVE
    '''
    player = crud.get_player(id)
    return jsonify(player)


@app.route('/player/update/<int:id>', methods=['PUT'])
def update_player_number(id):
    number = request.get_json()
    '''
    update a player number by id - UPDATE
    '''
    player = crud.update_player(id, number['player_number'])
    return Response('Player numeber update', 200, mimetype='application/json')


@app.route('/delete/<int:id>', methods=['GET'])
def delete_player(id):
    '''
    delete a player by id - DELETE
    '''
    crud.delete_player(id)
    return Response('Player deleted', 200, mimetype='application/json')
    

@app.route('/team', methods=['POST'])
def create_team():
    '''
    add team endpoint - CREATE
    '''
    data = request.get_json()
    team = crud.add_team(
        name=data['team_name'],
        coach=data['team_coach'],
        location=data['team_location'],
    )
    return Response("Team added", 201, mimetype='application/json')




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='localhost')