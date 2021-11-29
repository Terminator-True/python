from flask import Flask,render_template
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    with MongoClient('localhost',27017,username='admin',password='Admin@123',authSource='JoelFarell') as client:
        mydb = client.JoelFarell
        mycol = mydb.estudiants
    return render_template('hello.html', list=mycol.find())
