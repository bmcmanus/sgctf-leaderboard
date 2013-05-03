from flask import Flask, jsonify, request
from sqlalchemy import *
import config
from model import *
import json
import os

app = Flask(__name__)
app.debug = True
# curl -H "Content-Type:application/json" http://localhost:5000/api/player/create -d '{"name":"Team Name/Persons Name"}'

# curl -s -X POST -H "Content-Type:application/json" http://localhost:5000/api/player/create -d '{"name":"Team Aalphaaaaa"}'
@app.route("/api/player/create", methods=['GET', 'POST'])
def post_player():
    db.session.rollback()
    db.session.flush()

    if request.method == 'GET':
        return(json.dumps({'error': 'I... GET what you did but something isn\'t quite right here. '}))
    elif request.method == 'POST':
        token = os.urandom(16).encode('hex')
        try:
            db.session.add(Player(request.json['username'] if 'username' in request.json else u'', request.json['name'] if request.json['name'] else u'', u'', token, 1, 0))
        except exc.IntegrityError:
            db.session.rollback()
            db.session.flush()
            return(json.dumps({'error': 'Mmm, sorry. Your name isn\'t unique.'}))
        db.session.commit()
    return(json.dumps({"token": token}))
#    return json.dumps(request.json['username'])
    
#Router
@app.route("/api/board")
def get_board_list():
    return json.dumps(Board.query.all(), default=ctf_model)

@app.route("/api/player/<int:in_id>")
def get_player_by_id(in_id):
    return json.dumps(Player.query.filter_by(id=in_id).all(), default=ctf_model)

@app.route("/api/player/<string:in_username>")
def get_player_by_username(in_username):
    return json.dumps(Player.query.filter_by(username=in_username).all(), default=ctf_model)

@app.route("/")
def hello():
    return "View not available for application, just yet."

if __name__ == "__main__":
    if app.debug: use_debugger = True
    try:
        # Disable Flask's debugger if external debugger is requested
        use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
    except:
        pass
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
    app.run()
    #python 
    #from model import db