from flask import Flask, request, jsonify
import jsonpickle

app = Flask(__name__)


def is_alive():
    return 'EP Simulator is up and running\n'


def send_event():
    if request.is_json:
        print(f"called send_event")
        return request.json
    else:
        unpickle = jsonpickle.decode(request.data)
        print(unpickle)
        return jsonify(message=unpickle["message"],
                       send_to=unpickle["send_to"])


def publish():
    if request.method == 'POST':
        if request.is_json:
            return request.json
        else:
            return str(request.data, "utf-8")
    else:
        return f"called publish with {request.method}"


app.add_url_rule('/', view_func=is_alive)
app.add_url_rule('/is_alive', view_func=is_alive)
app.add_url_rule('/send_event', view_func=send_event, methods=['POST'])
app.add_url_rule('/publish', view_func=publish, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
