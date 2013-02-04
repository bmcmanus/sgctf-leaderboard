leaderboard
===========
#About
Small CTF leaderboard written in Python

#Note
There is a lot of work to still be done.  Right now I've created underpinnings so en0 can instrument iibot with api calls.

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
##/
Web Application or the user-facing leaderboard with a beautiful layout.

##/api
Services API allows gets/puts of leaderboard modifications
Requires basic http authentication over ssl. Allowed API keys for specific users stored in DB.
###/api/player/<integer id>
###/api/player/<string username>
###/api/board



