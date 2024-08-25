import psycopg2
import os

def connect_db():
    connection = psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db',  # Имя сервиса контейнера PostgreSQL
        port='5432'
    )
    return connection

def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            position VARCHAR(100)
        );
        """)
        conn.commit()

def insert_data(conn):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", ('Alice', 'Developer'))
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", ('Bob', 'Designer'))
        conn.commit()

def fetch_data(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employees;")
        records = cursor.fetchall()
        for record in records:
            print(record)

if __name__ == "__main__":
    conn = connect_db()
    create_table(conn)
    insert_data(conn)
    fetch_data(conn)
    conn.close()
