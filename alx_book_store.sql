CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

CREATE TABLE Books(book_id int AUTO_INCREMENT PRIMARY KEY , title varchar(130) not null, author_id FOREIGN KEY REFERENCES Authors(author_id), price not null, publication_date date);
CREATE TABLE Authors(author_id int AUTO_INCREMENT PRIMARY KEY, author_name varchar(215) not null);
CREATE TABLE Customers(customer_id int AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(215) not null, email VARCHAR(215) not null UNIQUE, address TEXT);
CREATE TABLE Orders(order_id INT PRIMARY KEY, order_date date, FOREIGN KEY(customer_id) REFERENCES Customers(customer_id));
CREATE TABLE Order_details(orderdetailid int primary key, FOREIGN KEY (order_id) REFERENCES Orders(order_id),FOREIGN KEY (book_id) REFERENCES Books(book_id), quantity double)
