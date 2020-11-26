#from app import app
#from app.controladores.controlador import tasks
from flask import jsonify
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

    def agregarCronograma(self, cro_eva, cro_fecha, cro_exa_teo,cro_eva_con,sil_ide):
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
    def modificarCronograma(self,cro_ide,cro_eva, cro_fecha, cro_exa_teo,cro_eva_con):
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