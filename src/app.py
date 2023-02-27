from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)


# supongamos que tienes todos (cierta información) en una variable json
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
        response = jsonify(todos) # Puedes convertir esa variable en un string json así
        return response # Y luego puedes retornarla (return) en el response body así:

     

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position-1)
    return jsonify(todos)

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)