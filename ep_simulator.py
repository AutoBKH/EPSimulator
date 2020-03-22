from flask import Flask
from flask import request
import json

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


@app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        if request.is_json:
            print(f"Changing configuration")
            return request.json
        else:
            return str(request.data, "utf-8")
    elif request.method == 'GET':
        return f"The current configuration is: "


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
        return f"Stopping simulator"
    else:
        return f"Unrecognized request"

if __name__ == "__main__":
    app.run(debug=True)
