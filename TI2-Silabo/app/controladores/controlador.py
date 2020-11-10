from app import app
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL
from app.modelos.Model import Model

model=Model(app)

@app.route('/')
def index():
    return 'hola'

@app.route('/tasks/<id>',methods=['POST'])
def tasks(id):
    return jsonify(model.tasks(id))
    


content = {}
@app.route('/insertion_SumFun', methods=['POST'])
def insertion_SumFun():
    print (request.json)
    return jsonify (content)