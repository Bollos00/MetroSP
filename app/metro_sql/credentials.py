from sqlalchemy.engine import URL

DRIVERNAME = "postgresql"
USERNAME = "postgres"
PASSWORD = "password"
HOST = "postgresdb"
# HOST = "localhost"
PORT = 5432
DATABASE = "db"

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername=DRIVERNAME,
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE
)