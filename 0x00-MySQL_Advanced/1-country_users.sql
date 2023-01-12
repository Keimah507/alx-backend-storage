-- MySQL Advanced task 1
-- Creates a table Users
CREATE TABLE IF NOT EXISTS Users(
    PRIMARY KEY(id int NOT NULL AUTO INCREMENT),
    email CHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN' DEFAULT 'US'),
)