-- creates the cities table in hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/*
	Cities (table):
	ID (autogenerated unique)
	name (none null)
	state_id (refers to the id in state table)
*/
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
  id 	  						INTEGER 		    PRIMARY KEY		  AUTO_INCREMENT,
  name							VARCHAR(256)  		NOT NULL,
  state_id						INTEGER,
  FOREIGN KEY (state_id) 		REFERENCES states(id)
);


