from flask import Flask, render_template,jsonify,request

from usuario import Usuario

app = Flask(__name__)

@app.route('/getUser/',methods=['GET'] )
def getUser():
     return render_template('manutencaoUsuario.html',visibilityInfoUser="hidden")

@app.route('/getUser/',methods=['POST'] )
def postGetUser():
     return render_template('manutencaoUsuario.html',visibilityInfoUser="show")

@app.route('/getUserbyID/',methods=['GET'] )
def getUserbyID():
     return render_template('getUserbyID.html')


@app.route('/getUserbyID/',methods=['POST'] )
def postUserbyID():
     request_data = request.form
     id  = request_data['id']
     return  jsonify(Usuario.getUserbyID(id))

@app.route('/createUser/', methods=['GET'])
def getCreateUser():
     return render_template('createUser.html')

@app.route('/createUser/', methods=['POST'])
def postCreateUser():
     request_data = request.form
     nome  = request_data['nome']
     dataNascimento  = request_data['dataNascimento']
     Usuario.createUser(nome,dataNascimento)
     return render_template('createUser.html')


@app.route('/')
def index():
    comments = ['Criar Usuario',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]
    return render_template('index.html',funcoes=comments)

