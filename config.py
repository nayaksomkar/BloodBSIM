# config.py - Configuration Settings
# Contains database credentials and application constants

# PostgreSQL database connection parameters
host = "localhost"
port = "5432"
db = "postgres"
user = "postgres"
paw = "pass"

# List of all blood group types in the system
blood_groups = ['O+','O-','A+','A-','B+','B-','AB+','AB-']

# Popularity weights determine how much blood gets added per update cycle
# Higher weights = more inventory additions (reflects demand)
popularity = {
    'O+': 1.5,
    'O-': 1.2,
    'A+': 1.3,
    'A-': 1.1,
    'B+': 1.0,
    'B-': 0.9,
    'AB+': 0.7,
    'AB-': 0.5
}


# Table header for display/report purposes
table_data = [
     ["Blood Group", "Hospital A", "Hospital B", "Hospital C"]
]
