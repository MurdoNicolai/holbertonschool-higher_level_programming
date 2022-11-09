-- creates id_not_null same as table 3 but id has default value 1
CREATE TABLE IF NOT EXISTS id_not_null(
	id 		INT 			default 1,
	name 	VARCHAR(256) 	not NULL
	);

