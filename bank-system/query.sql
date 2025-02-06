CREATE DATABASE bank_system;

USE bank_system;

CREATE TABLE accounts (
    account_number INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    balance DECIMAL(10,2) DEFAULT 0.00
);