import csv
from .connector import connect

# User Management Functions
def create_user(email, name, user_type):
    conn = connect()
    if conn is None:
        print("Connection to the database failed.")
        return False
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO Users (email, name, user_type) VALUES (%s, %s, %s)",
                (email, name, user_type)
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"Error creating user: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_user(email):
    conn = connect()
    if conn is None:
        print("Connection to the database failed.")
        return None
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users WHERE email = %s", (email,))
            return cur.fetchone()
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
    finally:
        conn.close()

# Agent Functions
def create_agent(agent_email, job_title, agency, phone_number):
    conn = connect()
    if conn is None:
        print("Connection to the database failed.")
        return False
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO Agent (agent_email, job_title, agency, phone_number) 
                VALUES (%s, %s, %s, %s)""",
                (agent_email, job_title, agency, phone_number)
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"Error creating agent: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# Renter Functions
def create_renter(renter_email, desired_move_in_date, preferred_location, budget, reward_points=0):
    conn = connect()
    if conn is None:
        print("Connection to the database failed.")
        return False
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO Renter (renter_email, desired_move_in_date, 
                preferred_location, budget, reward_points) 
                VALUES (%s, %s, %s, %s, %s)""",
                (renter_email, desired_move_in_date, preferred_location, budget, reward_points)
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"Error creating renter: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
