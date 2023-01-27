from flask import Flask
from flask import jsonify
from flask import request

from config.config import config
from config.sql import SQL

from business.business_logic import *

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    # init conection sql
    SQL.init()
    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/catalog/<name>', methods=['GET'])
def get_users(name):
    return get_catalog({
        'name_catalog': name
    })

@app.route('/student/register', methods=['POST', 'PUT'])
def post_register_student():
    if request.method == 'POST':
        return register_student(request.get_json(force=True))
    else:
        return update_register_student(request.get_json(force=True))
    
@app.route('/student/accept', methods=['PUT'])
def put_accept_student_request():
    return accept_student_request(request.get_json(force=True))

@app.route('/requests/<id_grimonio>', methods=['GET'])
def get_requests(id_grimonio):
    return get_estudents_by_grimonios({"id_grimonio": id_grimonio})

@app.route('/requests', methods=['GET','DELETE'])
def request_student():
    if request.method == 'GET':
        return get_requests_estudents()
    else:
        return delete_request_student(request.get_json(force=True))

if __name__ == '__main__':
    app.run(debug=True, port=4000)