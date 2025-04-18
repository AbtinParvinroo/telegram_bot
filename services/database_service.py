import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        dbname="your_db_name", 
        user="your_db_user", 
        password="your_db_password", 
        host="localhost", 
        port="5432"
    )
    return conn
