import mysql.connector


def create_new_table():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='testdb14'
    )
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(100),
    email varchar(255)   
    )
    '''
    cursor.execute(create_table_query)
    conn.close()


create_new_table()
