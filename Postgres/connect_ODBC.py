import os
import psycopg2
from dotenv import load_dotenv
  
load_dotenv()

def get_connection():
    try:
        return psycopg2.connect(
            database=os.environ['database'],
            user=os.environ['user'],
            password=os.environ['password'],
            host=os.environ['host'],
            port=int(os.environ['port']),
        )
    except:
        return False
  
conn = get_connection()
  
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered an error.")