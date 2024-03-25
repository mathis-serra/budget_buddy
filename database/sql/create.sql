-- Active: 1711370116390@@127.0.0.1@3306@maze_bank
CREATE DATABASE maze_bank;

USE maze_bank;

CREATE TABLE user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (255),
    firstname VARCHAR (255),
    email VARCHAR (255) UNIQUE CHECK (REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')),
    password VARCHAR (200)
);

CREATE TABLE transaction(
    id INT PRIMARY KEY AUTO_INCREMENT,
    amount INT,
    heure DATETIME DEFAULT CURRENT_TIMESTAMP,
    motif VARCHAR (255) 
);


-- CREATE TABLE Utilisateur (
--     id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
--     nom VARCHAR(255),
--     adresse VARCHAR(255),
--     email VARCHAR(255),
--     username VARCHAR(255),
--     password VARCHAR(255),
--     solde DECIMAL(10, 2)
-- );


-- CREATE TABLE Transaction (
--     id_transaction INT PRIMARY KEY AUTO_INCREMENT,
--     montant DECIMAL(10, 2),
--     date_heure DATETIME,
--     type_transaction VARCHAR(50),
--     compte_id INT,
--     FOREIGN KEY (compte_id) REFERENCES CompteBancaire(id_compte)
-- );