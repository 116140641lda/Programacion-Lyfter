Last login: Thu Aug  6 10:08:46 on ttys000
fabianfallas@Fabians-MacBook-Pro ~ % sqlite3
SQLite version 3.37.0 2021-12-09 01:34:53
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> CREATE TABLE Users (
   ...>    ...>     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>    ...>     full_name TEXT NOT NULL,
   ...>    ...>     email TEXT NOT NULL UNIQUE,
   ...>    ...>     registration_date TEXT NOT NULL
   ...>    ...> );
Error: in prepare, near ".": syntax error (1)
sqlite> CREATE TABLE Users (
   ...>   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>   full_name TEXT NOT NULL,
   ...>   email TEXT NOT NULL UNIQUE,
   ...>   registration_date TEXT NOT NULL
   ...> );
sqlite> CREATE TABLE Invoices (
   ...> invoice_number INT PRIMARY KEY AUTOINCREMENT,
   ...> purchase_date TEXT NOT NULL,
   ...> buyer_email TEXT NOT NULL,
   ...> total_amount REAL NOT NULL,
   ...> used_id INT NOT NULL,
   ...> FOREIGN KEY (user_id)
   ...> REFERENCES Users(user_id)
   ...> );
Error: in prepare, AUTOINCREMENT is only allowed on an INTEGER PRIMARY KEY (1)
sqlite> CREATE TABLE Invoices (
   ...> invoice_number INT PRIMARY KEY,
   ...> purchase_date TEXT NOT NULL,
   ...> buyer_email TEXT NOT NULL,
   ...> total_amount REAL NOT NULL,
   ...> used_id INT NOT NULL,
   ...> FOREIGN KEY (user_id)
   ...> REFERENCES Users(user_id)
   ...> );
Error: in prepare, unknown column "user_id" in foreign key definition (1)
sqlite> CREATE TABLE Invoices (
   ...> user_id INT NOT NULL,
   ...> invoice_number INT PRIMARY KEY,
   ...> purchase_date TEXT NOT NULL,
   ...> buyer_email TEXT NOT NULL,
   ...> total_amount REAL NOT NULL,
   ...> FOREIGN KEY (user_id)
   ...> REFERENCES Users(user_id)
   ...> );
sqlite> CREATE TABLE Products (
   ...> CREATE TABLE Products (
   ...>     code INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     name TEXT NOT NULL,
   ...>     price REAL NOT NULL CHECK (price >= 0),
   ...>     entry_date TEXT NOT NULL,
   ...>     brand TEXT NOT NULL,
   ...>     stock_available INTEGER NOT NULL CHECK (stock_available >= 0)
   ...> );
Error: in prepare, near "CREATE": syntax error (1)
sqlite> CREATE TABLE Products (
   ...>     code INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     name TEXT NOT NULL,
   ...>     price REAL NOT NULL CHECK (price >= 0),
   ...>     entry_date TEXT NOT NULL,
   ...>     brand TEXT NOT NULL,
   ...>     stock_available INTEGER NOT NULL CHECK (stock_available >= 0)
   ...> );
sqlite> CREATE TABLE Reviews (
   ...>     review_id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     product_code INTEGER NOT NULL,
   ...>     user_id INTEGER NOT NULL,
   ...>     comment TEXT NOT NULL,
   ...>     rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
   ...>     review_date TEXT NOT NULL,
   ...> 
   ...>     FOREIGN KEY (product_code) REFERENCES Products(code),
   ...>     FOREIGN KEY (user_id) REFERENCES Users(user_id)
   ...> );
sqlite> CREATE TABLE Payment_Methods (
   ...>     method_id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     method_type TEXT NOT NULL,
   ...>     bank_name TEXT
   ...> );
sqlite> DROP TABLE Invoices
   ...> );
Error: in prepare, near ")": syntax error (1)
sqlite> .tables
Invoices         Products         Users          
Payment_Methods  Reviews        
sqlite> DROP TABLE Invoices;
sqlite> .tables
Payment_Methods  Products         Reviews          Users          
sqlite> CREATE TABLE Invoices (
   ...>    ...> user_id INT NOT NULL,
   ...>    ...> invoice_number INT PRIMARY KEY,
   ...>    ...> purchase_date TEXT NOT NULL,
   ...>    ...> buyer_email TEXT NOT NULL,
   ...>    ...> total_amount REAL NOT NULL,
   ...>    ...> FOREIGN KEY (user_id)
   ...>    ...> REFERENCES Users(user_id)
   ...>    ...> user_id INT NOT NULL,
   ...>    ...> user_id INT NOT NULL,,
   ...> );
