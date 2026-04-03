# BloodSIM - Blood Inventory Simulation System

A Python-based blood inventory management and simulation system that tracks blood availability across multiple hospitals and generates PDF reports.

The UI is available here: [https://nayaksomkar.github.io/BloodSIM.ui/](https://nayaksomkar.github.io/BloodSIM.ui/)

## 📁 Project Structure

```
BloodSIM/
├── BloodIO.py         # Blood inventory operations (add, remove, reset)
├── compostFuncs.py    # PostgreSQL database connection utilities
├── config.py          # Configuration settings and constants
├── postquery.py       # SQL schema and initial data
├── repoGEN.py         # PDF report generator
├── testcone.py        # Database connection test
├── app.py            # Flask web server for UI
├── index.html        # Web dashboard UI
├── style.css         # Dashboard styling
├── script.js         # Dashboard JavaScript logic
├── blooddata.json    # JSON data file for web UI
├── reports/          # Generated PDF reports
```

## 🛠️ Prerequisites

- Python 3.x
- PostgreSQL database
- Required packages: `psycopg2`, `reportlab`, `flask`

## ⚡ Quick Start

### Option 1: Web Dashboard (Recommended)
```bash
pip install flask
python app.py
# Open http://127.0.0.1:5000
```

### Option 2: PostgreSQL Backend
```bash
# Setup database
psql -U postgres -f postquery.py

# Test connection
python testcone.py

# Run simulation
python repoGEN.py
```

## 📦 Components

| File | Description |
|------|-------------|
| `config.py` | Database credentials, blood groups, popularity weights |
| `BloodIO.py` | Functions: add_popularity(), remove_random(), reset_blood_data() |
| `compostFuncs.py` | Database connection and query functions |
| `repoGEN.py` | Generates PDF reports with blood inventory data |
| `app.py` | Flask server serving the web dashboard |
| `index.html` | Interactive dashboard with table and controls |
| `style.css` | Clean styling for the dashboard |
| `script.js` | JavaScript for data loading and CSV export |

## 🏥 Blood Types Tracked

| Blood Group | Hospital A | Hospital B | Hospital C |
|-------------|------------|------------|------------|
| O+          | 120        | 140        | 100        |
| O-          | 50         | 45         | 45         |
| A+          | 90         | 110        | 80         |
| A-          | 25         | 30         | 25         |
| B+          | 30         | 25         | 25         |
| B-          | 10         | 12         | 8          |
| AB+         | 8          | 6          | 6          |
| AB-         | 3          | 4          | 3          |

## 📊 Features

- **Web Dashboard**: View and modify blood inventory, download CSV reports
- **Database Backend**: PostgreSQL-based storage with full simulation
- **PDF Reports**: Automated report generation with timestamps
- **n8n Integration**: Chatbot workflow for querying inventory (see `workflows/`)
