/* users table*/
CREATE TABLE users (username char(30) PRIMARY KEY,password text,privileges text);
INSERT INTO users
VALUES ('chrissmith42','lion3','admin'), ('jackliddy5','windows5','admin'), ('guest46','linux3','guest');
SELECT * FROM users;

/* AudioFiles table */
CREATE TABLE AudioFiles (name char(30) PRIMARY KEY,date DATE,size text,audioLink text);
INSERT INTO AudioFiles
VALUES ('JHS 25','1994-12-21','43.2 MB','https://archive.org/details/JHS25SideA/JHS+25-+side+A.mp3'), ('JHS 33','1997-07-17','43.4 MB','https://archive.org/details/JHS57SideA'), ('JHS 46','1997-3-03','35.5 MB','https://archive.org/details/JHS46SideA');
SELECT * FROM AudioFiles;

/* Timeline table */
CREATE TABLE Timeline (name char(30) PRIMARY KEY,numOfFiles text);
INSERT INTO Timeline
VALUES ('History of Trenton','75'), ('Jewish History','65'), ('Oral History', '66');
SELECT * FROM Timeline;

/* Has_A table */
CREATE TABLE Has_A (TimelineName char(30) PRIMARY KEY,AudioFileName text);
INSERT INTO Has_A
VALUES ('History of Trenton','JHS 49'), ('Oral History','JHS 59'), ('Jewish History','JHS 59');
SELECT * FROM Has_A;

/* Bookmark table */
CREATE TABLE Bookmark (username char(30) PRIMARY KEY,audiofileName text);
INSERT INTO Bookmark
VALUES ('chrissmith42','JHS 49'), ('jackliddy5','JHS 59'), ('guest46','JHS 33');
SELECT * FROM Bookmark;

/* Views table */
CREATE TABLE Views (username char(30) PRIMARY KEY,TimelineName text);
INSERT INTO Views
VALUES ('chrissmith42','History of Trenton'), ('jackliddy5','Jewish History'), ('guest46','Jewish History');
SELECT * FROM Views;
    
