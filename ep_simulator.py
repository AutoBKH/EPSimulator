from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def sanity():
    return 'EP Simulator is up and running\n'


@app.route('/publish', methods=['POST'])
def publish():
    if request.method == 'POST':
        return request.json
    else:
        return f"called publish with {request.method}"


if __name__ == "__main__":
    app.run(debug=True)
