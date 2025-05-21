import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        database='tech_solidariobd',
        cursorclass=pymysql.cursors.DictCursor
    )