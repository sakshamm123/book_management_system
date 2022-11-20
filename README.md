# book_management_system


# requirements

pillow

pip install pillow

pymsql

pip install pymysql

# command to create database

create database mydb;

# create employee table

create table employee( firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL, username VARCHAR(100) NOT NULL, contact integer(50) NOT NULL,email  VARCHAR(100) NOT NULL,age integer(30)NOT NULL,gender char(50), password VARCHAR(50) NOT NULL, PRIMARY KEY ( username ) );


# create books table

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30)); 

# create isssued_books table 

create table issued_books(bid varchar(20) primary key, issueto varchar(30), email varchar(255), contact_no integer(255));
