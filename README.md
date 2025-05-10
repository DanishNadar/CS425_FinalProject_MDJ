Go to your psql directive 
Windows: cd user/program files/postgres etc... 

To create the db:
createdb rental_db
psql -U postgres -d rental_db -f current.sql <br />
          User^ rental_db^ <br />
Make sure the parameters match the env variables we have in connector.py which is your psql login information <br />
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/your_db") <br />
                                                User^                        rental_db^ <br />
