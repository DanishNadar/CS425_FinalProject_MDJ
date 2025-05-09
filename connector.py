import os
import psycopg2
from psycopg2.extras import RealDictCursor


def connect():
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:strong_password@localhost:5432/rental_db")

    
    try:
        return psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    except Exception as e:
        print("ERROR: Could not connect to database:", e)
        return None
