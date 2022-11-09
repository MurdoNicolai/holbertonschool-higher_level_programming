-- creates unique_id same as table 4 but id is unique
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT default 1 UNIQUE,
	name VARCHAR(256) not NULL);
