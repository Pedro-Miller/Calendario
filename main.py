import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

from functions import cadastro, checa_existe


calendario = Flask(__name__)
calendario.secret_key = "abc"  


@calendario.route("/")
def rota_home():
    return render_template("base.html")


@calendario.route("/cadastro")
def rota_cadastro():
    return render_template("cadastro.html")

@calendario.route("/cadastro_", methods =["POST"])
def cadastrando():
    if request.method == "POST":
        n = request.form["nome"]
        d = request.form["dre"]
        s = request.form["senha"]
        return cadastro(n, d, s)
    

    
@calendario.route("/login")
def rota_login():
    return render_template("login.html")
    
@calendario.route("/login_", methods =["POST"])
def login():

    if request.method == "POST":
        nome = request.form["nome"]
        dre = request.form["dre"]
        senha = request.form["senha"]
        
calendario.run()