#from app import app
#from app.controladores.controlador import tasks
from flask import jsonify
from flaskext.mysql import MySQL

class Model:

    def __init__(self,app):
        self.mysql=MySQL()
        app.config['MYSQL_DATABASE_USER']='root'
        app.config['MYSQL_DATABASE_PASSWORD']='1234'
        app.config['MYSQL_DATABASE_DB']='Silabo'
        app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
        self.mysql.init_app(app)

        self.con=self.mysql.connect()
        self.cursor=self.con.cursor()

    def task_autor(self, id):
        self.cursor.execute("SELECT * from autor where aut_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'aut_ide':result[0], 'aut_nom':result[1], 'aut_ape':result[2]}
            data.append(content)
            content={}
            return data
    def task_Bibliografia(self, id):
        self.cursor.execute("SELECT * from Bibliografia where bib_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'bib_ide':result[0], 'bib_nom':result[1], 'bib_edi':result[2],'bib_editorial':result[3]}
            data.append(content)
            content={}
            return data
    def task_silabo(self, id):
        self.cursor.execute("SELECT * from Silabo where sil_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'sil_ide':result[0], 'sil_sem':result[1], 'sil_inst_eva':result[2],'sil_per_aca':result[3],'sil_fun':result[4],'sil_sum':result[5],'sil_req_apro':result[6]}
            data.append(content)
            content={}
            return data
    def task_capitulo(self, id):
        self.cursor.execute("SELECT * from capitulo where cap_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'cap_ide':result[0], 'cap_nom':result[1], 'uni_aca_ide':result[2]}
            data.append(content)
            content={}
            return data
    def task_estrategia_evaluacion(self, id):
        self.cursor.execute("SELECT * from estrategia_evaluacion where est_eva_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'est_eva_ide':result[0], 'est_eva_eva_cont':result[1], 'est_eva_eva_per':result[2],'est_eva_tip_eva':result[3],'est_eva_inst_eva':result[4],'sil_ide':result[5]}
            data.append(content)
            content={}
            return data
    def task_estrategia_aprendizaje(self, id):
        self.cursor.execute("SELECT * from estrategia_aprendizaje where est_apre_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'est_apre_ide':result[0], 'est_apre_tip':result[1], 'est_apre_desc':result[2]}
            data.append(content)
            content={}
            return data
    def task_prerequisitos(self, id):
        self.cursor.execute("SELECT * from prerequisitos where pre_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'pre_ide':result[0], 'curs_ide':result[1], 'pre_cur_ide':result[2]}
            data.append(content)
            content={}
            return data
    def task_cronograma(self, id):
        self.cursor.execute("SELECT * from cronograma where cro_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'cro_ide':result[0], 'cro_eva':result[1], 'cro_fecha':result[2], 'cro_exa_teo':result[3], 'cro_eva_cont':result[4], 'cro_eva_pond':result[5], 'est_eva_ide':result[6]}
            data.append(content)
            content={}
            return data
    def task_tema(self, id):
        self.cursor.execute("SELECT * from tema where tem_ide="+id)
        rv=self.cursor.fetchall()

        data = []
        content = {}

        for result in rv:
            content={'tem_ide':result[0], 'tem_nom':result[1], 'tem_sem':result[2], 'tem_porcen':result[3], 'cap_ide':result[4]}
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
