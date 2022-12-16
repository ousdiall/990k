
CREATE TABLE author(
author_id NUMBER PRIMARY KEY,
author_first_name VARCHAR(60) NOT NULL,
author_last_name VARCHAR(60) NOT NULL);


CREATE TABLE publisher(
publisher_id NUMBER PRIMARY KEY,
publisher_name VARCHAR(60) NOT NULL);

CREATE TABLE patron(
patron_id NUMBER PRIMARY KEY,
patron_first_name VARCHAR(60) NOT NULL,
patron_last_name VARCHAR(60) NOT NULL);

CREATE TABLE library(
library_id NUMBER PRIMARY KEY,
library_address VARCHAR(1600) NOT NULL,
library_name VARCHAR(100) NOT NULL);

CREATE TABLE book(
book_id NUMBER PRIMARY KEY,
book_title VARCHAR(1600) NOT NULL,
borrow_date DATE DEFAULT NULL,
patron_id NUMBER DEFAULT NULL,
FOREIGN KEY (patron_id) REFERENCES patron(patron_id),
library_id NUMBER NOT NULL,
FOREIGN KEY (library_id) REFERENCES library(library_id));

ALTER TABLE book
ADD num_copies NUMBER DEFAULT 0 NOT NULL;

CREATE TABLE book_genre(
book_id NUMBER, 
FOREIGN KEY (book_id) REFERENCES book(book_id),
genre VARCHAR(20));

ALTER TABLE book_genre
MODIFY (book_id NOT NULL,
        genre VARCHAR(50) NOT NULL );

CREATE TABLE written_by(
author_id NUMBER NOT NULL,
FOREIGN KEY (author_id) REFERENCES author(author_id),
book_id NUMBER NOT NULL,
FOREIGN KEY (book_id) REFERENCES book(book_id));

CREATE TABLE published_by(
book_id NUMBER NOT NULL,
FOREIGN KEY (book_id) REFERENCES book(book_id),
publisher_id NUMBER NOT NULL,
FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id));


--AUTHOR ROWS

INSERT INTO author(author_id, author_first_name, author_last_name)
VALUES (1, 'Theodor', 'Geisel');

INSERT INTO author(author_id, author_first_name, author_last_name)
VALUES (2, 'Stephen', 'King');

--PUBLISHER ROWS

INSERT INTO publisher(publisher_id, publisher_name)
VALUES (1, 'Random House');

INSERT INTO publisher(publisher_id, publisher_name)
VALUES (2, 'Doubleday');

--PATRON ROWS

INSERT INTO patron(patron_id, patron_first_name, patron_last_name)
VALUES (1, 'John', 'Doe');

INSERT INTO patron(patron_id, patron_first_name, patron_last_name)
VALUES (2, 'Jane', 'Dee');

INSERT INTO patron(patron_id, patron_first_name, patron_last_name)
VALUES (3, 'Harry', 'Johnson');

--LIBRARY ROWS

INSERT INTO library(library_id, library_address, library_name)
VALUES (1, '6304 Castor Avenue Philadelphia, PA 19149-2731', 'Bushrod Library');

INSERT INTO library(library_id, library_address, library_name)
VALUES (2, '705 East Cathedral Road Philadelphia, PA 19128-2106', 'Andorra Library');

--BOOK ROWS

DELETE FROM book_genre;
DELETE FROM book;

INSERT INTO book(book_id, book_title, borrow_date, patron_id, library_id, num_copies)
VALUES (1, 'Cat In The Hat', TO_DATE('2012-04-01','YYYY-MM-DD'), 
(SELECT patron_id FROM patron WHERE patron_id = 1), 
(SELECT library_id FROM library WHERE library_id = 1), 103);

INSERT INTO book(book_id, book_title, borrow_date, patron_id, library_id, num_copies)
VALUES (2, 'The Shining', NULL, NULL, 
(SELECT library_id FROM library WHERE library_id = 2), 227);

INSERT INTO book(book_id, book_title, borrow_date, patron_id, library_id, num_copies)
VALUES (3, 'The Lorax', TO_DATE('2012-06-18','YYYY-MM-DD'), 2, 
(SELECT library_id FROM library WHERE library_id = 2), 193);

--BOOK_GENRE ROWS

INSERT INTO book_genre(book_id, genre) VALUES
(1, 'Fiction');

INSERT INTO book_genre(book_id, genre) VALUES
(1, 'Childrens Book');

INSERT INTO book_genre(book_id, genre) VALUES
(2, 'Horror');

INSERT INTO book_genre(book_id, genre) VALUES
(2, 'Fiction');

INSERT INTO book_genre(book_id, genre) VALUES
(2, 'Supernatural');

INSERT INTO book_genre(book_id, genre) VALUES
(3, 'Fiction');

INSERT INTO book_genre(book_id, genre) VALUES
(3, 'Childrens Book');

--WRITTEN_BY ROWS

INSERT INTO written_by(author_id, book_id)
VALUES (
(SELECT author_id FROM author WHERE author_id = 1), 
(SELECT book_id FROM book WHERE book_id = 1));

INSERT INTO written_by(author_id, book_id)
VALUES (
(SELECT author_id FROM author WHERE author_id = 2), 
(SELECT book_id FROM book WHERE book_id = 2));

INSERT INTO written_by(author_id, book_id)
VALUES (
(SELECT author_id FROM author WHERE author_id = 1), 
(SELECT book_id FROM book WHERE book_id = 3));

--PUBLISHED_BY ROWS

INSERT INTO published_by(book_id, publisher_id)
VALUES (
(SELECT book_id FROM book WHERE book_id = 1), 
(SELECT publisher_id FROM publisher WHERE publisher_id = 1));

INSERT INTO published_by(book_id, publisher_id)
VALUES (
(SELECT book_id FROM book WHERE book_id = 2), 
(SELECT publisher_id FROM publisher WHERE publisher_id = 2));

--QUERIES
SELECT *
FROM book_genre
WHERE genre = 'Fiction';

SELECT *
FROM book
WHERE borrow_date IS NOT NULL;

COMMIT;


