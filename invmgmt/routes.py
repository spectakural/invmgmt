from flask import render_template, request, url_for,redirect
from invmgmt import app
import os

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/importexcel', methods=["POST", "GET"])    
def importexcel():
    if request.method == "POST":
        req=request.form

        excel = request.files['excel']
        excel.save(f"./invmgmt/static/{excel.filename}")
        print(excel)
        return None
    else:
        return render_template('importexcel.html')

