from flask import Flask, render_template,redirect,request,session
from flask import current_app as app

@app.route("/login", methods=["POST"])
def login():
  if request.method == "POST":
        pwd = request.form.get("password")
        email = request.form.get("email")

  return redirect('/user_dashboard')

@app.route("/dashboard", methods=["GET","POST"])

def dashboard():

  if request.method == "GET":

      return "<p> this is your dashboard</p>"

  return redirect('/user_dashboard')

@app.route("/register", methods=["POST"])

def login():

  if request.method == "POST":

        pwd = request.form.get("password")

        email = request.form.get("email")

        fullname= request.form.get("fullname")
  return redirect('/login')
