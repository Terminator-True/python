from flask import Flask,render_template,request,redirect,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/usuaris"
mongo = PyMongo(app)

@app.route('/login')
def form(name=None):
    return render_template('hello2.html')

@app.route('/success/<name>')
def success(name=None):
   return render_template('success.html',name=name)

@app.route('/failure')
def failure():
   return render_template('failure.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    user = request.form['user']
    password = request.form['psswd']

    if user == mongo.db.usuaris.find_one({"user":user}):
        if password == mongo.db.usuaris.find_one({"password":password}):
            return redirect(url_for('success',name = user))
    else:
        return redirect(url_for('failure'))
