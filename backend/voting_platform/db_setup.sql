CREATE DATABASE KW_Awards_dev_db; -- Create the database
CREATE USER KW_Awards_dev_user WITH PASSWORD 'yourpassword'; -- Create the user
ALTER ROLE KW_Awards_dev_user SET client_encoding TO 'utf8'; -- Set the encoding
ALTER ROLE KW_Awards_dev_user SET default_transaction_isolation TO 'read committed'; -- Set the transaction isolation level
ALTER ROLE KW_Awards_dev_user SET timezone TO 'UTC'; -- Set the timezone
GRANT ALL PRIVILEGES ON DATABASE KW_Awards_dev_db TO KW_Awards_dev_user; -- Grant privileges to the user on the database
\l -- List all your databases
\c KW_Awards_dev_db -- Connect to your database
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- Create the uuid-ossp extension
\du -- List all your users and their privileges
