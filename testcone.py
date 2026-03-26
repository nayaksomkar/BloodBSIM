# testcone.py - Database Connection Test
# Simple script to verify PostgreSQL database connectivity

import compostFuncs as compost


# Test database connection using compostFuncs module
connector = compost.poscon()

print("Connected successfully!")
connector.close()
