# repoGEN.py - Report Generator Module
# Generates PDF reports of blood availability data at regular intervals

import time
import os
from datetime import datetime
import compostFuncs as compost

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import BloodIO


# Establish database connection on module load
conn = compost.poscon()
cursor = conn.cursor()


def generate_report():
    """
    Generates a PDF report of current blood availability across all hospitals.
    Report includes timestamp and formatted table of blood inventory data.
    """
    # Fetch blood availability data in consistent order
    cursor.execute("""
    SELECT blood_group, hospital_a, hospital_b, hospital_c
    FROM blood_availability
    ORDER BY 
    CASE blood_group
        WHEN 'O+' THEN 1
        WHEN 'O-' THEN 2
        WHEN 'A+' THEN 3
        WHEN 'A-' THEN 4
        WHEN 'B+' THEN 5
        WHEN 'B-' THEN 6
        WHEN 'AB+' THEN 7
        WHEN 'AB-' THEN 8
    END
    """)

    data = cursor.fetchall()

    # Generate timestamp for filename and report header
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")

    # Create dated folder for report storage
    folder = f"reports/report_of_{date_str}"
    os.makedirs(folder, exist_ok=True)

    # Build complete file path
    filename = f"{folder}/report_generated_{date_str}_{time_str}.pdf"

    # Initialize PDF document elements
    styles = getSampleStyleSheet()
    elements = []

    # Add title with date and time
    elements.append(
        Paragraph(f"Blood Report - {date_str} {time_str}", styles['Heading1'])
    )
    elements.append(Spacer(1, 12))

    # Build table data starting with header row
    table_data = [
        ["Blood Group", "Hospital A", "Hospital B", "Hospital C"]
    ]

    # Add database rows to table
    for row in data:
        table_data.append(list(row))

    # Create table and apply styling
    table = Table(table_data)
    table.setStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('GRID',(0,0),(-1,-1),1,colors.black),
    ])

    elements.append(table)

    # Generate PDF file
    doc = SimpleDocTemplate(filename, pagesize=A4)
    doc.build(elements)

    print(f"Report Generated: {filename}")


# Main execution loop - generates 5 reports with inventory updates
count = 0
BloodIO.reset_blood_data()

while True:
    count += 1
    if count > 5:
        break

    # Simulate inventory changes before each report
    BloodIO.add_popularity()
    BloodIO.remove_random()
    BloodIO.dontbeNegative()

    # Generate report reflecting updated inventory
    generate_report()

    print("Waiting 10 sec...")
    time.sleep(1)  # Reduced from 10s for testing
    
# Clean up database resources on completion
cursor.close()
conn.close()
