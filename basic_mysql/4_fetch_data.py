import mysql.connector


def fetch_table_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='testdb14'
    )
    cursor = conn.cursor()
    query = '''
            SELECT * FROM users
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


data = fetch_table_data()
for row in data:
    print(row)
