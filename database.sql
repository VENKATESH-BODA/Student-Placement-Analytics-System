CREATE DATABASE placement_analytics;
USE placement_analytics;
CREATE TABLE students (
    roll_num INT,
    student_name VARCHAR(100),
    skills VARCHAR(255),
    company VARCHAR(100),
    package_lpa FLOAT,
    cgpa FLOAT,
    branch VARCHAR(50)
);
SELECT * FROM `placement data`;
SELECT COUNT(*) AS total_students
FROM `placement data`;
SELECT AVG(cgpa) AS average_cgpa
FROM `placement data`;
SELECT MAX(package_lpa) AS highest_package
FROM `placement data`;
SELECT branch, COUNT(*) AS total_students
FROM `placement data`
GROUP BY branch;
SELECT company, COUNT(*) AS hires
FROM `placement data`
GROUP BY company
ORDER BY hires DESC;

RENAME TABLE `placement data`
TO placement_data;
ALTER TABLE placement_data
RENAME COLUMN `ï»¿roll_no` TO roll_no;

