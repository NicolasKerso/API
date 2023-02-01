# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:37:48 2022

@author: leleu
"""
from flask import *
from app import app
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
import os 
import matplotlib.pyplot as plt
global prenom 
global nom
global P
global c
global FOIS
global contents
global b

x = []
FOIS=[]
import random
L=[]
for i in range (1,2000):
    L.append(i)
app.secret_key = str(random.choice(L))
c=0

                       
@app.route('/', methods =["GET" , "POST"])
def index():   
    if 'nom'and 'prenom' in session:
        session.clear()
    return render_template('index.html' )
    


@app.route('/biceps',methods = ["GET" , "POST"])
def biceps():
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"]
    return render_template('biceps.html' , title = 'Biceps', nom=session['nom'] , prenom=session['prenom'])

@app.route('/triceps', methods = ["GET" , "POST"])
def triceps():
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"]
    return render_template('triceps.html' , title = 'triceps', nom=session['nom'] , prenom=session['prenom'])

@app.route('/biceps/curl_banc_inc', methods = ["GET" , "POST"])
def curl_banc_inc():
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"]
    return render_template('curl_banc_inc.html' , title = 'curl_banc_inc', nom=session['nom'] , prenom=session['prenom'])


@app.route('/purgatoire' , methods = ["GET", "POST"])
def purgatoire():
    value = request.form
    if value["but"] == "tonifier" :
        return render_template('tonifier.html' , title = 'tonifier' , page_tonifier = value)
    if value["but"] == "volume":
        return render_template('volume.html' , title = 'volume' , page_tonifier = value)
    if value ["but"] == "puissance":
        return render_template('puissance.html' , title = 'puissance' , page_tonifier = value)
        
@app.route('/biceps/curl_barre', methods = ["GET", "POST"])    
def curl_barre():
    return render_template('curl_barre.html' , title = 'curl_barre', nom=session['nom'] , prenom=session['prenom'])
    
@app.route('/login' , methods = ["GET" , "POST"])
def login():
    global c
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"]
        
        
    else:
        value = request.form
        print(session)
        session["nom"]=value['nom']
        session["prenom"]=value['prenom']
        nom=session["nom"]
        prenom=session["prenom"]
        
        
    
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO compte (prenom,nom) VALUES (?,?)",(session["prenom"],session["nom"]))
        con.commit()  
        print("enregistré avec succès")
    con.close()
          
    return render_template('login.html' , title = 'login' , nom=session['nom'] , prenom=session['prenom'] )
    

@app.route('/Poids', methods = ["GET", "POST"])    
def Poids():
    nom=""
    prenom=""
    nom_graph=""
    global c
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"]
        
    if "nom_graph" in session : 
        nom_graph = session["nom_graph"]
    
    else : 
        session["nom_graph"] = nom_graph
    
        
    
    fichier = nom+prenom
    nom_fichier = fichier+'.txt'
    poids = request.form.get("poids")
    nom_graph= fichier+'.png'
    
    if request.method == 'POST':
        if poids:
            with open(nom_fichier, "a") as f:
                f.write(poids + "\n")
        
            values = []
            with open(nom_fichier, "r") as f:
                values = [float(v) for v in f.readlines()]
                
            plt.cla()
            plt.plot(range(len(values)), values)
            plt.xlabel('nombre de fois où tu as enregistré ton poids')
            plt.ylabel('Poids')
            plt.xticks(rotation=70)
            ax = plt.gca()
            ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
            plt.savefig("app/static/images/" + nom_graph)
            values=[]
            session["nom_graph"] = nom_graph
        
        else:
            return "Pas de valeur"

    return render_template('Poids.html' , title = 'Tracking Poids' , nom=nom , prenom=prenom ,nom_graph = session["nom_graph"])


@app.route('/Poids/graph', methods = ["GET", "POST"])    
def graph():
    nom=""
    prenom=""
    nom_graph = ""
    if 'nom'and 'prenom' in session:
        nom=session["nom"]
        prenom=session["prenom"] 
        
    if "nom_graph" in session : 
        nom_graph = session["nom_graph"]
        
    return render_template('graph.html' , title = 'Tracking Poids' , nom=nom , prenom=prenom, nom_graph = session["nom_graph"])
    


    



        