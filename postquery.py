# postquery.py - Database Schema and Initial Data
# SQL commands to create and populate the blood availability table

# Create the blood_availability table
# Stores blood inventory levels for three hospitals (A, B, C)
"""CREATE TABLE blood_availability (
    blood_group VARCHAR(5),
    hospital_a INT,
    hospital_b INT,
    hospital_c INT
);"""


# Insert initial blood inventory data for all blood types
# Values represent units available at each hospital
"""
INSERT INTO blood_availability VALUES
('O+', 120, 140, 100),
('O-', 50, 45, 45),
('A+', 90, 110, 80),
('A-', 25, 30, 25),
('B+', 30, 25, 25),
('B-', 10, 12, 8),
('AB+', 8, 6, 6),
('AB-', 3, 4, 3);
"""