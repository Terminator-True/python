from flask import Flask,render_template,request,redirect,url_for
from Get_data import *
from init import *  
init()
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/in',methods = ['POST', 'GET'])
def llistar(dades=mostra_dades()):
    return render_template('index.html',productes=dades)

@app.route('/signin',methods = ['POST', 'GET'])
def signin():
    if request.method=="POST":
        user = request.form['user']
        password = request.form['psswd']
        guarda_usuari(user,password)
        next = request.args.get('next', None)
        if next:
            return redirect("/")

    return render_template('signin.html')
