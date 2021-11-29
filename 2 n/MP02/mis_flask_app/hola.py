from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', list=[1,2,3,4,5,6,7,8])
