-- MySQL Advanced task 0
-- Creates a table Users
CREATE TABLE Users IF NOT EXISTS(
    PRIMARY KEY(id int NOT NULL AUTO INCREMENT ), 
    email CHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    );