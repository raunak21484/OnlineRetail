-- DROP TABLE department;
-- CREATE TABLE department(
-- dept_id INT not null,
-- dept_name varchar(20),
-- PRIMARY KEY(dept_id)
-- );
CREATE TABLE administrator(
admin_ID INT NOT NULL auto_increment UNIQUE,
admin_name varchar(25),
admin_password varchar(50),
PRIMARY KEY(admin_ID)
);

CREATE TABLE distributors(
distributor_ID INT NOT NULL auto_increment UNIQUE,
location varchar(100),
email varchar(50),
PRIMARY KEY(distributor_ID)
);
CREATE TABLE `onlineretail`.`products` (
  product_id INT NOT NULL AUTO_INCREMENT UNIQUE,
  product_name VARCHAR(45) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  distributor_ID INT NOT NULL,
  PRIMARY KEY (`product_id`),
  FOREIGN KEY(distributor_ID) references distributors(distributor_ID)
  );
CREATE TABLE cart(
Product_ID INT NOT NULL,
Amount INT NOT NULL,
FOREIGN KEY(Product_ID) references products(product_id)
);
CREATE TABLE inventory(
Product_ID INT NOT NULL,
Quantity INT NOT NULL,
FOREIGN KEY(Product_ID) references products(product_id)
);
CREATE TABLE customer(
Customer_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
Customer_Email varchar(60) NOT NULL UNIQUE,
Customer_name varchar(25) NOT NULL,
Customer_Contact varchar(15) NOT NULL,
Customer_Address varchar(100),
PRIMARY KEY(Customer_ID)
);
CREATE TABLE Orders(
Order_ID INT NOT NULL AUTO_INCREMENT UNIQUE,
Amount INT NOT NULL,
Customer_ID INT NOT NULL,
Order_Date DATE,
Delivery_Date DATE,
PRIMARY KEY(Order_ID),
FOREIGN KEY(Customer_ID) references customer(Customer_ID)
);

CREATE TABLE Tracking(
Tracking_Number INT NOT NULL UNIQUE,
Status enum('Placed','Accepted','Rejected','Shipping','Dispached','Delivered'),
Order_ID INT NOT NULL,
PRIMARY KEY(Tracking_Number),
FOREIGN KEY(Order_ID) references Orders(Order_ID)
);
CREATE TABLE Payment(
Payment_ID INT NOT NULL UNIQUE,
Status enum('Accepted','Rejected'),
Order_ID INT NOT NULL,
Payment_Date DATE NOT NULL,
Payment_Method enum('Card','UPI','Cash','Net Banking'),
PRIMARY KEY(Payment_ID),
FOREIGN KEY(Order_ID) references Orders(Order_ID)
);
Drop table Payment;
CREATE TABLE Agents(
Agent_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
Contact_Number varchar(15) NOT NULL,
Order_ID INT NOT NULL,
PRIMARY KEY(Agent_ID),
FOREIGN KEY(Order_ID) references Orders(Order_ID)
);