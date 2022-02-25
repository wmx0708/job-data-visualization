from flask import Flask,render_template
import sqlite3
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()


@app.route('/city')
def city():
    return render_template("city.html")

@app.route('/salary')
def salary():
    return render_template("salary.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/experiment')
def experiment():
    return render_template("experiment.html")

@app.route('/company')
def company():
    return render_template("company.html")

@app.route('/aboutme')
def keyword():
    return render_template("aboutme.html")

@app.route('/aboutme')
def temp():
    return render_template("aboutme.html")


if __name__ == '__main__':
    app.run()

