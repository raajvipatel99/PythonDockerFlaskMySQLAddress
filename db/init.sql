CREATE DATABASE addressData;
USE addressData;

CREATE TABLE IF NOT EXISTS addresses (
	`id` int AUTO_INCREMENT,
    `fname` VARCHAR(21) CHARACTER SET utf8,
    `lname` VARCHAR(20) CHARACTER SET utf8,
    `address` VARCHAR(32) CHARACTER SET utf8,
    `city` VARCHAR(20) CHARACTER SET utf8,
    `state` VARCHAR(20) CHARACTER SET utf8,
    `zipcode` INT,
    primary key(`id`)
);
INSERT INTO addresses (fname, lname, address, city, state, zipcode) VALUES
    ('John','Doe','120 jefferson st.','Riverside',' NJ',8075),
    ('Jack','McGinnis','220 hobo Av.','Phila',' PA',9119),
    ('John "Da Man"','Repici','120 Jefferson St.','Riverside',' NJ',8075),
    ('Stephen','Tyler','7452 Terrace "At the Plaza" road','SomeTown','SD',91234),
    (NULL,'Blankman',NULL,'SomeTown',' SD',298),
    ('Joan "the bone", Anne','Jet','9th, at Terrace plc','Desert City','CO',123);