from flask import Flask
from flask import request
from flask.templating import render_template
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('db.html',title=title)


if __name__ == "__main__":
    app.run()