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
    

###### Thales ########### Thales ########### Thales ########### Thales ########### Thales ########### Thales ########### Thales #####

# 3.1.3 [Agregar Cronograma de Evaluacion]
@app.route('/silabo/cronogramaEva/agregar',methods=['POST'])
def agregarCronogramaEva():
    return jsonify(model.agregarCronogramaEva(request.json['cro_eva'], request.json['cro_fecha'], request.json['cro_exa_teo'],request.json['cro_eva_con'],request.json['sil_ide']))

# * 3.3.2 [Modificar Cronograma de Evaluacion]
@app.route('/silabo/cronogramaEva/modificar',methods=['POST'])
def modificarCronogramaEva():
    return jsonify(model.modificarCronogramaEva(request.json['cro_ide'],request.json['cro_eva'],request.json['cro_fecha'],request.json['cro_exa_teo'],request.json['cro_eva_con']))

# * 3.2.2 [Buscar Cronograma de Evaluacion]
@app.route('/silabo/cronogramaEva/buscar',methods=['POST'])
def buscarCronogramaEva():
    return jsonify(model.buscarCronogramaEva(request.json['sil_ide']))

# * 3.2.1 [Buscar contenido]
@app.route('/silabo/contenido/buscar',methods=['POST'])
def buscarContenido():
    return jsonify(model.buscarContenido(request.json['sil_ide']))

# * 3.4.1 [Quitar Contenido]
@app.route('/silabo/contenido/quitar/unidad',methods=['POST'])
def quitarContenidoUnidad():
    return jsonify(model.quitarContenidoUnidad(request.json['uni_aca_ide']))

@app.route('/silabo/contenido/quitar/capitulo',methods=['POST'])
def quitarContenidoCapitulo():
    return jsonify(model.quitarContenidoCapitulo(request.json['cap_ide']))

@app.route('/silabo/contenido/quitar/tema',methods=['POST'])
def quitarContenidoTema():
    return jsonify(model.quitarContenidoTema(request.json['tem_ide']))

###### End Thales ############ End Thales ############ End Thales ############ End Thales ############ End Thales 