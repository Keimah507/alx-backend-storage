-- MySQL Advanced task 1
-- Creates a table Users
CREATE TABLE IF NOT EXISTS Users(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN' DEFAULT 'US')
);