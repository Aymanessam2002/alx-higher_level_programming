-- Creating another table in the database
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- Inserting John into the newly created table
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (1, "John", 10);
-- Inserting Alex into a newly created table
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (2, "Alex", 3);
-- Inserting Bob into a newly created table
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (3, "Bob", 14);
-- Inserting George into a newly created table
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (4, "George", 8);
