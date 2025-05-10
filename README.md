Go to your psql directive 
Windows: cd user/program files/postgres etc... 

To create the db:
createdb rental_db
psql -U postgres -d rental_db -f current.sql
          User^ rental_db^
Make sure the parameters match the env variables we have in connector.py which is your psql login information
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/your_db")
                                                User^                        rental_db^
