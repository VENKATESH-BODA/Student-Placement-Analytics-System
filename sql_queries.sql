USE placement_analytics;

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