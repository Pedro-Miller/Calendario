import sqlite3
from flask import Flask, render_template, request, flash

existe = bool

def cria_tabela() :
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas ([nome] TEXT NOT NULL,[dre] TEXT PRIMARY KEY,[senha] TEXT NOT NULL);
    ''')

    db.commit()

class aluno():
    def __init__(self, nome, dre, senha):
        self.nome = nome
        self.dre = dre
        self.senha = senha



def checa_existe(dre) :
        db = sqlite3.connect('database.sqlite')
        cursor = db.cursor()
        cadastro = cursor.execute("SELECT * FROM contas where dre = '"+dre+"'").fetchall()
        if len(cadastro)>0 :
                return True
        else:
                
                return False       

#checa se ja existe e se nao existir ele cria
def cadastro(nome, dre, senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    if checa_existe(dre) == False:
        cursor.execute("INSERT INTO contas VALUES ('"+nome+"','"+dre+"','"+senha+"')")
        db.commit()
        return render_template("sucesso.html")
    else:
        flash("DRE ja existe")
        return "Esse DRE ja esta cadastrado"

global user 
user = aluno("","","")
