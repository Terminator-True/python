from flask import Flask,render_template,request,redirect,url_for
from manage_data import *
from init import *  
init()
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def login():
    if request.method=="POST":
        user = request.form.get('user_login')
        password = request.form.get('psswd_login')
        if comprova_usuari(user,password):
            return llistar()
        else:
            return render_template('login.html',error="Error, usuari o password incorrecte")
    return render_template('login.html')

@app.route('/in')
def llistar(dades=mostra_dades()):
    return render_template('index.html',productes=dades)

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
    if request.method=="POST":
        user = request.form.get('user')
        password = request.form.get('psswd')
        if guarda_usuari(user,password):
            return llistar()
        else:
            return render_template('signin.html',error="Error, usuari existent")
    return render_template('signin.html')
