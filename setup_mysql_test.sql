CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Query creates new database, if it doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Query creates new user with password protected access,
-- if user doesn't already exist.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Query grants the SELECT priviledge on an existing database.
-- User is only allowed to retrieve data.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Query grants all priviledges to the newly created database.
-- User may create, update, retrieve, and delete.
