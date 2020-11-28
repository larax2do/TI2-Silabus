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


 #Agregar Docente
    def addDocente(self):
        print(request.json)
        query = f'INSERT INTO Docente (doc_dni , doc_nom , doc_ape_pat , doc_ape_mat , doc_grad_aca , dep_aca_ide ) VALUES ({request.json["dni"]},"{request.json["name"]}","{request.json["lastname1"]}","{request.json["lastname2"]}","{request.json["gradoacademico"]}",{request.json["depAcademico"]})'
        print (query)
        self.cursor.execute(query)
        self.con.commit()
        return "Insert Succesful"

    #Buscar Docente
    def searchDocente(self, dni):
        Docentes = []
        query = "SELECT doc_dni , doc_nom , doc_ape_pat , doc_ape_mat , doc_grad_aca , dep_aca_ide FROM Docente WHERE doc_dni = %s AND doc_del_date is null "
        self.cursor.execute(query, (dni,))
        data = self.cursor.fetchall()

        for dnis in data:
            s = {}
            s["doc_dni"] = dnis[0]
            s["doc_nom"] = dnis[1]
            s["doc_ape_mat"] = dnis[2]
            s["doc_ape_pat"] = dnis[3]
            s["doc_grad_aca"] = dnis[4]
            s["dep_aca_ide"] = dnis[5]
            Docentes.append(s)

        return jsonify(Docentes)

    #Borrar Docente
    def deleteDocente(self,id):
        query = "UPDATE Docente SET doc_del_date=now() WHERE doc_ide= %s"
        self.cursor.execute(query, (id,))
        self.con.commit()
        return "Docente Eliminado"

    # Actualizar Docente
    def updateDocente(self ):
        newdata = request.json
        t = newdata["doc_ide"]
        
        query = "UPDATE Docente SET doc_dni = %s , doc_nom = %s, doc_ape_pat = %s, doc_ape_mat = %s, doc_grad_aca = %s, dep_aca_ide = %s WHERE doc_ide = %s" 

        print (query)
    
        self.cursor.execute(query,( newdata["doc_dni"],newdata["doc_nom"] ,newdata["doc_ape_pat"],newdata["doc_ape_mat"],newdata["doc_grad_aca"],newdata["dep_aca_ide"],newdata["doc_ide"]))
        self.con.commit()
        return "Docente Actualizado"
        
  
    # Buscar Curso 
    def searchCurs(self, cod):
        Cursos = []
        query = "SELECT cur_cod , cur_nom , cur_sem , cur_dur , cur_hor_teo , cur_hor_prac , cur_hor_lab , cur_credi , cur_fund FROM Curso WHERE cur_cod = %s "
        
        self.cursor.execute(query, (cod,))
        data = self.cursor.fetchall()

        for codi in data:
            s = {}
            s["cur_cod"] = codi[0]
            s["cur_nom"] = codi[1]
            s["cur_sem"] = codi[2]
            s["cur_dur"] = codi[3]
            s["cur_hor_teo"] = codi[4]
            s["cur_hor_prac"] = codi[5]
            s["cur_hor_lab"] = codi[6]
            s["cur_credi"] = codi[7]
            s["cur_fund"] = codi[8]
            
            Cursos.append(s)

        return jsonify(Cursos)


###### End Rodrigo ############ End Rodrigo ############ End Rodrigo ############  End Rodrigo ############ End Rodrigo ######
