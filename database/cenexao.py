import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        database='',
        cursorclass=pymysql.cursors.DictCursor
    )