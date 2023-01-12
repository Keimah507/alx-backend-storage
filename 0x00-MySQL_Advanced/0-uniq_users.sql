-- MySQL Advanced task 0
-- Creates a table Users
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    );