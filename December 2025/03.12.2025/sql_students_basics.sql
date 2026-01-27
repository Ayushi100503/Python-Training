CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students(
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100),
  age INT,
  city VARCHAR(50)
);

INSERT INTO students(first_name, last_name, email, age, city)
VALUES
('Aisha', 'Khan', 'aisha@example.com', 20, 'Mumbai'),
('Rahul', 'Sharma', 'rahul@example.com', 22, 'Delhi'),
('Virat', 'Kohli', 'virat@example.com', 21, 'London'),
('Chirag', 'Shetty', 'chirag@example.com', 28, 'Hyderabad');
select * from students;
select first_name, last_name, city FROM students;
select * from students where city = 'Delhi';
select * from students order by age desc;

update students set city = 'Bangalore' where student_id = 2;
SET SQL_SAFE_UPDATES = 0;
update students set age = 24 where email = 'rahul@example.com';

delete from students where student_id =1;
delete from students where city = 'Delhi';
SELECT * FROM students;

DROP TABLE students;
DROP DATABASE college_db;