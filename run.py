from flask import *
import sqlite3

with sqlite3.connect("database.db") as con:  
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS compte (prenom,nom)")
con.close()
# Create the application instance

# Create a URL route in our application for "/"
from app import app
app.run(port=5000, debug = True)
        