Error: in prepare, near ".": syntax error (1)
sqlite> CREATE TABLE Invoices (
   ...>   user_id INT NOT NULL,
   ...>   invoice_number INT PRIMARY KEY,
   ...>   purchase_date TEXT NOT NULL,
   ...>   buyer_email TEXT NOT NULL,
   ...>   total_amount REAL NOT NULL,
   ...>   FOREIGN KEY (user_id) REFERENCES Users(user_id)
   ...>   FOREIGN KEY (method_id) REFERENCES Payment_Methods(method_id)
   ...> );
Error: in prepare, unknown column "method_id" in foreign key definition (1)
sqlite> CREATE TABLE Invoices (
   ...>   user_id INT NOT NULL,
   ...>   invoice_number INT PRIMARY KEY,
   ...>   purchase_date TEXT NOT NULL,
   ...>   buyer_email TEXT NOT NULL,
   ...>   total_amount REAL NOT NULL,
   ...>   method_id INT NOT NULL,
   ...>   FOREIGN KEY (user_id) REFERENCES Users(user_id)
   ...>   FOREIGN KEY (method_id) REFERENCES Payment_Methods(method_id)
   ...> );
sqlite> .tables
Invoices         Products         Users          
Payment_Methods  Reviews        
sqlite> ALTER TABLE Products
   ...> (;
Error: in prepare, near "(": syntax error (1)
sqlite> ALTER TABLE Invoices
   ...> ADD buyer_number INT NOT NULL,
   ...> ADD employee_id_number VARCHAR NOT NULL
   ...> );
Error: in prepare, near ",": syntax error (1)
sqlite> ALTER TABLE Invoices
   ...> ADD employee_id_number VARCHAR NOT NULL
   ...> );
Error: in prepare, near ")": syntax error (1)
sqlite> ALTER TABLE Invoices
   ...> ADD buyer_number INT NOT NULL;
sqlite> ALTER TABLE Invoices
   ...> ADD employee_id_number VARCHAR NOT NULL;
sqlite> SELECT *
   ...> FROM Products;
sqlite> INSERT INTO Users (full_name, email, registration_date) VALUES
   ...> ('Juan Pérez', 'juan@email.com', '2026-08-01'),
   ...> ('María López', 'maria@email.com', '2026-08-02'),
   ...> ('Carlos Rodríguez', 'carlos@email.com', '2026-08-03');
sqlite> INSERT INTO Products (name, price, entry_date, brand, stock_available) VALUES
   ...> ('Laptop Dell Inspiron', 650000, '2026-08-01', 'Dell', 10),
   ...> ('Mouse Logitech G203', 18000, '2026-08-02', 'Logitech', 50),
   ...> ('Teclado Redragon K552', 35000, '2026-08-03', 'Redragon', 30),
   ...> ('Monitor Samsung 24"', 120000, '2026-08-04', 'Samsung', 15),
   ...> ('Disco SSD Kingston 1TB', 75000, '2026-08-05', 'Kingston', 20);
sqlite> INSERT INTO Payment_Methods (method_type, bank_name) VALUES
   ...> ('Tarjeta de crédito', 'BAC'),
   ...> ('Transferencia bancaria', 'Banco Nacional'),
   ...> ('PayPal', NULL);
sqlite> INSERT INTO Invoices (user_id, method_id, purchase_date, total_amount) VALUES
   ...> (1, 1, '2026-08-05', 668000),
   ...> (2, 2, '2026-08-05', 195000),
   ...> (1, 3, '2026-08-06', 53000),
   ...> (3, 1, '2026-08-06', 120000);
Error: stepping, NOT NULL constraint failed: Invoices.buyer_email (19)
sqlite> CREATE TABLE (
   ...> invoice_number INT NOT NULL,
   ...> product_code INT NOT NULL,
   ...> quantity INT NOT NULL,
   ...> total_amount INT NOT NULL,
   ...> );
