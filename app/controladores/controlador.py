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
    
    '''cursor.execute('SELECT * from Silabo')
    rv = cursor.fetchall()
    data=[]
    content={}
    for result in rv:
        content={'sil_ide':result[0], 'sil_sem':result[1], 'sil_inst_eva':result[2],'sil_per_aca':result[3],'sil_fun':result[4],'sil_sum':result[5],'sil_req_apro':result[6]}
        data.append(content)
        content={}
    return jsonify(data)'''