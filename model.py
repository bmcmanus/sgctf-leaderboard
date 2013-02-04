from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
import config 

# DB class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  config.DB_URI
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'player'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', db.String(60), unique=True)
    email = Column('email', db.String(120), unique=True)
    token = Column('token', db.String(160), unique=True)
    board = db.relationship('Board', uselist=False, backref='player')
    active = Column('active', db.Boolean())
    admin = Column('admin',db.Boolean())
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __unicode__(self):
        return self.username

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)


class Board(db.Model):
    __tablename__ = 'board'
    id = Column('id', Integer, primary_key=True)
    player_id = Column(db.Integer, db.ForeignKey('player.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    

class Levels(db.Model):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True)
    title = Column(db.String(60))
    description = Column(db.String(512))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

"""
Allows simplejson to sort our Models
"""
def ctf_model(obj):
	if isinstance(obj, Board):
		return {'id': obj.id, 'player_id': obj.player_id, 'created_at': unicode(obj.created_at), 'updated_at':unicode(obj.updated_at)}
	elif isinstance(obj, Player):
		return []
	else:
		raise TypeError(repr(obj) + " is not JSON serializable")