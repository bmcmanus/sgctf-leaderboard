from flask import Flask, jsonify
import config
from model import *
import json

app = Flask(__name__)

app.debug = True

#Router
@app.route("/api/board")
def get_board_list():
    return "%s" % json.dumps(Board.query.all(), default=ctf_model)

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
    