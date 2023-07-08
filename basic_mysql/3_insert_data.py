import mysql.connector


def insert_data_table():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='testdb14'
    )
    cursor = conn.cursor()
    create_table_query = '''
        INSERT INTO users(name, email)
        VALUES
        ('smith', 'smith@gmail.com'),
        ('Green', 'green@gmail.com'),
        ('Kevin', 'kevin@gmail.com'),
        ('Mike', 'mike@gmail.com');
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()


insert_data_table()
