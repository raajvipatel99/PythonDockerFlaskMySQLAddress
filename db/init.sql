CREATE DATABASE addressData;
USE addressData;

CREATE TABLE IF NOT EXISTS addresses (
    `id` int AUTO_INCREMENT primary key ,
    `fname` VARCHAR(21) CHARACTER SET utf8,
    `lname` VARCHAR(8) CHARACTER SET utf8,
    `address` VARCHAR(32) CHARACTER SET utf8,
    `city` VARCHAR(11) CHARACTER SET utf8,
    `state` VARCHAR(3) CHARACTER SET utf8,
    `zipcode` INT
);
INSERT INTO addresses VALUES
    ('Jack','McGinnis','220 hobo Av.','Phila',' PA',09119),
    ('John "Da Man"','Repici','120 Jefferson St.','Riverside',' NJ',08075),
    ('Stephen','Tyler','7452 Terrace "At the Plaza" road','SomeTown','SD', 91234),
    (NULL,'Blankman',NULL,'SomeTown',' SD', 00298),
    ('Joan "the bone", Anne','Jet','9th, at Terrace plc','Desert City','CO',00123);
