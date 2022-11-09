-- creates a database and a user that only has privelege to that database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE user IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