Error: in prepare, near "(": syntax error (1)
sqlite> CREATE TABLE Invoice_Products (
   ...> invoice_number INT NOT NULL,
   ...> product_code INT NOT NULL,
   ...> quantity INT NOT NULL,
   ...> total_amount INT NOT NULL,
   ...> );
Error: in prepare, near ")": syntax error (1)
sqlite> CREATE TABLE Invoice_Products (
   ...> invoice_number INT NOT NULL,
   ...> product_code INT NOT NULL,
   ...> quantity INT NOT NULL,
   ...> total_amount INT NOT NULL
   ...> );
sqlite> INSERT INTO Reviews
   ...> (product_code, user_id, comment, rating, review_date)
   ...> VALUES
   ...> (1, 1, 'Excelente computadora.', 5, '2026-08-06'),
   ...> (2, 2, 'Muy buen mouse.', 4, '2026-08-06'),
   ...> (4, 3, 'Imagen muy nítida.', 5, '2026-08-06');
sqlite> SELECT *
   ...> FROM Products;
1|Laptop Dell Inspiron|650000.0|2026-08-01|Dell|10
2|Mouse Logitech G203|18000.0|2026-08-02|Logitech|50
3|Teclado Redragon K552|35000.0|2026-08-03|Redragon|30
4|Monitor Samsung 24"|120000.0|2026-08-04|Samsung|15
5|Disco SSD Kingston 1TB|75000.0|2026-08-05|Kingston|20
sqlite> SELECT *
   ...> FROM Products
   ...> WHERE price > 5000;
1|Laptop Dell Inspiron|650000.0|2026-08-01|Dell|10
2|Mouse Logitech G203|18000.0|2026-08-02|Logitech|50
3|Teclado Redragon K552|35000.0|2026-08-03|Redragon|30
4|Monitor Samsung 24"|120000.0|2026-08-04|Samsung|15
5|Disco SSD Kingston 1TB|75000.0|2026-08-05|Kingston|20
sqlite> SELECT *
   ...> FROM Invoice_Products
   ...> WHERE product_code = 3;
sqlite> INSERT INTO Invoice_Products
   ...> (invoice_number, product_code, quantity, total_amount)
   ...> VALUES
   ...> (1, 1, 1, 650000),
   ...> (1, 2, 1, 18000),
   ...> 
   ...> (2, 4, 1, 120000),
   ...> (2, 5, 1, 75000),
   ...> 
   ...> (3, 2, 1, 18000),
   ...> (3, 3, 1, 35000),
   ...> 
   ...> (4, 4, 1, 120000);
sqlite> SELECT *
   ...> FROM Invoice_Products
   ...> WHERE product_code = 3;
3|3|1|35000
sqlite> SELECT
   ...>     p.code,
   ...>     p.name,
   ...>     SUM(ip.quantity) AS total_comprado
   ...> FROM Invoice_Products ip
   ...> JOIN Products p
   ...>     ON ip.product_code = p.code
   ...> GROUP BY p.code, p.name;
1|Laptop Dell Inspiron|1
2|Mouse Logitech G203|2
3|Teclado Redragon K552|1
4|Monitor Samsung 24"|2
5|Disco SSD Kingston 1TB|1
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE user_id = 3;
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE user_id = 1;
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE user_id =2;
sqlite> SELECT *
   ...> FROM Invoices;
sqlite> SELECT *
   ...> FROM Products
   ...> ;
1|Laptop Dell Inspiron|650000.0|2026-08-01|Dell|10
2|Mouse Logitech G203|18000.0|2026-08-02|Logitech|50
3|Teclado Redragon K552|35000.0|2026-08-03|Redragon|30
4|Monitor Samsung 24"|120000.0|2026-08-04|Samsung|15
5|Disco SSD Kingston 1TB|75000.0|2026-08-05|Kingston|20
sqlite> INSERT INTO Invoices (user_id, method_id, purchase_date, total_amount, buyer_email) VALUES
   ...>    (1, 1, '2026-08-05', 668000, aljs@gmail.com),
   ...>    (2, 3, '2026-08-05', 195000, hlsdj@gmail.com),
   ...>    1, 3, '2026-08-06', 53000, hlsjodl@gmail.com),
   ...>    (3, 1, '2026-08-06', 120000, dhas@gmail.com);
