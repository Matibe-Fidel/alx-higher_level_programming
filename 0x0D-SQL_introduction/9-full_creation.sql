-- create second_table if it doesnot already exist
CREATE TABLE IF NOT EXISTS `second_table`(`id` INT, `name` VARCHAR(256), `score` INT);
-- insert records into second_table
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
(1,'Jonh', 10),
(2,'Alex', 3),
(3,'Bob', 14),
(5,'George', 8),
