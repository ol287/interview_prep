-- 1. Drop the tables if they already exist (to avoid conflicts)
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

-- 2. Create the Departments table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

-- 3. Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- 4. Insert data into the Departments table
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES 
(1, 'HR'), 
(2, 'Finance'), 
(3, 'IT'), 
(4, 'Marketing'),
(5, 'Operations'); -- Extra department not linked with employees

-- 5. Insert data into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(1, 'John', 'Doe', 'HR', 50000),
(2, 'Jane', 'Smith', 'Finance', 60000),
(3, 'Mike', 'Johnson', 'IT', 75000),
(4, 'Emily', 'Davis', 'IT', 80000),
(5, 'Sarah', 'Brown', 'Marketing', 45000);

-- 6. Query: Select all data from the Employees table
SELECT * FROM Employees;

-- 7. Query: Select specific columns (FirstName, LastName, Department)
SELECT FirstName, LastName, Department FROM Employees;

-- 8. Query: Select employees with salary greater than 60,000
SELECT * FROM Employees
WHERE Salary > 60000;

-- 9. Query: Find the average salary of employees
SELECT AVG(Salary) AS AverageSalary FROM Employees;

-- 10. Query: Group by Department and count number of employees in each
SELECT Department, COUNT(*) AS NumberOfEmployees 
FROM Employees
GROUP BY Department;

-- 11. INNER JOIN: Select employees and their corresponding departments
SELECT e.FirstName, e.LastName, d.DepartmentName 
FROM Employees e
INNER JOIN Departments d ON e.Department = d.DepartmentName;

-- 12. LEFT JOIN: Select all employees and departments, even if there’s no match in Departments
SELECT e.FirstName, e.LastName, d.DepartmentName 
FROM Employees e
LEFT JOIN Departments d ON e.Department = d.DepartmentName;

-- 13. RIGHT JOIN: Select all departments and employees, even if there’s no match in Employees
SELECT e.FirstName, e.LastName, d.DepartmentName 
FROM Employees e
RIGHT JOIN Departments d ON e.Department = d.DepartmentName;

-- 14. FULL OUTER JOIN (Simulated using UNION in databases that don't support it)
-- This query returns all records from both Employees and Departments, including mismatches
SELECT e.FirstName, e.LastName, d.DepartmentName 
FROM Employees e
LEFT JOIN Departments d ON e.Department = d.DepartmentName
UNION
SELECT e.FirstName, e.LastName, d.DepartmentName 
FROM Employees e
RIGHT JOIN Departments d ON e.Department = d.DepartmentName;

-- 15. Update: Increase the salary of employee with EmployeeID = 1
UPDATE Employees
SET Salary = 55000
WHERE EmployeeID = 1;

-- 16. Delete: Remove employee with EmployeeID = 5
DELETE FROM Employees
WHERE EmployeeID = 5;

-- 17. Query: Select all data from the Employees table after the update and delete
SELECT * FROM Employees;

-- 18. Drop the Employees and Departments tables (cleanup)
DROP TABLE Employees;
DROP TABLE Departments;
