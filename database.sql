CREATE TABLE CUSTOMER (
    CustomerID int,
    FirstName varchar(255),
    LastName varchar(255),
    Email varchar(255),
    dob DATE
);

CREATE TABLE ITEM (
    ItemId int,
    ItemName varchar(255),
    UnitPrice decimal(10,2),
    AmountInStock int
);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, Email, dob)
VALUES ('0', 'Nathan', 'Gorsch', 'ng026@uowmail.edu.au', '1997-11-19');