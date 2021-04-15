from flask import Flask
from flask import request
from flask.templating import render_template
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/param", methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name',"Kimchulsu")
    if request.method == "GET":
        name = request.args.get('name','kimchulz')
#     request.args.get('name','user01')
    return "param=" + name


@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('forward.html',title=title)


if __name__ == "__main__":
    app.run()