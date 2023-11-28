CREATE DATABASE PDMS;

USE PDMS

 CREATE TABLE `patient` (
  `p_id` varchar(5) NOT NULL,
  `p_name` varchar(30) NOT NULL,
  `age` int NOT NULL,
  `house_no` varchar(5) NOT NULL,
  `street_name` varchar(25) DEFAULT NULL,
  `city` varchar(15) NOT NULL DEFAULT 'Bengaluru',
  `Postal_code` int NOT NULL,
  `gender` enum('M','F','O') NOT NULL,
  PRIMARY KEY (`p_id`)
);


 CREATE TABLE `doctor` (
  `d_id` varchar(7) NOT NULL,
  `d_name` varchar(30) NOT NULL,
  `specification` varchar(40) DEFAULT NULL,
  `h_name` varchar(30) NOT NULL,
  `h_id` varchar(7) NOT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`d_id`),
  CONSTRAINT `doctor_chk_1` CHECK ((char_length(`contact_no`) = 10))
);


 CREATE TABLE `prescription` (
  `p_id` varchar(5) NOT NULL,
  `drug_name` varchar(25) NOT NULL,
  `dosage` varchar(6) NOT NULL,
  `add_comment` varchar(100) DEFAULT 'General Prescribed',
  `pres_date` date DEFAULT (curdate()),
  `pres_time` time DEFAULT (curtime()),
  `d_id` varchar(10) DEFAULT 'N/A'
);


CREATE TABLE `pharmacist` (
  `ph_id` varchar(6) NOT NULL,
  `ph_name` varchar(20) NOT NULL,
  `age` int NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `gender` enum('M','F','O') NOT NULL,
  PRIMARY KEY (`ph_id`)
);


CREATE TABLE `medicine` (
  `m_id` varchar(7) NOT NULL,
  `drug_name` varchar(30) NOT NULL,
  `company_name` varchar(45) DEFAULT NULL,
  `price` decimal(8,2) NOT NULL,
  `exp_date` date NOT NULL,
  `composition` varchar(100) DEFAULT NULL,
  `dd_id` varchar(7) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`m_id`),
  KEY `dd_id` (`dd_id`),
  KEY `FK_drug_name` (`drug_name`),
  CONSTRAINT `FK_drug_name` FOREIGN KEY (`drug_name`) REFERENCES `drug_dealer` (`drug_name`)
);


CREATE TABLE `drug_dealer` (
  `dd_id` varchar(7) NOT NULL,
  `drug_name` varchar(30) NOT NULL,
  `dd_company_name` varchar(40) DEFAULT NULL,
  `quantity` varchar(15) NOT NULL,
  `price_of_each_med` decimal(8,2) NOT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`dd_id`,`drug_name`),
  KEY `idx_drug_name` (`drug_name`),
  CONSTRAINT `drug_dealer_chk_1` CHECK ((char_length(`contact_no`) = 10))
);


CREATE TABLE `med_order_p` (
  `order_no` varchar(6) DEFAULT NULL,
  `Item_No` int NOT NULL,
  `Med_Name` varchar(30) NOT NULL,
  `Dosage` int NOT NULL,
  `Cost` decimal(8,2) NOT NULL DEFAULT '0.00',
  `Patient_ID` varchar(20) NOT NULL,
  `Doctor_Name` varchar(20) NOT NULL,
  `Pharmacist_Name` varchar(20) NOT NULL,
  `order_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `deleted_expired_medicines` (
  `m_id` varchar(7) DEFAULT NULL,
  `drug_name` varchar(30) DEFAULT NULL,
  `exp_date` date DEFAULT NULL
);

-- Inserting data into the patient table
INSERT INTO patient VALUES
('p_1', 'Ramesh Kumar', 35, 'A12', 'MG Road', 'Bengaluru', 560001, 'M'),
('p_2', 'Priya Sharma', 28, 'B45', 'Residency Road', 'Bengaluru', 560025, 'F'),
('p_3', 'Rajesh Singh', 45, 'C78', 'Brigade Road', 'Bengaluru', 560042, 'M'),
('p_4', 'Asha Patel', 22, 'D34', 'Commercial Street', 'Bengaluru', 560011, 'F'),
('p_5', 'Vijay Reddy', 60, 'E56', 'Indiranagar', 'Bengaluru', 560038, 'M');

-- Inserting data into the doctor table
INSERT INTO doctor VALUES
('d_1', 'Dr. Gupta', 'Cardiologist', 'Apollo Hospital', 'h_1', '9876543210'),
('d_2', 'Dr. Sharma', 'Pediatrician', 'Fortis Hospital', 'h_2', '8765432109'),
('d_3', 'Dr. Reddy', 'Dermatologist', 'Manipal Hospital', 'h_3', '7654321098');

-- Inserting data into the prescription table
INSERT INTO prescription VALUES
('p_1', 'Dolo-650', '10 tabs', 'Fever', '2023-11-15', '10:30:00', 'd_1'),
('p_2', 'Sinarest', '5 tabs', 'Cold', '2023-11-16', '11:45:00', 'd_2'),
('p_3', 'Amoxicillin', '1 tab', 'General Prescribed', '2023-11-17', '12:30:00', 'd_3');

-- Inserting data into the pharmacist table
INSERT INTO pharmacist VALUES
('ph_1', 'Sneha Patel', 30, 'B.Pharm', 'F'),
('ph_2', 'Raj Kumar', 28, 'D.Pharm', 'M');

-- Inserting data into the medicine table
INSERT INTO medicine VALUES
('m_1', 'Dolo-650', 'Micro Labs Ltd', 10.50, '2023-12-01', 'Paracetamol 500mg', 'dd_2', 150),
('m_2', 'Sinarest', 'Centaur Pharmaceuticals Pvt Ltd', 6.70, '2024-01-01', 'Paracetamol 650mg', 'dd_4', 100),
('m_3', 'Amoxicillin', 'Dr.Reddys', 11.00, '2023-12-31', 'Amoxicillin 500mg', 'dd_1', 150);

-- Inserting data into the drug_dealer table
INSERT INTO drug_dealer VALUES
('dd_1', 'Amoxicillin', 'Dr.Reddys', '150 + 50', 11.00, '9876543210'),
('dd_2', 'Dolo-650', 'Micro Labs Ltd', '200 + 100', 1.50, '8765432109'),
('dd_3', 'VSL#3 capsules', 'Sun Pharma Lab Ltd', '0 + 50', 42.00, NULL),
('dd_4', 'Sinarest', 'Centaur Pharmaceuticals Pvt Ltd', '100 + 50', 6.70, '7654321098'),
('dd_5', 'Benadryl DR Syrup', 'JOHNSON & JOHNSON PVT LTD', '0 + 6', 63.00, '8765432109'),
('dd_6', 'Febrex 250mg/5ml', 'Indoco Remedies Ltd', '10 + 5', 35.00, '9876543210');

-- Inserting data into the med_order_p table
INSERT INTO med_order_p VALUES
(NULL, 1, 'Dolo-650', 10, 105.00, 'p_1', 'Dr. Gupta', 'Sneha Patel', '2023-11-15 10:30:00'),
(NULL, 2, 'Sinarest', 5, 33.50, 'p_2', 'Dr. Sharma', 'Raj Kumar', '2023-11-16 11:45:00'),
(NULL, 3, 'Amoxicillin', 1, 11.00, 'p_3', 'Dr. Reddy', 'Raj Kumar', '2023-11-17 12:30:00');




