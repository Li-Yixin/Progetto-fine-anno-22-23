from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="SOLAR_SYSTEM"
)
mycursor = mydb.cursor()

app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template('Home.html')

@app.route('/D')
def dati():
    mycursor.execute("SELECT * FROM System_Element")
    myresult = mycursor.fetchall()
    return render_template('Dati.html', units=myresult)

@app.route('/M')
def moto():
    return render_template('Moto.html')

@app.route('/G')
def galleria():
    return render_template('Galleria.html')