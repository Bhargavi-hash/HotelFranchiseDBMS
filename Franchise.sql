-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: Franchise
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-----------------------------------------------------------
-----------------------------------------------------------
-- Creating Database: Franchise
-----------------------------------------------------------
DROP DATABASE IF EXISTS Franchise;
CREATE DATABASE Franchise;
USE Franchise;

-- Creating Table structure for table "Hotel"
DROP TABLE IF EXISTS Hotel;
CREATE TABLE Hotel(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_No INT NOT NULL,
    Colony_Name VARCHAR(40) NOT NULL,
    Door_No INT NOT NULL,
    PRIMARY KEY (Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Hotel"
INSERT INTO Hotel VALUES
(1, 400065, 23, 'Privet Drive', 102),
(2, 400015, 9, 'KingsCross', 73),
(3, 400104, 17, 'Grimauld', 12),
(4, 400128, 12, 'Hogsmead', 3);

-- Creating Table structure for table "Furniture"
DROP TABLE IF EXISTS Furniture;
CREATE TABLE Furniture(
    Furniture_Name VARCHAR(40),
    Quantity INT,
    Branch_ID INT,
    -- PRIMARY KEY(Furniture_Name),
    CONSTRAINT Furniture_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    -- FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    -- ON UPDATE CASCADE
    -- ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Furniture"
INSERT INTO Furniture VALUES
('Table', 10, 1), ('Chair', 47, 1), ('Cushion', 12, 1), ('Desk', 2, 1),
('Table', 6, 2), ('Chair', 30, 2), ('Desk', 2, 2), ('Stool', 3, 2),
('Table', 50, 3), ('Chair', 270, 3), ('Cushion', 316, 3), ('Desk', 7, 3), ('Stool', 15, 3),
('Table', 12, 4), ('Chair', 58, 4), ('Stool', 16, 4), ('Desk', 2, 4);

-- Creating Table structure for table "Staff"
DROP TABLE IF EXISTS Staff;
CREATE TABLE IF NOT EXISTS Staff(
    Staff_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    First_Name VARCHAR(40) NOT NULL,
    Last_Name VARCHAR(40),
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Salary INT NOT NULL,
    Shift VARCHAR(40) NOT NULL,
    Department_Name VARCHAR(40) NOT NULL,
    PRIMARY KEY(Staff_ID),
    CONSTRAINT Staff_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Staff" -- (First Hotel)
INSERT INTO Staff VALUES
(1, 1, 'Minerva', 'McGonagall', 12, 10, 1981, 10000, 'Morning', 'Chef'),
(2, 1, 'Albus', 'Dumbeldore', 9, 11, 1966, 27000, 'Afternoon', 'Manager'),
(3, 1, 'Arthur', 'Weasley', 30, 5, 1991, 2500, 'Morning', 'Security'),
(4, 1, 'Severus', 'Snape', 17, 9, 1985, 20000, 'Night', 'Manager'),
(5, 1, 'Rebues', 'Hagrid', 28, 3, 1971, 12000, 'Afternoon', 'Chef'),
(6, 1, 'Luna', 'Lovegood', 15, 7, 1989, 2300, 'Morning', 'Cleaner'),
(7, 1, 'Dean', 'Thomas', 14, 5, 1969, 15000, 'Morning', 'Chef'),
(8, 1, 'Abeforth', 'Dumbeldore', 10, 10, 1970, 19000, 'Morning', 'Manager'),
(9, 1, 'Pansy', 'Parkinson', 21, 7, 1999, 9500, 'Night', 'Chef'),
(10, 1, 'Morvolo', 'Gaunt', 22, 6, 1987, 2140, 'Night', 'Cleaner'),
(11, 1, 'Draco', 'Malfoy', 5, 12, 1986, 1100, 'Afternoon', 'Security'),
(12, 1, 'Ted', 'Tonks', 4, 6, 1994, 1250, 'Afternoon', 'Cleaner'),
(13, 1, 'Bellatrix', 'Lestrange', 30, 7, 1982, 1210, 'Night', 'Cleaner'),
(14, 1, 'Regulus', 'Black', 21, 8, 1999, 11900, 'Night', 'Chef'),
(15, 1, 'Fluer', 'Delacaur', 15, 12, 1996, 14300, 'Afternoon', 'Chef');

-- Inserting values into table "Staff" -- (Second Hotel)
INSERT INTO Staff VALUES
(16, 2, 'Araina', 'Dumbeldore', 2, 10, 1991, 11300, 'Morning', 'Chef'),
(17, 2, 'Molly', 'Weasley', 19, 11, 1986, 18000, 'Afternoon', 'Manager'),
(18, 2, 'Reamus', 'Lupin', 20, 5, 1987, 2100, 'Morning', 'Security'),
(19, 2, 'Peter', 'Petigrew', 27, 9, 1987, 16000, 'Night', 'Manager'),
(20, 2, 'Petunia', 'Dursley', 18, 3, 1971, 11500, 'Afternoon', 'Chef'),
(21, 2, 'Kingsley', 'Shakelbolt', 15, 9, 1989, 2120, 'Morning', 'Cleaner'),
(22, 2, 'Belladora', 'Took', 24, 11, 1979, 12300, 'Morning', 'Chef'),
(23, 2, 'Bilbo', 'Baggins', 10, 12, 1984, 18300, 'Morning', 'Manager'),
(24, 2, 'Amos', 'Diggory', 23, 9, 1989, 9150, 'Night', 'Chef'),
(25, 2, 'Alecto', 'Carrowl', 22, 2, 1987, 2040, 'Night', 'Cleaner'),
(26, 2, 'Lucius', 'Malfoy', 15, 2, 1989, 1500, 'Afternoon', 'Security'),
(27, 2, 'Crabbe', 'Goyle', 14, 7, 1991, 1150, 'Afternoon', 'Cleaner'),
(29, 2, 'Astoria', 'Malfoy', 21, 8, 1999, 11400, 'Night', 'Chef'),
(30, 2, 'Grabille', 'Delacaur', 5, 12, 1998, 13700, 'Afternoon', 'Chef');

-- Inserting values into table "Staff" -- (Third Hotel)
INSERT INTO Staff VALUES
(31, 3, 'Ginny', 'Weasley', 12, 10, 1998, 13300, 'Morning', 'Chef'),
(32, 3, 'Lily', 'Potter', 9, 7, 1987, 17950, 'Afternoon', 'Manager'),
(33, 3, 'Amycus', 'Carrowl', 23, 7, 1982, 1930, 'Morning', 'Security'),
(34, 3, 'Fred', 'Weasley', 17, 3, 1997, 13175, 'Night', 'Manager'),
(35, 3, 'George', 'Weasley', 17, 3, 1997, 10500, 'Afternoon', 'Chef'),
(36, 3, 'Nymphadora', 'Tonks', 5, 9, 1981, 2100, 'Morning', 'Cleaner'),
(37, 3, 'Ted', 'Lupin', 14, 1, 1989, 12140, 'Morning', 'Chef'),
(38, 3, 'Rosmerta', 'Bartin', 20, 2, 1974, 17325, 'Morning', 'Manager'),
(39, 3, 'Cornelus', 'Fudge', 13, 8, 1982, 9025, 'Night', 'Chef'),
(40, 3, 'Percy', 'Weasley', 21, 7, 1989, 2015, 'Night', 'Cleaner'),
(41, 3, 'Dudley', 'Dursley', 18, 12, 1999, 1370, 'Afternoon', 'Security'),
(42, 3, 'Parvati', 'Patil', 29, 7, 1981, 1077, 'Afternoon', 'Cleaner'),
(43, 3, 'Cho', 'Chang', 22, 4, 1987, 1020, 'Night', 'Cleaner'),
(44, 3, 'John', 'McLaggen', 11, 1, 1989, 10400, 'Night', 'Chef');

-- Inserting Values into table "Staff" -- (Fourth hotel)
INSERT INTO Staff VALUES
(45, 4, 'Bathilda', 'Bagshot', 15, 4, 1988, 12700, 'Afternoon', 'Chef'),
(28, 4, 'Delphi', 'Diggory', 30, 7, 1982, 1010, 'Night', 'Cleaner'),
(46, 4, 'Bill', 'Weasley', 13, 6, 1987, 945, 'Night', 'Security'),
(47, 4, 'Charlie', 'Weasley', 24, 11, 1989, 12075, 'Morning', 'Chef'),
(48, 4, 'Vernon', 'Dursley', 27, 1, 1981, 16400, 'Afternoon', 'Manager'),
(49, 4, 'Xeno', 'Lovegood', 18, 12, 1972, 19700, 'Morning', 'Manager'),
(50, 4, 'Tom', 'Riddle', 24, 9, 1989, 11555, 'Night', 'Chef'),
(51, 4, 'Alastor', 'Moody', 27, 1, 1983, 19950, 'Night', 'Manager');

-- Creating Table structure for Table "Owners"
DROP TABLE IF EXISTS Owners;
CREATE TABLE Owners(
    First_Name VARCHAR(40) NOT NULL,
    Last_Name VARCHAR(40),
    Monthly_Rent INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(First_Name, Last_Name),
    CONSTRAINT Owners_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Owners"

INSERT INTO Owners VALUES
('Godric', 'Gryffindor', 40000, 1),
('Salazar', 'Slytherin', 70000, 2),
('Rowena', 'Ravenclaw', 95000, 3),
('Helga', 'Hufflepuff', 60700, 4);

-- Creating a Table structure for Table "Department"
DROP TABLE IF EXISTS Department;
CREATE TABLE Department(
    Department_Name VARCHAR(40) NOT NULL,
    Num_Workers INT NOT NULL,
    PRIMARY KEY(Department_Name)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Department"
INSERT INTO Department VALUES
('Manager', 12),
('Chef', 20),
('Cleaner', 12),
('Security', 7);

-- Creating a Table structure for Table "Menu"
DROP TABLE IF EXISTS Menu;
CREATE TABLE Menu(
    Food_Type VARCHAR(40),
    Food_Item_ID INT,
    Item_Cost INT,
    Food_Item VARCHAR(70),
    PRIMARY KEY(Food_Item_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Menu" --(Veg Starters)

INSERT INTO Menu VALUES
('Veg Starters', 1, 30, 'Achari Paneer Tikka'),
('Veg Starters', 2, 27, 'Hariyali Mushroom'),
('Veg Starters', 3, 21, 'Beetroot Kebab'),
('Veg Starters', 4, 29, 'American Cheese Potato'),
('Veg Starters', 5, 25, 'Crispy corn'),
('Veg Starters', 6, 27, 'Oriental grill veg'),
('Veg Starters', 7, 27, 'Churasco Pineapple');

-- Inserting values into table "Menu" --(Non-veg Starters)
INSERT INTO Menu VALUES
('Non-veg Starters', 8, 39, 'Kalmi Chicken Tikka'),
('Non-veg Starters', 9, 41, 'Angara Tangadi'),
('Non-veg Starters', 10, 37, 'Mutton Pudina Seekh'),
('Non-veg Starters', 11, 36, 'Bhuna wings'),
('Non-veg Starters', 12, 42, 'Coastal BBQ Fish'),
('Non-veg Starters', 13, 37, 'Chilly Garlic Prawns');

-- Inserting values into table "Menu" --(Soup)
INSERT INTO Menu VALUES
('Soup', 14, 22, 'Veg manchow Soup'),
('Soup', 15, 41, 'Lemon coriander chicken soup');

-- Inserting into table "Menu" --(table Dips)
INSERT INTO Menu VALUES
('Table Dips', 16, 10, 'Mint Chutney'),
('Table Dips', 17, 12, 'Garlic Mayo'),
('Table Dips', 18, 12, 'Mango Mint'),
('Table Dips', 19, 11, 'Tomato Salsa');

-- Inserting into table "Menu" --(Salads)
INSERT INTO Menu VALUES
('Salads', 20, 49, 'Mixed Sprout Salad'),
('Salads', 21, 48, 'German Potato Salad'),
('Salads', 22, 51, 'Carrot Raisin Salad'),
('Salads', 23, 41, 'Tossed Veg Salad'),
('Salads', 24, 54, 'Green Salad'),
('Salads', 25, 50, 'Dahi Salad'),
('Salads', 26, 57, 'Pickle Home Made'),
('Salads', 27, 54, 'Fried Fryum and Baked Papad'),
('Salads', 28, 59, 'Curd'),
('Salads', 29, 41, 'Curd Rice');

-- Inserting values into table "Menu" --(Sauce, Pasta, Eggs, Lassi)
INSERT INTO Menu VALUES
('Sauce', 30, 24, 'AB Dancing Sauce'),
('Sauce', 31, 31, 'Asian Black Pepper Sauce'),
('Sauce', 32, 28, 'Pesto Sauce'),
('Sauce', 33, 36, 'Moroccan Sauce'),
('Sauce', 34, 40, 'Black Bean Sauce'),
('Sauce', 35, 48, 'Toofani Indian Curry Sauce'),
('Pasta Counter', 36, 41, 'Red Sauce and Cheesee Sauce'),
('Egg Counter', 37, 47, 'Fried Masala Egg'),
('Lassi Counter', 38, 52, 'Punjabi Lassi'),
('Lassi Counter', 39, 66, 'Dil Bahar Lassi'),
('Lassi Counter', 40, 57, 'Chaas');

-- Inserting into table "Menu" --(Desserts)
INSERT INTO Menu VALUES
('Dessets', 41, 100, 'Shahi Phirni'),
('Dessets', 42, 124, 'Angoori Gulab Jamun'),
('Dessets', 43, 139, 'Moong Dal Halwa'),
('Dessets', 44, 129, 'AB celebration Chocolate Pastry'),
('Dessets', 45, 101, 'Chocolate Walnut Brownie'),
('Dessets', 46, 147, 'Pineapple Upside Down'),
('Dessets', 47, 124, 'Jalebi with Rabdi'),
('Dessets', 48, 135, 'Assorted Ice Cream'),
('Dessets', 49, 111, 'Cut Fruits'),
('Dessets', 50, 97, 'Indrani');

-- Inserting into table "Menu" --(Non-veg main course)
INSERT INTO Menu VALUES
('Non-veg Main Course', 51, 99, 'Mutton Rogan Josh'),
('Non-veg Main Course', 52, 119, 'Allepy Fish Curry'),
('Non-veg Main Course', 53, 87, 'Dum Ka Murg'),
('Non-veg Main Course', 54, 84, 'Szechuan Chicken Fried Rice'),
('Non-veg Main Course', 55, 105, 'Egg Lababdar'),
('Non-veg Main Course', 56, 121, 'Hyderabadi Chicken Dum Biryani'),
('Non-veg Main Course', 57, 99, 'Roti'),
('Non-veg Main Course', 58, 88, 'Naan');

-- Inserting into table "Menu" --(Veg Main course)
INSERT INTO Menu VALUES
('Veg Main Course', 59, 76, 'Kadhai Paneer'),
('Veg Main Course', 60, 89, 'Kachhe Kele Ka Kofta'),
('Veg Main Course', 61, 74, 'Bhindi Dopyaza'),
('Veg Main Course', 62, 109, 'Mushroom babycorn Takatak'),
('Veg Main Course', 63, 80, 'Pindi Chole'),
('Veg Main Course', 64, 121, 'Paneer Butter Masala'),
('Veg Main Course', 65, 88, 'Steamed Basmati Rice'),
('Veg Main Course', 66, 69, 'Hyderbadi Veg Dum Viryani'),
('Veg Main Course', 67, 105, 'Butter Garlic Noodles'),
('Veg Main Course', 68, 100, 'Lahsooni Dal Tadka'),
('Veg Main Course', 69, 62, 'AB Special Dal');

-- Inserting values into table "menu" --(Chaat)
INSERT INTO Menu VALUES
('Chaat', 70, 74, 'Ragda Pattice'),
('Chaat', 71, 84, 'Pani Pauri'),
('Chaat', 72, 64, 'Dahi Puri'),
('Chaat', 73, 62, 'Bhel Puri');

-- Creating a Table structure for table "Customer"
DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer(
    Customer_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    First_Name VARCHAR(40),
    Last_Name VARCHAR(40),
    Table_ID INT,
    PRIMARY KEY(Customer_ID),
    CONSTRAINT Customer_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Customer"
INSERT INTO Customer VALUES
(1, 3, 'Harry', 'Potter', 7),
(2, 3, 'Ron', 'Weasley', 7),
(3, 3, 'Hermione', 'Granger', 7),
(4, 2, 'Cedric', 'Diggory', 5),
(5, 2, 'Thorin', 'Oekinshield', 4),
(6, 2, 'Victor', 'Krum', 4),
(7, 1, 'Lockhart', 'Premb', 2),
(8, 4, 'Trienwel', 'Sinistra', 4),
(9, 4, 'James', 'Potter', 3),
(10, 4, 'Sirius', 'Black', 3),
(11, 1, 'Algus', 'Filch', 2),
(12, 1, 'Norris', 'Filch', 2);

-- Creating a table structure for table "Raw_Materials"
DROP TABLE IF EXISTS Raw_Materials;
CREATE TABLE Raw_Materials(
    Branch_ID INT NOT NULL,
    Source_ID INT NOT NULL,
    Source_Name VARCHAR(60),
    PRIMARY KEY(Branch_ID, Source_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Raw_Materials"
INSERT INTO Raw_Materials VALUES
(1, 3, 'Dairy'),
(1, 2, 'Vegetable_Shop'),
(1, 1, 'Poultry'),
(2, 3, 'Dairy'),
(2, 2, 'Vegetable_Shop'),
(2, 1, 'Poultry'),
(3, 3, 'Dairy'),
(3, 2, 'Vegetable_Shop'),
(3, 1, 'Poultry'),
(4, 3, 'Dairy'),
(4, 2, 'Vegetable_Shop'),
(4, 1, 'Poultry');

-- Creating table structure for table "Poultry"
DROP TABLE IF EXISTS Poultry;
CREATE TABLE Poultry(
    Non_veg_Item VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Non_veg_Item, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for table "Vegetable_Shop"
DROP TABLE IF EXISTS Vegetable_Shop;
CREATE TABLE Vegetable_Shop(
    Vegetable_Name VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Vegetable_Name, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for table "Dairy"
DROP TABLE IF EXISTS Dairy;
CREATE TABLE Dairy(
    Dairy_Item VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Dairy_Item, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for table "Order_c"
DROP TABLE IF EXISTS _Order;
CREATE TABLE _Order(
    Quantity INT NOT NULL,
    Customer_ID INT NOT NULL,
    Food_Item_ID INT NOT NULL,
    PRIMARY KEY(Customer_ID, Food_Item_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for "Staff_Mobile_Number"
-- Multi-valued table
DROP TABLE IF EXISTS Staff_Mobile_Number;
CREATE TABLE Staff_Mobile_Number(
    Staff_ID INT NOT NULL,
    Mobile_Number INT NOT NULL,
    CONSTRAINT STN_ibfk_1 FOREIGN KEY (Staff_ID) REFERENCES Staff (Staff_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for "Owners_Mobile_Number"
-- Multi-valued table
DROP TABLE IF EXISTS Owners_Mobile_Number;
CREATE TABLE Owners_Mobile_Number(
    First_Name VARCHAR(40),
    Last_Name VARCHAR(40),
    Mobile_Number INT NOT NULL,
    Constraint OMN_ibfk_1 FOREIGN KEY (First_Name, Last_Name) 
    REFERENCES Owners (First_Name, Last_Name)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Owners_Mobile_Number"
INSERT INTO Owners_Mobile_Number VALUES
('Godric', 'Gryffindor', 9000500010),
('Godric', 'Gryffindor', 9000523410),
('Godric', 'Gryffindor', 9234500010),
('Salazar', 'Slytherin', 8000500010),
('Salazar', 'Slytherin', 8765500010),
('Salazar', 'Slytherin', 8133500010),
('Salazar', 'Slytherin', 8123500010),
('Rowena', 'Ravenclaw', 1234567890),
('Helga', 'Hufflepuff', 6000500010);

-- Creating a table structure for table "Discount"
DROP TABLE IF EXISTS Discount;
CREATE TABLE Discount(
    Food_Item_ID INT NOT NULL,
    Discount_Amount INT NOT NULL,
    Min_Cost INT NOT NULL,
    Constraint Discount_ibfk_1
    FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating a table structure for relationship "_Orders"
-- Customer - Orders - Menu(Food_Item)
--              |
--             Hotel
-- Above is a 3 degree relationship
DROP TABLE IF EXISTS _Orders;
CREATE TABLE _Orders(
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating a table structure for relationship "Offers"
-- "Hotel" offers "discount" on "order" from "Menu" to "Customer"
-- Above is a 5 degree relationship
DROP TABLE IF EXISTS Offers;
CREATE TABLE Offers(
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    Min_Cost INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID, Min_Cost)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating a table structure for "Events"
DROP TABLE IF EXISTS Events;
CREATE TABLE Events(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_Number INT NOT NULL,
    Colony_Name VARCHAR(70) NOT NULL,
    Door_No INT NOT NULL,
    PRIMARY KEY (Pin_Code, Street_Number, Colony_Name, Door_No)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Creating table structure for relationship "Caterings"
-- "Hotel" caterings for "orders" for "events".
-- Above is a 3 degree relationship.
DROP TABLE IF EXISTS Caterings;
CREATE TABLE Caterings(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_Number INT NOT NULL,
    Colony_Name VARCHAR(70) NOT NULL,
    Door_No INT NOT NULL,
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID, Pin_Code, Street_Number, Colony_Name, Door_No),
    
    CONSTRAINT Caterings_ibfk_1
    FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
    
    CONSTRAINT Caterings_ibfk_2
    FOREIGN KEY (Pin_Code, Street_Number, Colony_Name, Door_No) 
    REFERENCES Events (Pin_Code, Street_Number, Colony_Name, Door_No)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

    CONSTRAINT Caterings_ibfk_6
    FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

    CONSTRAINT Caterings_ibfk_7
    FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;



