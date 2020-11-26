from flask import json
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

@app.route('/nSilabo',methods=['POST'])
def nSilabo():
    return jsonify(model.nSilabo(request.json['sil_ide'],request.json['sil_sem'],request.json['sil_inst_eva'],request.json['sil_per_aca'],request.json['sil_fun'],request.json['sil_sum'],request.json['sil_req_apro']))
    
# 3.1.3 [Agregar Cronograma de Evaluacion]
@app.route('/silabo/cronograma/agregar',methods=['POST'])
def agregarCronograma():
    return jsonify(model.agregarCronograma(request.json['cro_eva'], request.json['cro_fecha'], request.json['cro_exa_teo'],request.json['cro_eva_con'],request.json['sil_ide']))

# * 3.3.2 [Modificar Cronograma de Evaluacion]
@app.route('/silabo/cronograma/modificar',methods=['POST'])
def modificarCronograma():
    return jsonify(model.modificarCronograma(request.json['cro_ide'],request.json['cro_eva'],request.json['cro_fecha'],request.json['cro_exa_teo'],request.json['cro_eva_con']))

# * 3.2.3 [Buscar Cronograma de Evaluacion]
