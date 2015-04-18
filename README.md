leaderboard
===========
#About
Small CTF leaderboard written in Python by Brian McManus

#Note
There is a lot of work to still be done.  Right now I've created underpinnings so en0 can instrument iibot with api calls.

#Requirements
pip install Flask sqlalchemy Flask-SQLAlchemy jsonify simplejson jinja2

#Docker (preferred method)
 * docker build -t sgctf .
 * docker run -d -p 5000:5000 sgctf

#Getting Started (venv, local development)
 * virtualenv venv
 * source venv/bin/activate
 * pip install -r requirements.txt
 * python src/create_schema.py
 * python src/ctf.py
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
#Copyright
    Copyright 2013, Brian McManus, SocialGeeks

#License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

