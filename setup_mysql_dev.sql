CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Query creates new database, if it doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Query creates new user with password protected access,
-- if user doesn't already exist.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Query grants the SELECT priviledge on existing database.
-- User is only allowed to retrieve data.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Query grants all priviledges to the newly created database.
-- User may create, update, retrieve, and delete.
