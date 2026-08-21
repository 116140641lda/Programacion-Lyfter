

CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    registration_date TEXT NOT NULL
);



CREATE TABLE Products (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    entry_date TEXT NOT NULL,
    brand TEXT NOT NULL,
    stock_available INTEGER NOT NULL CHECK (stock_available >= 0)
);




CREATE TABLE Payment_Methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type TEXT NOT NULL,
    bank_name TEXT
);




CREATE TABLE Invoices (
    invoice_number INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    purchase_date TEXT NOT NULL,
    buyer_email TEXT NOT NULL,
    buyer_number TEXT NOT NULL,
    employee_id_number TEXT NOT NULL,
    total_amount REAL NOT NULL CHECK (total_amount >= 0),

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    FOREIGN KEY (method_id)
        REFERENCES Payment_Methods(method_id)
);




CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    comment TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_date TEXT NOT NULL,

    FOREIGN KEY (product_code)
        REFERENCES Products(code),

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
);




CREATE TABLE Invoice_Products (
    invoice_number INTEGER NOT NULL,
    product_code INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount REAL NOT NULL CHECK (total_amount >= 0),

    PRIMARY KEY (invoice_number, product_code),

    FOREIGN KEY (invoice_number)
        REFERENCES Invoices(invoice_number),

    FOREIGN KEY (product_code)
        REFERENCES Products(code)
);




INSERT INTO Users (
    full_name,
    email,
    registration_date
)
VALUES
    ('Juan Pérez', 'juan@email.com', '2026-08-01'),
    ('María López', 'maria@email.com', '2026-08-02'),
    ('Carlos Rodríguez', 'carlos@email.com', '2026-08-03');




INSERT INTO Products (
    name,
    price,
    entry_date,
    brand,
    stock_available
)
VALUES
    ('Laptop Dell Inspiron', 650000, '2026-08-01', 'Dell', 10),
    ('Mouse Logitech G203', 18000, '2026-08-02', 'Logitech', 50),
    ('Teclado Redragon K552', 35000, '2026-08-03', 'Redragon', 30),
    ('Monitor Samsung 24"', 120000, '2026-08-04', 'Samsung', 15),
    ('Disco SSD Kingston 1TB', 75000, '2026-08-05', 'Kingston', 20);




INSERT INTO Payment_Methods (
    method_type,
    bank_name
)
VALUES
    ('Tarjeta de crédito', 'BAC'),
    ('Transferencia bancaria', 'Banco Nacional'),
    ('PayPal', NULL);




INSERT INTO Invoices (
    user_id,
    method_id,
    purchase_date,
    buyer_email,
    buyer_number,
    employee_id_number,
    total_amount
)
VALUES
    (1, 1, '2026-08-05', 'juan@email.com', '88881111', '101230456', 668000),
    (2, 2, '2026-08-05', 'maria@email.com', '88882222', '205670123', 195000),
    (1, 3, '2026-08-06', 'juan@email.com', '88881111', '101230456', 53000),
    (3, 1, '2026-08-06', 'carlos@email.com', '88883333', '304560789', 120000);




INSERT INTO Reviews (
    product_code,
    user_id,
    comment,
    rating,
    review_date
)
VALUES
    (1, 1, 'Excelente computadora.', 5, '2026-08-06'),
    (2, 2, 'Muy buen mouse.', 4, '2026-08-06'),
    (4, 3, 'Imagen muy nítida.', 5, '2026-08-06');



INSERT INTO Invoice_Products (
    invoice_number,
    product_code,
    quantity,
    total_amount
)
VALUES
    (1, 1, 1, 650000),
    (1, 2, 1, 18000),
    (2, 4, 1, 120000),
    (2, 5, 1, 75000),
    (3, 2, 1, 18000),
    (3, 3, 1, 35000),
    (4, 4, 1, 120000);




SELECT *
FROM Products;



SELECT *
FROM Products
WHERE price > 50000;




SELECT *
FROM Invoice_Products
WHERE product_code = 3;




SELECT
    p.code,
    p.name,
    SUM(ip.quantity) AS total_comprado
FROM Invoice_Products AS ip
JOIN Products AS p
    ON ip.product_code = p.code
GROUP BY
    p.code,
    p.name;




SELECT *
FROM Invoices
WHERE user_id = 1;




SELECT *
FROM Invoices
ORDER BY total_amount DESC;



SELECT *
FROM Invoices
WHERE invoice_number = 1;