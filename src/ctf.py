from flask import Flask, jsonify, request, render_template
from sqlalchemy import *
import config
from model import *
import json
import os
import jinja2
from datetime import timedelta
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir)
app.debug = True

@app.route("/api/player/create", methods=['GET', 'POST'])
def post_player():
    """
    curl -H "Content-Type:application/json" http://localhost:5000/api/player/create -d '{"name":"Team Name/Persons Name"}'
    """
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

@app.route("/api/flag/capture", methods=['POST'])
def capture_level():
    """
    curl -H "Content-Type:application/json" http://localhost:5000/api/flag/capture -d '{"token": "2b00042f7481c7b056c4b410d28f33cf", password: "9hSaVoey44Puz0fbWlHtZh5jTooLVplC"}'
    """
    db.session.rollback()
    db.session.flush()
    if 'token' in request.json and 'password' in request.json:
        if request.json['password'] == u'9hSaVoey44Puz0fbWlHtZh5jTooLVplC':
            db.session.add(Capture(request.json['token'], 1))
        elif request.json['password'] == u'aRJMGKT6H7AOfGwllwocI2QwVyvo7dcl':
            db.session.add(Capture(request.json['token'], 2))
        elif request.json['password'] == u'lOHYKVT34rB4agsz1yPJ2QvENy7YnxUb':
            db.session.add(Capture(request.json['token'], 3))
        elif request.json['password'] == u'8ywPLDUB2yY2ujFnwGUdWWp8MT4yZrqz':
            db.session.add(Capture(request.json['token'], 4))
        elif request.json['password'] == u'V0p12qz30HEUU22dz7CZGHiFk3VdPA9Z':
            db.session.add(Capture(request.json['token'], 5))
        elif request.json['password'] == u'mfPYpp1UBKKsx7g4F0LaRjhKKenYAOqU':
            db.session.add(Capture(request.json['token'], 6))
        elif request.json['password'] == u'XLoIufz83MjpTrtPvP9iAtgF48EWjicU':
            db.session.add(Capture(request.json['token'], 7))
        elif request.json['password'] == u'maabkdexUStb6JJXUqmBx7Re8M61cksn':
            db.session.add(Capture(request.json['token'], 8))
        elif request.json['password'] == u'sQ6DKR8ICwqDMTd48lQlJfbF1q9B3edT':
            db.session.add(Capture(request.json['token'], 9))
        elif request.json['password'] == u's09byvi8880wqhbnonMFMW8byCojm8eA':
            db.session.add(Capture(request.json['token'], 10))
        elif request.json['password'] == u'SUIRtXqbB3tWzTOgTAX2t8UfMbYKrgp6':
            db.session.add(Capture(request.json['token'], 11))
        elif request.json['password'] == u'sh7DrWKtb8xw9PIMkh8OQsgno6iZnJQu':
            db.session.add(Capture(request.json['token'], 12))
        elif request.json['password'] == u'IGCXqS4x472aoHZYaidvmeoWj2GmuRYz':
            db.session.add(Capture(request.json['token'], 13))
        elif request.json['password'] == u'sSkCeug1bdrYejzAaBhgwI3qJXDKqlgh':
            db.session.add(Capture(request.json['token'], 14))
        elif request.json['password'] == u'm2azll7JH6HS8Ay3SOjG3AGGlDGTJSTV':
            db.session.add(Capture(request.json['token'], 15))
        elif request.json['password'] == u'3VfCzgaWjEAcmCQphiEPoXi9HtlmVr3L':
            db.session.add(Capture(request.json['token'], 16))
        elif request.json['password'] == u'9HBzt5ljtPAgmaYvNfZ8chZVq50oepsx':
            db.session.add(Capture(request.json['token'], 17))
        else:
            return(json.dumps({"error": "That\'s not the password we're looking for...."}))
        db.session.commit()
        return(json.dumps({"status": "successful capture of this flag."}))
    else:
        return(json.dumps({'error': 'A capture requires a \'token\' and \'password\''}))

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
def display_board():
    mst = timedelta(hours=6)
#    board = db.session.query(Capture, )
#query = session.query(User, Document, DocumentsPermissions).join(Document).join(DocumentsPermissions)
    board = Player.query.order_by(Player.flag.desc()).all()
    display = []
    #this should be refactored with a list comprehension, seriously!
    i=0
    for row in board:
        i=i+1
        display.append({"rank": i, "name": row.name, "points": row.points, "flag": row.flag, "updated_at": row.updated_at-mst})
#        return json.dumps(display)
    return render_template('leaderboard.html', players=display)
#Session.query(User,Document,DocumentPermissions).filter(User.email == Document.author).\
#    filter(Document.name == DocumentPermissions.document).\
#    filter(User.email == 'someemail').all()

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
