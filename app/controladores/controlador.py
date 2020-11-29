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

###### Rodrigo ############ Rodrigo ############ Rodrigo ############ Rodrigo ############ Rodrigo ######

# *  [Modificar Sílabo]
@app.route('/silabo/silabo/modificar',methods=['POST'])
def modificarSilabo():
    return jsonify(model.modificarSilabo(request.json['sil_ide'],request.json['sil_per'],request.json['sil_inf_espe'],request.json['sil_comp_asig'],request.json['sil_eva_apre'],request.json['sil_req_apro']))

# *  [Agregar Sílabo]
@app.route('/silabo/silabo/agregar',methods=['POST'])
def agregarSilabo():
    return model.agregarSilabo()
# *  [Agregar Contenido]
@app.route('/silabo/unidad_academica/agregar',methods=['POST'])
def agregarUnidad():
    return model.agregarUnidad()

@app.route('/silabo/capitulo/agregar',methods=['POST'])
def agregarCapitulo():
    return model.agregarCapitulo()

@app.route('/silabo/tema/agregar',methods=['POST'])
def agregarTema():
    return model.agregarTema()

# *  [Modificar Contenido]
@app.route('/silabo/unidad_academica/modificar',methods=['POST'])
def modificarUnidad():
    return jsonify(model.modificarUnidad(request.json['uni_aca_ide'],request.json['uni_nom']))
@app.route('/silabo/capitulo/modificar',methods=['POST'])
def modificarCapitulo():
    return jsonify(model.modificarCapitulo(request.json['cap_ide'],request.json['cap_nom']))
@app.route('/silabo/tema/modificar',methods=['POST'])
def modificarTema():
    return jsonify(model.modificarTema(request.json['tem_ide'],request.json['tem_nom'],request.json['tem_sem'],request.json['tem_porcen']))

###### End Rodrigo ############ End Rodrigo ############ End Rodrigo ############  End Rodrigo ############ End Rodrigo #######

######  Jhoel ############  Jhoel ############  Jhoel ############   Jhoel ############ Jhoel ######
#Buscar un silabo por ID
@app.route('/BuscarSilabo/<id>',methods=['POST'])
def BuscarSilabo(id):
    return jsonify(model.BuscarSilabo(id))

#Delete por ID
@app.route('/DeleteSilabo/<id>',methods=['DELETE'])
def DeleteSilabo(id):
    return jsonify(model.DeleteSilabo(id))

#Agrega Bibliografia
@app.route('/AsignarBibliografia/',methods=['POST'])
def AsignarBibliografias():
    return model.AsignarBibliografias()

#Delete Bibliografia
@app.route('/DeleteBibliografia/<id>',methods=['DELETE'])
def DeleteBibliografia(id):
    return jsonify(model.DeleteBibliografia(id))

#Buscar un silabo por ID
@app.route('/BuscarBibliografia/<id>',methods=['GET'])
def BuscarBibliografia(id):
    return model.BuscarBibliografia(id)


###### End Jhoel ############ End Jhoel ############ End Jhoel ############  End Jhoel ############ End Jhoel ######


###### End José ############ End José ############ End José ############  End José ############ End José ######


#Agregar Docente
@app.route('/addDocente', methods=['POST'])
def Add_docentes ():
    return model.addDocente()
    
#Buscar Docente
@app.route('/searchDocente/<dni>', methods=['GET'])
def Search_docentes (dni):
    return model.searchDocente(dni)

#Borrar Docente
@app.route('/deleteDocente/<dni>', methods=['GET'])
def DeleteDocentes (dni):
    return model.deleteDocente(dni)

# Actualizar Docente
@app.route('/updateDocente', methods=['POST'])
def UpdateDocentes ():
    return model.updateDocente()

# Buscar Curso 
@app.route('/searchCurs/<cod>', methods=['GET'])
def SearchCurso (cod):
    return model.searchCurs(cod)

###### End José ############ End José ############ End José ############  End José ############ End José ######

