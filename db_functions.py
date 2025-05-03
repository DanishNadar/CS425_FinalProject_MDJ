from connector import connect

def createUser(email, name, userType):
    sql = "INSERT INTO Users (email, name, userType) VALUES (%s, %s, %s);"
    return executeSQL(sql, (email, name, userType))

def createAgent(agentEmail, jobTitle, agency, phoneNumber):
    sql = """INSERT INTO Agent (agentEmail, jobTitle, agency, phoneNumber)
             VALUES (%s, %s, %s, %s);"""
    return executeSQL(sql, (agentEmail, jobTitle, agency, phoneNumber))

def createRenter(renterEmail, desMoveInDate, prefLoc, budget, rewPo=0):
    sql = """INSERT INTO Renter
                (renterEmail, desMoveInDate, prefLoc, budget, rewPo)
             VALUES (%s, %s, %s, %s, %s);"""
    return executeSQL(sql, (renterEmail, desMoveInDate, prefLoc, budget, rewPo))

def createAddress(userEmail, city, state, zipCode):
    sql = "INSERT INTO Address (userEmail, city, state, zip) VALUES (%s, %s, %s, %s);"
    return executeSQL(sql, (userEmail, city, state, zipCode))

def createCC(userEmail, billingAddID, number, expDate, ctype):
    sql = """INSERT INTO Credit_Card
                (userEmail, billingAddID, cardNumber, expDate, cardType)
             VALUES (%s, %s, %s, %s, %s);"""
    return executeSQL(sql, (userEmail, billingAddID, number, expDate, ctype))

def listAvailableProperties():
    sql = """
    SELECT p.propertyID, p.description, p.rental_price, n.name AS neighborhood
      FROM Property p
      LEFT JOIN Neighborhood n ON p.neighborhood_id = n.neighborhood_id
     WHERE p.availability = TRUE
     ORDER BY p.propertyID;
    """
    return fetchAllItems(sql)

def bookProperty(propertyID, renterEmail, cardID):
    sqlInsert = """
      INSERT INTO Booking (booking_date, propertyID, renterEmail, cardID)
      VALUES (CURRENT_DATE, %s, %s, %s);
    """
    sqlUpdate = """
      UPDATE Property
         SET availability = FALSE
       WHERE propertyID = %s;
    """
    co = connect()
    if not co:
        return False
    try:
        with co:
            with co.cursor() as c:
                c.execute(sqlInsert, (propertyID, renterEmail, cardID))
                c.execute(sqlUpdate, (propertyID,))
        return True
    except Exception as e:
        print("ERROR: Booking Property:", e)
        return False
    finally:
        co.close()
      
def executeSQL(sql, params=()):
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

def fetchAllItems(sql, params=()):
    co = connect()
    if not co:
        return []
    try:
        with co.cursor() as cur:
            c.execute(sql, params)
            return c.fetchAll()
    except Exception as e:
        print("SQL ERROR:", e)
        return []
    finally:
        conn.close()
