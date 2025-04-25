import os
import pandas as pd
import sqlite3 as sql3
from datetime import datetime, date
from flask import flash, session, redirect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
today = str(datetime.today().date())
today = today.replace("-", "_")
db_name = "staff_" + str(today) + ".db"


def createDB():
    conn=sql3.connect(os.path.join(BASE_DIR, db_name))
    conn.commit()
    conn.close()


def db_conn():
    conn = sql3.connect('dbs/' + db_name)
    conn.row_factory = sql3.Row
    return conn


def call_db(sqlQuery):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dbData = conn.execute(sqlQuery,).fetchall()
    conn.close()
    return dbData


def call_db_one(sqlQuery, adition):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dbData = conn.execute(sqlQuery, adition).fetchone() # SEE adition as a tuple
    conn.close()
    return dbData


def call_db_one_dict(sqlQuery, adition):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    conn.row_factory = sql3.Row
    dbData = conn.execute(sqlQuery, adition).fetchone() # SEE adition as a tuple
    conn.close()
    return dbData


def call_db_all(sqlQuery, adition):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dbData = conn.execute(sqlQuery, adition).fetchall()
    conn.close()
    return dbData


def call_db_all_dict(sqlQuery, adition):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    conn.row_factory = sql3.Row
    dbData = conn.execute(sqlQuery, adition).fetchall()
    conn.close()
    return dbData


def createTable(sqlQuery):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    cur = conn.cursor()
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def save_db(dataframe, table):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dataframe.to_sql(name=table, con=conn, if_exists="replace", index=False)
    conn.close()


def save_response(dataframe, table):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dataframe.to_sql(name=table, con=conn, if_exists="append", index=False)
    conn.close()


def call_db_con(sqlQuery, adition):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dbData = conn.execute(sqlQuery, (adition,)).fetchall()
    conn.close()
    return dbData


def call_db_two_all_dict(sqlQuery, data1, data2):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    conn.row_factory = sql3.Row
    dbData = conn.execute(sqlQuery, (data1, data2)).fetchone()
    conn.close()
    return dbData


def call_db_two_all(sqlQuery, data1, data2):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    dbData = conn.execute(sqlQuery, (data1, data2)).fetchall()
    conn.close()
    return dbData


def update_db(sqlQuery, data1, data2):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    cur = conn.cursor()
    cur.execute(sqlQuery, (data1, data2))
    conn.commit()
    conn.close()


def updateInforme(sqlQuery):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    cur = conn.cursor()
    cur.execute(sqlQuery)
    conn.commit()
    conn.close()


def delete_two_db(sqlQuery, data1, data2):
    conn = sql3.connect(os.path.join(BASE_DIR, db_name))
    cur = conn.cursor()
    cur.execute(sqlQuery, (data1, data2))
    conn.commit()
    conn.close()


def to_test():
    sqlQuery = """ CREATE TABLE ToTest (
        FICHA TEXT NOT NULL, 
        DOCAPRENDIZ TEXT NOT NULL, 
        APRENDIZ_NAME TEXT NOT NULL, 
        APRENDIZ_LAST TEXT NOT NULL, 
        DOCINSTRUCTOR TEXT NOT NULL, 
        INSTRUCTOR_NAME TEXT NOT NULL, 
        INSTRUCTOR_LAST TEXT NOT NULL,
        PROGFORMACION TEXT NOT NULL
        )"""
    try:
        createTable(sqlQuery)
    except Exception as e:
        flash(f'Error al procesar los archivos: {str(e)}')
        return redirect('/')


def fullMixTable(request):
    sql = "SELECT * FROM Preguntas"
    preguntas = call_db(sql)

        # DATABASE Informe
    sqlQuery = """ CREATE TABLE Informe (
        FICHA TEXT NOT NULL, 
        DOCAPRENDIZ TEXT NOT NULL, 
        APRENDIZ_NAME TEXT NOT NULL, 
        APRENDIZ_LAST TEXT NOT NULL, 
        DOCINSTRUCTOR TEXT NOT NULL, 
        INSTRUCTOR_NAME TEXT NOT NULL, 
        INSTRUCTOR_LAST TEXT NOT NULL, 
        P1 TEXT NOT NULL, 
        P2 TEXT NOT NULL, 
        P3 TEXT NOT NULL, 
        P4 TEXT NOT NULL, 
        P5 TEXT NOT NULL, 
        P6 TEXT NOT NULL, 
        P7 TEXT NOT NULL, 
        P8 TEXT NOT NULL, 
        P9 TEXT NOT NULL, 
        P10 TEXT NOT NULL, 
        P11 TEXT NOT NULL, 
        P12 TEXT NOT NULL
        )"""
    
    try:
        createTable(sqlQuery)
    except:
        flash(f'La Tabla "Informe" ya existe!')
        
