-- Create and select the database 
Create Database if NOT EXISTS student_system;
USE student_system;

-- Table to store student personal data
Create Table if NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    pronouns VARCHAR(50),
    date_of_birth DATE NOT NULL,
    home_address VARCHAR(255) NOT NULL,
    term_address VARCHAR(225) NOT NULL,
    emergency_contact_name VARCHAR(100) NOT NULL,
    emergency_contact_number VARCHAR(20) NOT NULL,
    course VARCHAR(100) NOT NULL
);

-- Table to store login credentials 
CREATE TABLE IF NOT EXISTS login (
    login_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(10) NOT NULL,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Pre-populate lecturer account (password: Lecturer123)
INSERT INTO login (username, password_hash, role, student_id)
VALUES ("lecturer", SHA2("lecturer123", 256), "lecturer", NULL);

-- Pre-populate sample student Ellen
INSERT INTO students VALUES (
    1, "Ellen Smith", "she/her", "2004-03-22",
    "45 Maple Avenue, Manchester",
    "8 College Road, Basingstoke",
    "Ken Smith", "07755123468", "Cyber Security"
);

INSERT INTO login (username, password_hash, role, student_id)
VALUES ("ellen", SHA2("Ellen123", 256), "student", 1);