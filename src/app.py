from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

user = [{ "Name": "Ximena", "edad": 26 },
        { "Name": "Javier", "edad": 32 },
        ]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

@app.route('/user/<int:position2>', methods=['GET'])
def get_user(position2):
    print("This is the position to get:", position2)
    get_user_from_list = user[position2]
    if get_user_from_list is not None:
        return jsonify(get_user_from_list)
    else:
        return jsonify({"error": "usuario no encontrado"}), 404






# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)