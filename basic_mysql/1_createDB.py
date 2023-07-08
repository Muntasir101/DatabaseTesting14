import mysql.connector


def create_new_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE testdb14")
    conn.close()


create_new_database()
