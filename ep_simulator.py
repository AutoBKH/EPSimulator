from flask import Flask
from flask import request
from event import Event
import json
import pickle

app = Flask(__name__)


@app.route('/')
def sanity():
    return 'EP Simulator is up and running\n'


@app.route('/publish', methods=['POST'])
def publish():
    if request.method == 'POST':
        if request.is_json:
            return request.json
        else:
            return str(request.data, "utf-8")
    else:
        return f"called publish with {request.method}"


# @app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        if request.is_json:
            print(f"Changing configuration")
            return request.json
        else:
            return str(request.data, "utf-8")
    elif request.method == 'GET':
        return f"The current configuration is: "


def about():
    return "about page"

def send_event():
    if request.is_json:
        print(f"Changing configuration")
        return request.json
    else:
        unpickle = Event(pickle.loads(request.data))

        return str(request.data, "utf-8")
    return f"Received send_event"



app.add_url_rule('/config', view_func=config, methods=['POST', 'GET'])
app.add_url_rule('/about', view_func=about, methods=['POST', 'GET'])
app.add_url_rule('/send_event', view_func=send_event, methods=['POST'])

# app.view_functions['about'] = about



@app.route('/start', methods=['POST'])
def start_simulator():
    if request.method == 'POST':
        return f"Starting simulator"
    else:
        return f"Unrecognized request"


@app.route('/stop', methods=['POST'])
def stop_simulator():
    if request.method == 'POST':
        return f"Stopping simulator"
    else:
        return f"Unrecognized request"


@app.route('/restart', methods=['POST'])
def restart_simulator():
    if request.method == 'POST':
        return f"Restarted simulator"
    else:
        return f"Unrecognized request"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
