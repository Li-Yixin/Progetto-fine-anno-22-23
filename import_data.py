# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS SOLAR_SYSTEM")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS SOLAR_SYSTEM.System_Planet (
    Planet VARCHAR(30) NOT NULL, 
    Color VARCHAR(100),
    Mass FLOAT,
    Diameter FLOAT,
    Density FLOAT,
    Surface Gravity FLOAT,
    Escape Velocity INT,
    Rotation Period INT,
    Length of Day FLOAT,
    Distance from Sun FLOAT,
    Perihelion FLOAT,
    Aphelion FLOAT,
    Orbital Period FLOAT,
    Orbital Velocity FLOAT,
    Orbital Inclination FLOAT,
    Orbital Eccentricity FLOAT,
    Obliquity to Orbit FLOAT,
    Mean Temperature FLOAT,
    Surface Pressure FLOAT,
    Number of Moons FLOAT,
    PRIMARY KEY (Planet)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM SOLAR_SYSTEM.System_Planet")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./planets.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO SOLAR_SYSTEM.System_Planet VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)