from flask import Flask, request, jsonify
from helper.flow_client import create_flow_client, call_flow, create_user_message
from helper.env import get_key_from_env

app = Flask(__name__)
flow_client = create_flow_client()

# Armazenamento global dos snippets
snippets = []
next_id = 1  # Para gerar IDs únicos

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

    return jsonify({"assistant": assistant})

@app.route('/snippets', methods=['GET'])
def get_snippets():
    """Retorna todos os snippets armazenados."""
    return jsonify(snippets), 200

@app.route('/snippets', methods=['POST'])
def create_snippet():
    """Cria um novo snippet e o adiciona à lista global."""
    global next_id  # Acessa a variável global next_id
    data = request.get_json()

    # Validação básica dos dados de entrada
    if 'content' not in data or 'manual_tags' not in data:
        return jsonify({"error": "Bad request, 'content' and 'manual_tags' are required."}), 400

    snippet = {
        'id': next_id,
        'content': data['content'],
        'tags': data['manual_tags']
    }

    snippets.append(snippet)
    next_id += 1  # Incrementa o ID para o próximo snippet

    return jsonify(snippet), 201

@app.route('/snippets/<int:snippet_id>', methods=['GET'])
def get_snippet(snippet_id):
    """Retorna um snippet específico pelo ID."""
    snippet = next((s for s in snippets if s['id'] == snippet_id), None)
    if snippet is None:
        return jsonify({"error": "Snippet not found"}), 404
    return jsonify(snippet), 200

@app.route('/snippets/<int:snippet_id>', methods=['DELETE'])
def delete_snippet(snippet_id):
    """Deleta um snippet específico pelo ID."""
    global snippets
    snippets = [s for s in snippets if s['id'] != snippet_id]
    return jsonify({"message": "Snippet deleted"}), 200

if __name__ == '__main__':
    should_start_as_debug = get_key_from_env("FLASK_DEBUG")
    app.run(host='0.0.0.0', port=5000, debug=should_start_as_debug)