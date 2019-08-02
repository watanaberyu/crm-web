DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
    name TEXT,
    age INTEGER
);

INSERT INTO
    customers
VALUES
    ("Bob", 15),
    ("Tom", 57),
    ("Ken", 73)
;