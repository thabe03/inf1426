import urllib.parse
from flask import Flask, render_template
import pyodbc 


# Create the connection
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\xi1le\OneDrive\Bureau\Data.accdb;') 
cursor = conn.cursor()

# Create an instance of Flask 
app = Flask(__name__) 

 # Create a route and view function 
@app.route('/') 
def index(): 
    cursor.execute("SELECT DISTINCT Sujet FROM QnA") 
    rows = cursor.fetchall()
    subject="Blog"
    cursor.execute("SELECT * FROM QnA")
    default_rows = cursor.fetchall()
    return render_template("index.html",rows=rows,default_rows=default_rows)

@app.route('/subject/<string:subject>')
def subject(subject):
    cursor.execute("SELECT DISTINCT Sujet FROM QnA") 
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM QnA WHERE Sujet=?", subject)
    default_rows = cursor.fetchall()
    return render_template("subject.html",rows=rows,default_rows=default_rows)

@app.route('/article/<id>')
def article(id):
    cursor.execute("SELECT DISTINCT Sujet FROM QnA") 
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM QnA WHERE ID=?", id)
    default_row = cursor.fetchone()
    return render_template("article.html",rows=rows,question=default_row[1],reponse=default_row[2])

@app.route('/subscribe')
def subscribe():
    cursor.execute("SELECT DISTINCT Sujet FROM QnA") 
    rows = cursor.fetchall()
    return render_template("subscribe.html",rows=rows)

@app.route('/subscribe', methods=['post'])
def subscribe_submit():
    cursor.execute("SELECT DISTINCT Sujet FROM QnA") 
    rows = cursor.fetchall()
    # ajouter un courriel
    return render_template("subscribe.html",rows=rows)

app.run(host='0.0.0.0', port=81)
