from flask import Flask, request, jsonify
from helper.flow_client import create_flow_client, call_flow, create_user_message
from helper.env import get_key_from_env

app = Flask(__name__)
flow_client = create_flow_client()


@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'


@app.route('/call-flow', methods=['POST'])
def flow_endpoint():
    data = request.json
    
    if 'userMessage' not in data:
        return jsonify({"error": "Field 'userMessage' is required"}), 400
    
    user_message = data['userMessage']

    assistant = call_flow(flow_client, [create_user_message(user_message)])

    return jsonify({"assistant:": assistant})


if __name__ == '__main__':

    should_start_as_debug = get_key_from_env("FLASK_DEBUG")

    app.run(host='0.0.0.0', port=5000, debug=should_start_as_debug) 