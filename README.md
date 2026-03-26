# BloodSIM - Blood Inventory Simulation System

A Python-based blood inventory management and simulation system that tracks blood availability across multiple hospitals and generates PDF reports at regular intervals.

## Overview

BloodSIM simulates blood inventory updates based on popularity weights and generates automated reports. The system connects to a PostgreSQL database to store and manage blood stock levels for three hospitals (A, B, and C).

## Project Structure

```
BloodSIM/
├── BloodIO.py         # Blood inventory operations (add, remove, reset)
├── compostFuncs.py    # Common PostgreSQL database utilities
├── config.py          # Configuration settings and constants
├── postquery.py       # SQL schema and initial data
├── repoGEN.py         # PDF report generator
├── testcone.py        # Database connection test
├── reports/           # Generated PDF reports
└── venv/              # Virtual environment
```

## Prerequisites

- Python 3.x
- PostgreSQL database
- Required packages:
  - `psycopg2` - PostgreSQL adapter
  - `reportlab` - PDF generation

## Database Setup

1. Create a PostgreSQL database
2. Run the SQL commands from `postquery.py`:
   - Create the `blood_availability` table
   - Insert initial blood inventory data

3. Update credentials in `config.py`:
   ```python
   host = "localhost"
   port = "5432"
   db = "postgres"
   user = "postgres"
   paw = "your_password"
   ```

## Configuration

Edit `config.py` to customize:

- **Database credentials**: Connection parameters
- **Blood groups**: List of tracked blood types
- **Popularity weights**: Determines how much blood gets added per update cycle
- **Table headers**: Display names for reports

## Usage

### Test Database Connection

```bash
python testcone.py
```

### Run Simulation and Generate Reports

```bash
python repoGEN.py
```

This will:
1. Reset blood data to initial values
2. Run 5 update cycles with simulated inventory changes
3. Generate a PDF report after each cycle
4. Reports are saved in `reports/report_of_YYYY-MM-DD/`

### Available Operations (BloodIO.py)

- `add_popularity()` - Add inventory based on blood type popularity
- `remove_random()` - Simulate random blood consumption
- `dontbeNegative()` - Ensure no negative inventory values
- `reset_blood_data()` - Reset to initial default values

## Blood Types Tracked

| Blood Group | Hospital A | Hospital B | Hospital C |
|-------------|------------|------------|-------------|
| O+          | 120        | 140        | 100         |
| O-          | 50         | 45         | 45          |
| A+          | 90         | 110        | 80          |
| A-          | 25         | 30         | 25          |
| B+          | 30         | 25         | 25          |
| B-          | 10         | 12         | 8           |
| AB+         | 8          | 6          | 6           |
| AB-         | 3          | 4          | 3           |

## Popularity Weights

Higher weights indicate more demand and result in larger inventory additions:

- O+: 1.5 (highest demand)
- A+: 1.3
- O-: 1.2
- A-: 1.1
- B+: 1.0
- B-: 0.9
- AB+: 0.7
- AB-: 0.5 (lowest demand)
