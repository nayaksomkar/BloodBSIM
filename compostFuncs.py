# compostFuncs.py - Common PostgreSQL Database Functions
# Provides reusable database connection and query utilities

import psycopg2 as post
import config


def poscon():
    """
    Creates and returns a PostgreSQL database connection.
    Uses credentials from config.py module.
    
    Returns:
        psycopg2.connection: Database connection object
    """
    connector = post.connect(
        host=config.host,
        port=config.port,
        database=config.db,
        user=config.user,
        password=config.paw
    )
    
    return connector


def posreadBLOOD():
    """
    Fetches all blood availability records from the database.
    
    Returns:
        list: Tuple of blood availability records, or None if connection fails
    """
    connector = poscon()
    if connector:
        cursor = connector.cursor()
        
        # Query all blood availability data
        cursor.execute("SELECT * FROM blood_availability;")
        
        # Fetch all matching rows
        rows = cursor.fetchall()
        
        # Clean up resources
        cursor.close()
        connector.close()
        
        return rows


def posseal():
    """
    Placeholder for generic SELECT query function.
    Intended to accept custom SQL queries and return results.
    """
    pass