Error: in prepare, near "@gmail": syntax error (1)
sqlite> INSERT INTO Invoices (user_id, method_id, purchase_date, total_amount, buyer_email) VALUES
   ...>    (1, 1, '2026-08-05', 668000,"aljs@gmail.com"),
   ...>    (2, 3, '2026-08-05', 195000,"hlsdj@gmail.com"),                      
   ...>    (1, 3, '2026-08-06', 53000, "hlsjodl@gmail.com"),                        ...>    (3, 1, '2026-08-06', 120000," dhas@gmail.com");
Error: stepping, NOT NULL constraint failed: Invoices.buyer_number (19)
sqlite> INSERT INTO Invoices
   ...> (user_id, method_id, purchase_date, total_amount, buyer_email)
   ...> VALUES
   ...> (1, 1, '2026-08-05', 668000, 'aljs@gmail.com'),
   ...> (2, 3, '2026-08-05', 195000, 'hlsdj@gmail.com'),
   ...> (1, 3, '2026-08-06', 53000, 'hlsjodl@gmail.com'),
   ...> (3, 1, '2026-08-06', 120000, 'dhas@gmail.com');
Error: stepping, NOT NULL constraint failed: Invoices.buyer_number (19)
sqlite> INSERT INTO Invoices
   ...> (user_id, method_id, purchase_date, total_amount, buyer_email, buyer_number)
   ...> VALUES
   ...> (1, 1, '2026-08-05', 668000, 'juan@email.com', '88881111'),
   ...> (2, 3, '2026-08-05', 195000, 'maria@email.com', '88882222'),
   ...> (1, 3, '2026-08-06', 53000, 'juan@email.com', '88881111'),
   ...> (3, 1, '2026-08-06', 120000, 'carlos@email.com', '88883333');
Error: stepping, NOT NULL constraint failed: Invoices.employee_id_number (19)
sqlite> INSERT INTO Invoices
   ...> (
   ...>     user_id,
   ...>     method_id,
   ...>     purchase_date,
   ...>     total_amount,
   ...>     buyer_email,
   ...>     buyer_number,
   ...>     employee_id_number
   ...> )
   ...> VALUES
   ...> (1, 1, '2026-08-05', 668000, 'juan@email.com', '88881111', '101230456'),
   ...> (2, 3, '2026-08-05', 195000, 'maria@email.com', '88882222', '205670123'), 
   ...> (1, 3, '2026-08-06', 53000, 'juan@email.com', '88881111', '101230456'),
   ...> (3, 1, '2026-08-06', 120000, 'carlos@email.com', '88883333', '304560789');
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE user_id = 1;
1||2026-08-05|juan@email.com|668000.0|1|88881111|101230456
1||2026-08-06|juan@email.com|53000.0|3|88881111|101230456
sqlite> SELECT *
   ...> FROM Invoices
   ...> ORDER BY total_amount DESC;
1||2026-08-05|juan@email.com|668000.0|1|88881111|101230456
2||2026-08-05|maria@email.com|195000.0|3|88882222|205670123
3||2026-08-06|carlos@email.com|120000.0|1|88883333|304560789
1||2026-08-06|juan@email.com|53000.0|3|88881111|101230456
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE invoice_number = 15;
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE invoice_number = 1 ;
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE user_id = 1 ;
1||2026-08-05|juan@email.com|668000.0|1|88881111|101230456
1||2026-08-06|juan@email.com|53000.0|3|88881111|101230456
sqlite> ALTER TABLE Invoices
   ...> ADD COLUMN invoice_number INTEGER;
Error: in prepare, duplicate column name: invoice_number (1)
sqlite> WHERE invoice_number = 1 ;
Error: in prepare, near "WHERE": syntax error (1)
sqlite> SELECT *
   ...> FROM Invoices
   ...> WHERE invoice_number = 1 ;
sqlite> SELECT *
   ...> FROM Invoice_Products
   ...> WHERE invoice_number = 1 ;
1|1|1|650000
1|2|1|18000
sqlite> 