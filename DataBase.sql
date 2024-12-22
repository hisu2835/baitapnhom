GO
USE MilkStore;
GO

CREATE TABLE Customer
(
    CustomerID int PRIMARY KEY NOT NULL,
    FirstName char(255),
    LastName char(255),
    Address char(255),
    Email char(255),
    Phone int,
);

CREATE TABLE Product
(
    ProductID int PRIMARY KEY NOT NULL,
    ProductName char(255),
    StockQuantity int,
    Price int,
    Decription char(255),
);

CREATE TABLE Supplier
(
    SupplierID int PRIMARY KEY NOT NULL,
    SupplierName char(255),
    ProductID int FOREIGN KEY REFERENCES Product(ProductID),
    Address char(255),
    Phone int,
);

CREATE TABLE ORDERs
(
    OrderID int PRIMARY KEY NOT NULL,
    CustomerID int FOREIGN KEY REFERENCES Customer(CustomerID),
    TotalAmount int,
    TotalPrice int,
)

CREATE TABLE PersonalORDERs
(
    CustomerID int FOREIGN KEY REFERENCES Customer(CustomerID),
    ProductID int FOREIGN KEY REFERENCES Product(ProductID),
    Amount int,
    OrderDate DATE,
)