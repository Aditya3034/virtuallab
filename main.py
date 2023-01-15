import flask
from flask import Flask , render_template , url_for , request , jsonify , redirect 
# from flask_sqlalchemy import SQLAlchemy
# import jinja2
# from datetime import datetime
# import joblib
app = Flask(__name__)
@app.route("/")
def home():
   return render_template("index.html")
@app.route("/extc.html")
def extc():
    return render_template("extc.html")
@app.route("/third") 
def third():
    return render_template("third.html")
@app.route("/experiment")
def experiment1():
    return render_template("experiment1.html")