from flask import render_template, request, url_for, redirect
from invmgmt import app
from invmgmt.items import records
import os


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/importexcel', methods=["POST", "GET"])
def importexcel():
    if request.method == "POST":
        excel = request.files['excel']
        excel.save(f"./invmgmt/static/{excel.filename}")
        print(excel)
        global database
        database = records(f"./invmgmt/static/{excel.filename}")
        return redirect(url_for("view"))
    else:
        return render_template('importexcel.html')


@app.route("/view")
def view():
    global database
    return render_template("view.html", values=database)
