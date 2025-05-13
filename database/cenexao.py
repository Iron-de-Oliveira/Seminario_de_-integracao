import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='',
        cursorclass=pymysql.cursors.DictCursor
    )