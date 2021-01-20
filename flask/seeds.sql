DROP TABLE IF EXISTS trainers;

CREATE TABLE trainers (
    id serial PRIMARY KEY,
    brand VARCHAR NOT NULL,
    country VARCHAR
);

INSERT INTO trainers
    (brand, country)
VALUES
    ('Nike', 'USA'),
    ('Adidas', 'Germany'),
    ('Mizuno', 'Japan');

