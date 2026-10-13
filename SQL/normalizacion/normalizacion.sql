

PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Customers;


CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    CustomerPhone TEXT NOT NULL
);


CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    CustomerID INTEGER NOT NULL,
    DeliveryTime TEXT NOT NULL,
    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
);

CREATE TABLE Items (
    ItemID INTEGER PRIMARY KEY,
    ItemName TEXT NOT NULL,
    Price REAL NOT NULL CHECK (Price >= 0)
);


CREATE TABLE OrderDetails (
    OrderID TEXT NOT NULL,
    ItemID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL CHECK (Quantity > 0),
    SpecialRequest TEXT,
    DeliveryAddress TEXT NOT NULL,
    PRIMARY KEY (OrderID, ItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);


INSERT INTO Customers VALUES
(1, 'Alice', '123-456-7890'),
(2, 'Bob', '987-654-3210'),
(3, 'Claire', '555-123-4567');


INSERT INTO Orders VALUES
('001', 1, '6:00 PM'),
('002', 2, '7:30 PM'),
('003', 3, '12:00 PM'),
('004', 3, '5:00 PM');


INSERT INTO Items VALUES
(101, 'Cheeseburger', 8.00),
(102, 'Fries', 3.00),
(103, 'Pizza', 12.00),
(105, 'Salad', 6.00),
(106, 'Water', 1.00);


INSERT INTO OrderDetails VALUES
('001', 101, 2, 'No onions', '123 Main St'),
('001', 102, 1, 'Extra ketchup', '123 Main St'),
('002', 103, 1, 'Extra cheese', '456 Elm St'),
('002', 102, 2, 'None', '4th Avenue'),
('003', 105, 1, 'No croutons', '789 Oak St'),
('004', 106, 1, 'None', '464 Georgia St');






DROP TABLE IF EXISTS VehicleOwnershipInsurance;
DROP TABLE IF EXISTS Owners;
DROP TABLE IF EXISTS Vehicles;


CREATE TABLE Vehicles (
    VIN TEXT PRIMARY KEY,
    Make TEXT NOT NULL,
    Model TEXT NOT NULL,
    Year INTEGER NOT NULL,
    Color TEXT NOT NULL
);


CREATE TABLE Owners (
    OwnerID INTEGER PRIMARY KEY,
    OwnerName TEXT NOT NULL,
    OwnerPhone TEXT NOT NULL
);


CREATE TABLE VehicleOwnershipInsurance (
    VIN TEXT NOT NULL,
    OwnerID INTEGER NOT NULL,
    InsuranceCompany TEXT NOT NULL,
    InsurancePolicy TEXT,
    PRIMARY KEY (VIN, OwnerID),
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);


INSERT INTO Vehicles VALUES
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver'),
('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue'),
('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');


INSERT INTO Owners VALUES
(101, 'Alice', '123-456-7890'),
(102, 'Bob', '987-654-3210'),
(103, 'Claire', '555-123-4567'),
(104, 'Dave', '111-222-3333');


INSERT INTO VehicleOwnershipInsurance VALUES
('1HGCM82633A', 101, 'ABC Insurance', 'Fire & Theft'),
('1HGCM82633A', 102, 'XYZ Insurance', 'Full Cover'),
('5J6RM4H79EL', 103, 'DEF Insurance', 'Collision'),
('1G1RA6EH1FU', 104, 'GHI Insurance', NULL);
