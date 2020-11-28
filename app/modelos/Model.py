#from app import app
#from app.controladores.controlador import tasks
from flask import jsonify,request
from flaskext.mysql import MySQL

class Model:

    def __init__(self,app):
        self.mysql=MySQL()
        app.config['MYSQL_DATABASE_USER']='root'
        app.config['MYSQL_DATABASE_PASSWORD']='gonzalito'
        app.config['MYSQL_DATABASE_DB']='Silabo2'
        app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
        self.mysql.init_app(app)

        self.con=self.mysql.connect()
        self.cursor=self.con.cursor()

    def tasks(self, id):
        self.cursor.execute("SELECT * from Silabo where sil_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'sil_ide':result[0], 'sil_sem':result[1], 'sil_inst_eva':result[2],'sil_per_aca':result[3],'sil_fun':result[4],'sil_sum':result[5],'sil_req_apro':result[6]}
            data.append(content)
            content={}
            return data

    def nSilabo(self,sil_ide,sil_sem,sil_inst_eva,sil_per_aca,sil_fun,sil_sum,sil_req_apro):

        params={
            'sil_ide':sil_ide,
            'sil_sem':sil_sem,
            'sil_inst_eva':sil_inst_eva,
            'sil_per_aca':sil_per_aca,
            'sil_fun':sil_fun,
            'sil_sum':sil_sum,
            'sil_req_apro':sil_req_apro
        }
        query="""INSERT INTO Silabo (sil_ide,sil_sem,sil_inst_eva,sil_per_aca,sil_fun,sil_sum,sil_req_apro) VALUES (%(sil_ide)s, %(sil_sem)s, %(sil_inst_eva)s, %(sil_per_aca)s, %(sil_fun)s, %(sil_sum)s, %(sil_req_apro)s);"""
        self.cursor.execute(query,params)
        self.con.commit()

        return params

###### Thales ########### Thales ########### Thales ########### Thales ########### Thales ########### Thales ########### Thales #####

    def agregarCronogramaEva(self, cro_eva, cro_fecha, cro_exa_teo,cro_eva_con,sil_ide):
        params={
            'cro_eva':cro_eva,
            'cro_fecha':cro_fecha, 
            'cro_exa_teo':cro_exa_teo,
            'cro_eva_con':cro_eva_con,
            'sil_ide':sil_ide
        }
        query="""INSERT INTO Cronograma_evaluacion(cro_eva, cro_fecha, cro_exa_teo,cro_eva_con,sil_ide) VALUES (%(cro_eva)s,%(cro_fecha)s,%(cro_exa_teo)s,%(cro_eva_con)s,%(sil_ide)s);"""
        self.cursor.execute(query,params)
        self.con.commit()

        return params
    def modificarCronogramaEva(self,cro_ide,cro_eva, cro_fecha, cro_exa_teo,cro_eva_con):
        params={
            'cro_ide':cro_ide,
            'cro_eva':cro_eva,
            'cro_fecha':cro_fecha,
            'cro_exa_teo':cro_exa_teo,
            'cro_eva_con':cro_eva_con
        }
        query="""UPDATE Cronograma_evaluacion SET cro_ide=%(cro_ide)s,cro_eva=%(cro_eva)s, cro_fecha=%(cro_fecha)s, cro_exa_teo=%(cro_exa_teo)s,cro_eva_con=%(cro_eva_con)s WHERE cro_ide= %(cro_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()
        return params
    def buscarCronogramaEva(self,sil_ide):
        self.cursor.execute("SELECT * from Cronograma_evaluacion WHERE sil_ide="+str(sil_ide))
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'cro_ide':result[0], 'cro_eva':result[1], 'cro_fecha':result[2],'cro_exa_teo':result[3],'cro_eva_con':result[4]}
            data.append(content)
            content={}
        return data

    def buscarContenido(self,sil_ide):
        params={
            'sil_ide':sil_ide
        }
        query="""SELECT Unidad_academica.uni_aca_ide, Unidad_academica.uni_nom, Capitulo.cap_ide, Capitulo.cap_nom, Tema.tem_ide, Tema.tem_nom, Tema. tem_sem, Tema.tem_porcen
        FROM Tema
        INNER JOIN Capitulo ON Tema.cap_ide=Capitulo.cap_ide
        INNER JOIN Unidad_academica ON Capitulo.uni_aca_ide=Unidad_academica.uni_aca_ide
        WHERE sil_ide=%(sil_ide)s
        """
        self.cursor.execute(query,params)
        rv=self.cursor.fetchall()     

        data=[]
        content={}

        for result in rv:
            content={'uni_aca_ide':result[0], 'uni_nom':result[1], 'cap_ide':result[2],'cap_nom':result[3],'tem_ide':result[4],'tem_nom':result[5],'tem_sem':result[6],'tem_porcen':result[7]}
            data.append(content)
            content={}
        return data

    def quitarContenidoUnidad(self,uni_aca_ide):
        params={
            'uni_aca_ide':uni_aca_ide,
        }
        query="""DELTE FROM Unidad_academica WHERE uni_aca_ide=%(uni_aca_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()

        return params  

    def quitarContenidoCapitulo(self,cap_ide):
        params={
            'cap_ide':cap_ide,
        }
        query="""DELTE FROM Capitulo WHERE cap_ide=%(cap_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()

        return params

    def quitarContenidoTema(self,tem_ide):
        params={
            'tem_ide':tem_ide,
        }
        query="""DELTE FROM Tema WHERE tem_ide=%(tem_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()

        return params 

###### End Thales ############ End Thales ############ End Thales ############ End Thales ############ End Thales ######

###### Rodrigo ############ Rodrigo ############ Rodrigo ############ Rodrigo ############ Rodrigo ######
    def modificarSilabo(self,sil_ide,sil_per, sil_inf_espe, sil_comp_asig,sil_eva_apre,sil_req_apro):
        params={
            'sil_ide':sil_ide,
            'sil_per':sil_per,
            'sil_inf_espe':sil_inf_espe,
            'sil_comp_asig':sil_comp_asig,
            'sil_eva_apre':sil_eva_apre,
            'sil_req_apro':sil_req_apro
        }
        query="""UPDATE silabo SET sil_ide=%(sil_ide)s,sil_per=%(sil_per)s, sil_inf_espe=%(sil_inf_espe)s, sil_comp_asig=%(sil_comp_asig)s,sil_eva_apre=%(sil_eva_apre)s,sil_req_apro=%(sil_req_apro)s WHERE sil_ide= %(sil_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()
        return params

    def modificarUnidad(self,uni_aca_ide,uni_nom):
        params={
            'uni_aca_ide':uni_aca_ide,
            'uni_nom':uni_nom
        }
        query="""UPDATE unidad_academica SET uni_aca_ide=%(uni_aca_ide)s,uni_nom=%(uni_nom)s WHERE uni_aca_ide= %(uni_aca_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()
        return params

    def modificarCapitulo(self,cap_ide,cap_nom):
        params={
            'cap_ide':cap_ide,
            'cap_nom':cap_nom
        }
        query="""UPDATE capitulo SET cap_ide=%(cap_ide)s,cap_nom=%(cap_nom)s WHERE cap_ide= %(cap_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()
        return params

    def modificarTema(self,tem_ide,tem_nom,tem_sem,tem_porcen):
        params={
            'tem_ide':tem_ide,
            'tem_nom':tem_nom,
            'tem_sem':tem_sem,
            'tem_porcen':tem_porcen
        }
        query="""UPDATE tema SET tem_ide=%(tem_ide)s,tem_nom=%(tem_nom)s,tem_sem=%(tem_sem)s,tem_porcen=%(tem_porcen)s WHERE tem_ide= %(tem_ide)s;"""
        self.cursor.execute(query,params)
        self.con.commit()
        return params

    def agregarSilabo(self):
        print(request.json)
        query = f'INSERT INTO silabo (sil_per , sil_inf_espe , sil_comp_asig , sil_eva_apre , sil_req_apro ) VALUES ({request.json["periodo"]},"{request.json["informe"]}","{request.json["asignado"]}","{request.json["evaluacion"]}","{request.json["requisitos"]}")'
        print (query)
        self.cursor.execute(query)
        self.con.commit()
        return "Insert Succesful"

    def agregarUnidad(self):
        print(request.json)
        query = f'INSERT INTO unidad_academica (uni_aca_ide , uni_nom ) VALUES ({request.json["id"]},"{request.json["nombre"]}")'
        print (query)
        self.cursor.execute(query)
        self.con.commit()
        return "Insert Succesful"

    def agregarCapitulo(self):
        print(request.json)
        query = f'INSERT INTO capitulo (cap_ide , cap_nom ) VALUES ({request.json["id"]},"{request.json["nombre"]}")'
        print (query)
        self.cursor.execute(query)
        self.con.commit()
        return "Insert Succesful"
    def agregarTema(self):
        print(request.json)
        query = f'INSERT INTO tema (tem_ide , tem_nom , tem_sem , tem_porcen ) VALUES ({request.json["id"]},"{request.json["nombre"]}","{request.json["semestre"]}","{request.json["porcentaje"]}")'
        print (query)
        self.cursor.execute(query)
        self.con.commit()
        return "Insert Succesful"
###### End Rodrigo ############ End Rodrigo ############ End Rodrigo ############  End Rodrigo ############ End Rodrigo ######
