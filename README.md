Go to your psql directive <br />

For Windows: cd user/program files/postgres etc... <br />

To create the db: <br />
createdb rental_db <br />
psql -U postgres -d rental_db -f current.sql <br />


Make sure the parameters match the env variables we have in connector.py which is your psql login credentials <br />
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/your_db") <br />

