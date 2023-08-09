from flask import render_template
from app import app
from app.forms import LoginForm



user: dict = {"nombre": "gerardo",
              "edad": 15
              
              }


contex: dict = {"user": user}
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", context=contex)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/afiliate')
def afiliate():
    return render_template('datos_afiliacion.html')