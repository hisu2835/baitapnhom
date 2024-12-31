--Tạo database Milk_Store
CREATE DATABASE Milk_Store

--Sử dụng database vừa tạo
GO
USE Milk_Store;
GO

--Tạo bảng Khách hàng
CREATE TABLE Customer
(
    CustomerID int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    FirstName NCHAR(255),
    LastName NCHAR(255),
    Address NCHAR(255),
    Email char(255),
    Phone int,
);

--Tạo bảng Nhà cung cấp
CREATE TABLE Supplier
(
    SupplierID int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    SupplierName NCHAR(255),
    Address NCHAR(255),
    Phone int,
);

--Tạo bảng Sản phẩm
CREATE TABLE Product
(
    ProductID int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    ProductName NCHAR(255),
    StockQuantity int,
    ExpiryDate DATE,
    Price int,
    Decription NCHAR(255),
    SupplierID int FOREIGN KEY REFERENCES Supplier(SupplierID),
);

--Tạo bảng Đơn hàng
CREATE TABLE ORDERs
(
    OrderID int IDENTITY(1, 1) PRIMARY KEY NOT NULL,
    CustomerID int FOREIGN KEY REFERENCES Customer(CustomerID),
    TotalPrice int,
)

--Tạo bảng Sản phẩm đặt hàng
CREATE TABLE ProductOrder
(
    ProductID int FOREIGN KEY REFERENCES Product(ProductID),
    OrderID int FOREIGN KEY REFERENCES ORDERs(OrderID),
    Amount int,
    OrderDate DATETIME,
)