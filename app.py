from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)





if __name__ == "__main__":
    app.run(debug=True)


@app.route('/users',methods=['GET'])
def get_users():
    return jsonify({"payload": "success"})

@app.route('/user', methods=['POST'])
def post_user():
    return jsonify({"payload": "success"})

@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({"payload": "success"})
    
@app.route('/user', methods=['PUT']) #h4 falla el test pero esta correcto
def update_user():
    return jsonify({"payload": "success"})

@app.route('/api/v1/users')
def get_users_version_one():
    data = list()
    return jsonify({"payload": data})
    
@app.route('/api/v1/user', methods=['POST']) #h6
def send_user_data():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({"payload": {
        'email': email,
        'name': name
    }})

@app.route('/api/v1/user/add', methods=['POST']) #h7
def send_user_form_data():
    id = request.form.get('id')
    email = request.form.get('email')
    name = request.form.get('name')
    return jsonify({"payload": {
        'email': email,
        'name': name,
        'id': id
    }})

@app.route('/api/v1/user/create', methods=['POST']) #h7
def send_user_json_data():
    data = request.get_json()
    id = data['id']
    email = data['email']
    name = data['name']
    return jsonify({"payload": {
        'email': email,
        'name': name,
        'id': id,
    }})