# book_management_system

#command to create database

create database mydb;

# create employee table

create table employee( firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL, username VARCHAR(100) NOT NULL, contact integer(50) NOT NULL,email  VARCHAR(100) NOT NULL,age integer(30)NOT NULL,gender char(50), password VARCHAR(50) NOT NULL, PRIMARY KEY ( username ) );


#create books table

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30)); 

# create books_issued table 

create table books_issued(bid varchar(20) primary key, issueto varchar(30));
