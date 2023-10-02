import flask
from flask import Flask,jsonify, request


#Criando aplicação
app = Flask(__name__)

games = [
    {
        'id': 1 ,
        'titulo': 'Final Fantasy',
        'ano': '1987'
    },
    
    {
        'id': 2,
        'titulo': 'Final Fantasy II',
        'ano': '1988'
    },
    
    {
        'id':3,
        'titulo': 'Final Fantasy Legend I',
        'ano':  '1989'
    },
    {
        'id':4,
        'titulo': 'Final Fantasy III',
        'ano': '1990'
    }
    
]

# GET
@app.route('/games',methods=['GET'])
def get_games():
    return jsonify(games)

# GET by id
@app.route('/games/<int:id>',methods=['GET'])
def get_games_by_id(id):
    for game in games:
        if game.get('id') == id:
            return jsonify (game)
# Post
@app.route('/games',methods=['POST'])
def add_new_game():
    new_game = request.get_json()
    games.append(new_game)
    
    return jsonify(games)

# Put
@app.route('/games/<int:id>',methods=['PUT'])
def edit_games_by_id(id):
    changed_game = request.get_json()
    for indice, game in enumerate(games):
        if game.get('id') == id:
            games[indice].update(changed_game)
            return jsonify(games[indice])

# Delete
@app.route('/games/<int:id>',methods=['DELETE'])
def delete_games(id):
    for indice, game in enumerate(games):
        if game.get("id") == id:
            del games[indice]
            
    return jsonify(games)


app.run(port=5000,host='localhost',debug=True)