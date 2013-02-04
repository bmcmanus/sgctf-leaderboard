leaderboard
===========
#About
Small CTF leaderboard written in Python

#Requirements
pip install Flask sqlalchemy Flask-SQLAlchemy jsonify simplejson

#Getting Started
 * Install requirements
 * Call python create_schema.py
 * Execute ala python ctf.py
 * Browse http://localhost:5000/api/board
 * Profit, add some entries to the board and enjoy.


#Example Usage
 * curl http://localhost:5000/api/player/brian
 * curl http://localhost:5000/api/player/1
 * curl http://localhost:5000/api/board

#Design
Two routes
## /
User-facing service.

##/api
Services API allows gets/puts of leaderboard modifications
Requires basic http authentication over ssl. Allowed API keys stored in DB.
###/api/player/<integer id>
###/api/player/<string username>
###/api/board
##/
Web Application


