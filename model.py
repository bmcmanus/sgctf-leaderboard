from datetime import *
import config 
import md5
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float, Boolean, DateTime, exc
# DB class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)
db.session.autocommit = True
db.session.autoflush = True
"""
Captures - the ledger for players who have Captured flags to earn points
"""
class Capture(db.Model):
    __tablename__ 	 = 'captures'
    id 				 = Column(Integer, primary_key=True)
    player_id 		 = Column(Integer, db.ForeignKey('players.id'))
    flag 			 = Column(Integer, db.ForeignKey('flags.id'))
    points_earned 	 = Column(Integer)
    created_at 		 = Column(DateTime, default=db.func.now())
    updated_at 		 = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

"""
Player engaged in the contest
"""
class Player(db.Model):
    __tablename__ 	 = 'players'
    id 		   		 = Column(Integer, primary_key=True)
    username   		 = Column(String(60), unique=False)
    name			 = Column(String(60), unique=True)
    email 	   		 = Column(String(120), unique=False)
    token 	   		 = Column(String(160), unique=True)
    board 	   		 = db.relationship('Board', primaryjoin='(Player.id==Board.player_id)', backref='players')
    active     		 = Column(Boolean())
    admin 	   		 = Column(Boolean())
    created_at 		 = Column(DateTime, default=db.func.now())
    updated_at 		 = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, username, name, email, token, active, admin):
        self.username = username
        self.name = name
        self.email = email
        self.token = token
        self.admin = admin
        self.active = active
        
    def __unicode__(self):
        return self.username

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)

"""
Current board and stack-rank (may be unneeded)
"""
class Board(db.Model):
    __tablename__ 	 = 'board'
    id 				 = Column(Integer, primary_key=True)
    player_id 		 = Column(Integer, db.ForeignKey('players.id'))
    created_at 		 = Column(DateTime, default=db.func.now())
    updated_at 		 = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, player_id):
        self.player_id = player_id

"""
CTF Flags and their associated points (value)
"""
class Flag(db.Model):
    __tablename__ 	 = 'flags'
    id 				 = Column(Integer, primary_key=True)
    title 			 = Column(String(60))
    description 	 = Column(String(512))
    value 			 = Column(Integer, default=0)
    created_at 		 = Column(DateTime, default=db.func.now())
    updated_at 		 = Column(DateTime, default=db.func.now(), onupdate=db.func.now())
    def __init__(self, title, description, value):
        self.title = title
        self.description = description
        self.value = value

"""
Allows simplejson to sort our Models
"""
def ctf_model(obj):
    if isinstance(obj, Board):
        return {'id': obj.id, 'player_id': obj.player_id, 'created_at': unicode(obj.created_at), 'updated_at':unicode(obj.updated_at)}
    elif isinstance(obj, Player):
        return {'id': obj.id, 'username': obj.username, 'email': obj.email, 'token': obj.token, 'board': obj.board, 'active': obj.active, 'created_at': unicode(obj.created_at), 'updated_at':unicode(obj.updated_at)}
    else:
        raise TypeError(repr(obj) + " is not JSON serializable")
