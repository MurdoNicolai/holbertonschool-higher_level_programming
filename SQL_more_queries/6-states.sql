/* creates a states table in hbtn_0d_usa database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- ID (autogenerated unique) and name (none null)
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
  id 	  INTEGER 		    PRIMARY KEY		  AUTO_INCREMENT,
  name	VARCHAR(256)  	NOT NULL
);

