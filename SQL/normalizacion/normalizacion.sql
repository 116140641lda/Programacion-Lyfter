





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
    DeliveryAddress TEXT NOT NULL,
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
    PRIMARY KEY (OrderID, ItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

INSERT INTO Customers VALUES
(1, 'Alice', '123-456-7890'),
(2, 'Bob', '987-654-3210'),
(3, 'Claire', '555-123-4567');


INSERT INTO Orders VALUES
('001', 1, '123 Main St', '6:00 PM'),
('002', 2, '456 Elm St', '7:30 PM'),
('003', 3, '789 Oak St', '12:00 PM'),
('004', 3, '464 Georgia St', '5:00 PM');

INSERT INTO Items VALUES
(101, 'Cheeseburger', 8.00),
(102, 'Fries', 3.00),
(103, 'Pizza', 12.00),
(105, 'Salad', 6.00),
(106, 'Water', 1.00);


INSERT INTO OrderDetails VALUES
('001', 101, 2, 'No onions'),
('001', 102, 1, 'Extra ketchup'),
('002', 103, 1, 'Extra cheese'),
('002', 102, 2, 'None'),
('003', 105, 1, 'No croutons'),
('004', 106, 1, 'None');






DROP TABLE IF EXISTS VehicleOwnershipInsurance;
DROP TABLE IF EXISTS InsurancePolicies;
DROP TABLE IF EXISTS InsuranceCompanies;
DROP TABLE IF EXISTS Owners;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS VehicleModels;


CREATE TABLE VehicleModels (
    ModelID INTEGER PRIMARY KEY,
    Make TEXT NOT NULL,
    Model TEXT NOT NULL,
    Year INTEGER NOT NULL,
    UNIQUE (Make, Model, Year)
);

CREATE TABLE Vehicles (
    VIN TEXT PRIMARY KEY,
    ModelID INTEGER NOT NULL,
    Color TEXT NOT NULL,
    FOREIGN KEY (ModelID) REFERENCES VehicleModels(ModelID)
);

CREATE TABLE Owners (
    OwnerID INTEGER PRIMARY KEY,
    OwnerName TEXT NOT NULL,
    OwnerPhone TEXT NOT NULL
);

CREATE TABLE InsuranceCompanies (
    CompanyID INTEGER PRIMARY KEY,
    CompanyName TEXT NOT NULL UNIQUE
);


CREATE TABLE InsurancePolicies (
    PolicyID INTEGER PRIMARY KEY,
    CompanyID INTEGER NOT NULL,
    PolicyName TEXT,
    UNIQUE (CompanyID, PolicyName),
    FOREIGN KEY (CompanyID)
        REFERENCES InsuranceCompanies(CompanyID)
);


CREATE TABLE VehicleOwnershipInsurance (
    VIN TEXT NOT NULL,
    OwnerID INTEGER NOT NULL,
    PolicyID INTEGER NOT NULL,
    PRIMARY KEY (VIN, OwnerID),
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID)
);


INSERT INTO VehicleModels VALUES
(1, 'Honda', 'Accord', 2003),
(2, 'Honda', 'CR-V', 2014),
(3, 'Chevrolet', 'Volt', 2015);

INSERT INTO Vehicles VALUES
('1HGCM82633A', 1, 'Silver'),
('5J6RM4H79EL', 2, 'Blue'),
('1G1RA6EH1FU', 3, 'Red');

INSERT INTO Owners VALUES
(101, 'Alice', '123-456-7890'),
(102, 'Bob', '987-654-3210'),
(103, 'Claire', '555-123-4567'),
(104, 'Dave', '111-222-3333');

INSERT INTO InsuranceCompanies VALUES
(1, 'ABC Insurance'),
(2, 'XYZ Insurance'),
(3, 'DEF Insurance'),
(4, 'GHI Insurance');


INSERT INTO InsurancePolicies VALUES
(1, 1, 'Fire & Theft'),
(2, 2, 'Full Cover'),
(3, 3, 'Collision'),
(4, 4, NULL);

INSERT INTO VehicleOwnershipInsurance VALUES
('1HGCM82633A', 101, 1),
('1HGCM82633A', 102, 2),
('5J6RM4H79EL', 103, 3),
('1G1RA6EH1FU', 104, 4);


SELECT
    o.OrderID,
    c.CustomerName,
    c.CustomerPhone,
    o.DeliveryAddress,
    i.ItemName,
    i.Price,
    od.Quantity,
    od.SpecialRequest,
    o.DeliveryTime
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Items i ON od.ItemID = i.ItemID
ORDER BY o.OrderID, i.ItemID;

SELECT
    v.VIN,
    vm.Make,
    vm.Model,
    vm.Year,
    v.Color,
    ow.OwnerID,
    ow.OwnerName,
    ow.OwnerPhone,
    ic.CompanyName AS InsuranceCompany,
    ip.PolicyName AS InsurancePolicy
FROM Vehicles v
JOIN VehicleModels vm ON v.ModelID = vm.ModelID
JOIN VehicleOwnershipInsurance voi ON v.VIN = voi.VIN
JOIN Owners ow ON voi.OwnerID = ow.OwnerID
JOIN InsurancePolicies ip ON voi.PolicyID = ip.PolicyID
JOIN InsuranceCompanies ic ON ip.CompanyID = ic.CompanyID
ORDER BY v.VIN, ow.OwnerID;

PRAGMA foreign_key_check;