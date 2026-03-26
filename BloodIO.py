# BloodIO.py - Blood Inventory Operations Module
# Handles database read/write operations for blood availability across hospitals

import compostFuncs as compost
import config
import random


# Establish database connection
conn = compost.poscon()
cursor = conn.cursor()


def add_popularity():
    """
    Updates blood inventory based on popularity weights.
    More popular blood types receive higher additions to inventory.
    """
    for blood in config.popularity:
        # Calculate addition based on popularity weight (1-10 random * weight)
        add_value = int(random.randint(1,10) * config.popularity[blood])
        
        # Update all three hospitals with the calculated value
        cursor.execute("""
        UPDATE blood_availability
        SET hospital_a = hospital_a + %s,
            hospital_b = hospital_b + %s,
            hospital_c = hospital_c + %s
        WHERE blood_group = %s
        """, (add_value, add_value, add_value, blood))

    conn.commit()
    print("Popularity update done")


def remove_random():
    """
    Simulates random blood consumption by removing random quantities
    from all hospitals for each blood type.
    """
    for blood in config.blood_groups:
        # Remove random quantity (1-5 units) from each hospital
        cursor.execute("""
        UPDATE blood_availability
        SET hospital_a = hospital_a - %s,
            hospital_b = hospital_b - %s,
            hospital_c = hospital_c - %s
        WHERE blood_group = %s
        """, (random.randint(1,5), random.randint(1,5), random.randint(1,5), blood))

    conn.commit()
    print("Random update done")


def dontbeNegative():
    """
    Ensures no negative blood quantities exist in the database.
    Sets any negative values to zero using GREATEST SQL function.
    """
    cursor.execute("""
        UPDATE blood_availability
        SET 
            hospital_a = GREATEST(hospital_a, 0),
            hospital_b = GREATEST(hospital_b, 0),
            hospital_c = GREATEST(hospital_c, 0)
        """)
    
    conn.commit() 
    print("Negative values fixed")


def reset_blood_data():
    """
    Resets blood availability table to initial default values.
    Deletes all records and inserts predefined starting inventory.
    """
    conn = compost.poscon()
    cursor = conn.cursor()

    # Clear existing table data
    cursor.execute("DELETE FROM blood_availability")

    # Insert initial inventory values for all blood types
    cursor.execute("""
    INSERT INTO blood_availability VALUES
    ('O+', 120, 140, 100),
    ('O-', 50, 45, 45),
    ('A+', 90, 110, 80),
    ('A-', 25, 30, 25),
    ('B+', 30, 25, 25),
    ('B-', 10, 12, 8),
    ('AB+', 8, 6, 6),
    ('AB-', 3, 4, 3)
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Blood data reset successfully")
