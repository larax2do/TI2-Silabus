from app import app
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL
from app.modelos.Model import Model

model=Model(app)

@app.route('/')
def index():
    return 'hola'

@app.route('/task_autor/<id>',methods=['POST'])
def task_autor(id):
    return jsonify(model.task_autor(id))
@app.route('/task_Bibliografia/<id>',methods=['POST'])
def task_Bibliografia(id):
    return jsonify(model.task_Bibliografia(id))
@app.route('/task_silabo/<id>',methods=['POST'])
def task_silabo(id):
    return jsonify(model.task_silabo(id))
@app.route('/task_capitulo/<id>',methods=['POST'])
def task_capitulo(id):
    return jsonify(model.task_capitulo(id))
@app.route('/task_estrategia_evaluacion/<id>',methods=['POST'])
def task_estrategia_evaluacion(id):
    return jsonify(model.task_estrategia_evaluacion(id))
@app.route('/task_estrategia_aprendizaje/<id>',methods=['POST'])
def task_estrategia_aprendizaje(id):
    return jsonify(model.task_estrategia_aprendizaje(id))
@app.route('/task_prerequisitos/<id>',methods=['POST'])
def task_prerequisitos(id):
    return jsonify(model.task_prerequisitos(id))    
@app.route('/task_cronograma/<id>',methods=['POST'])
def task_cronograma(id):
    return jsonify(model.task_cronograma(id))
@app.route('/task_tema/<id>',methods=['POST'])
def task_tema(id):
    return jsonify(model.task_tema(id))
