import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

host = "localhost"  
database = "postgres" 
user = "postgres"  
password = os.getenv("DB_PASS")  
port = os.getenv("DB_PORT")
conn = None

try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host = host,
        dbname = database,
        user = user,
        password = password,
        port = port
    )

    # Tạo một con trỏ
    cursor = conn.cursor()

     # Câu lệnh truy vấn với LIMIT
    select_query = "SELECT * FROM employees LIMIT 10;"

    # Thực hiện câu lệnh
    cursor.execute(select_query)

    # Lấy tất cả các bản ghi
    records = cursor.fetchall()

    # In kết quả ra log
    print("5 bản ghi đầu tiên trong bảng employees:")
    for record in records:
        print(record)

except Exception as e:
    print("Lỗi:", e)

finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
