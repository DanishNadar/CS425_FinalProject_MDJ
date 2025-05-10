from connector import connect

def create_user(email, name, user_type):
    sql = "INSERT INTO Users (email, name, user_type) VALUES (%s, %s, %s);"
    return execute_sql(sql, (email, name, user_type))

def create_agent(agent_email, job_title, agency, phone_number):
    sql = """INSERT INTO Agent (agent_email, job_title, agency, phone_number)
             VALUES (%s, %s, %s, %s);"""
    return execute_sql(sql, (agent_email, job_title, agency, phone_number))

def create_renter(renter_email, desired_move_in_date, preferred_location, budget, reward_points=0):
    sql = """INSERT INTO Renter
                (renter_email, desired_move_in_date, preferred_location, budget, reward_points)
             VALUES (%s, %s, %s, %s, %s);"""
    return execute_sql(sql, (renter_email, desired_move_in_date, preferred_location, budget, reward_points))

def create_address(user_email, city, state, zip_code): 
    sql = "INSERT INTO Address (user_email, city, state, zip) VALUES (%s, %s, %s, %s);"
    return execute_sql(sql, (user_email, city, state, zip_code)) 

def create_cc(user_email, billing_address_id, card_number, expiration_date, card_type):
    sql = """INSERT INTO Credit_Card
                (user_email, billing_address_id, card_number, expiration_date, card_type)
             VALUES (%s, %s, %s, %s, %s);"""
    return execute_sql(sql, (user_email, billing_address_id, card_number, expiration_date, card_type))

def list_available_properties():
    sql = """
    SELECT p.property_id, p.description, p.rental_price, n.name AS neighborhood
      FROM Property p
      LEFT JOIN Neighborhood n ON p.neighborhood_id = n.neighborhood_id
     WHERE p.availability = TRUE
     ORDER BY p.property_id;
    """
    return fetch_all_items(sql)

      
def execute_sql(sql, params=()):
    co = connect()
    if not co:
        return False
    try:
        with co:
            with co.cursor() as c:
                c.execute(sql, params)
        return True
    except Exception as e:
        print("SQL ERROR:", e)
        return False
    finally:
        co.close()

def fetch_all_items(sql, params=()):
    co = connect()
    if not co:
        return []
    try:
        with co.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    except Exception as e:
        print("SQL ERROR:", e)
        return []
    finally:
        co.close()

def create_property(agent_email, city, state, zip_code, rental_price, description, sq_footage, property_type):
    co = connect()
    if not co:
        return False
    
    try:
        with co:
            with co.cursor() as c:
                c.execute("SELECT address_id FROM Address WHERE user_email = %s", (agent_email,))
                address_id = c.fetchone()['address_id']
                
                c.execute("""
                    INSERT INTO Property 
                    (agent_email, address_id, rental_price, description, sq_footage, property_type)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (agent_email, address_id, rental_price, description, sq_footage, property_type))
                
             
                c.execute("SELECT LASTVAL()")
                property_id = c.fetchone()['lastval']
                
             
                if property_type == 'House':
                    num_rooms = int(input("Number of rooms: "))
                    c.execute("""
                        INSERT INTO House (property_id, num_rooms)
                        VALUES (%s, %s)
                    """, (property_id, num_rooms))
                elif property_type == 'Apartment':
                    num_rooms = int(input("Number of rooms: "))
                    building_type = input("Building type: ")
                    c.execute("""
                        INSERT INTO Apartment (property_id, num_rooms, building_type)
                        VALUES (%s, %s, %s)
                    """, (property_id, num_rooms, building_type))
                
                
        return True
    except Exception as e:
        print("ERROR creating property:", e)
        return False
    finally:
        co.close()

def get_user(email):
    co = connect()
    if not co:
        return None
    
    try:
        with co.cursor() as cur:
            cur.execute("SELECT * FROM Users WHERE email = %s", (email,))
            return cur.fetchone()
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
    finally:
        co.close()