import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='adimin',
        database='tech_solidariobd',
        cursorclass=pymysql.cursors.DictCursor
    )