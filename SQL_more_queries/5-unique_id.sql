-- creates unique_id same as table 4 but id is unique
CREATE TABLE IF NOT EXISTS unique_id(
	id INT default 1 UNIQUE,
	name VARCHAR(256) not NULL);
