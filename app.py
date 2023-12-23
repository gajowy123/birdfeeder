from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.get("/")
def hello_world():
    return render_template("start.html")

@app.post("/")
def handle_form():
    return request.form["name"]
    


@app.route("/test")
def some_stuff():
    a=2+2
    return f"2+2={a}"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)