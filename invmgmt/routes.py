from flask import render_template, request, url_for
from invmgmt import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


    