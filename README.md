# 💰 Cost of Living Index - Web Application

> A comprehensive Flask-based web application that compares cost of living indices across different countries with interactive data management and financial planning tools.

**Live Demo:** 🚀 https://mini-project-cost-of-living.onrender.com

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Code Examples](#code-examples)
- [Deployment](#deployment)
- [Team](#team)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📊 Overview

The **Cost of Living Index** is a full-stack web application designed to help users:
- 🌍 Compare cost of living metrics across countries
- 📈 Analyze trends in living expenses (rent, groceries, dining, etc.)
- 💼 Access financial planning and budgeting resources
- 🎯 Manage country data through an intuitive admin dashboard
- 📱 View real-time comparisons with interactive tables and sorting

**Language Composition:**
- HTML: 83.1%
- CSS: 11.8%
- Python: 5.1%

**Repository Stats:**
- Created: April 6, 2025
- Status: Active Development ✅
- License: Open Source
- Stars: ⭐

---

## ✨ Features

### 🎯 Core Features
✅ **Cost Comparison** - Compare 7 different cost metrics across countries
✅ **Search & Filter** - Quickly find countries using the search functionality
✅ **Sorting** - Sort by any column (ascending/descending)
✅ **CRUD Operations** - Add, edit, update, and delete country records
✅ **Admin Dashboard** - Manage all country data securely
✅ **Data Visualization** - Interactive charts and analysis tools
✅ **Financial Planning** - Budgeting and saving tips
✅ **Responsive Design** - Mobile-friendly interface
✅ **Real-time Updates** - Instant data synchronization
✅ **User-Friendly Interface** - Intuitive navigation

### 📊 Metrics Tracked Per Country
Each country entry tracks 7 essential metrics:

| Metric | Description |
|--------|-------------|
| **Rank** | Country's cost of living rank |
| **Cost of Living Index** | Overall index value (higher = more expensive) |
| **Rent Index** | Housing/accommodation costs |
| **Groceries Index** | Food and grocery prices |
| **Restaurant Index** | Dining and restaurant prices |
| **Local Purchase Index** | Power of local currency purchasing |
| **Currency** | Measured in Indian Rupees (₹) |

---

## 🏗️ Tech Stack

### Backend
- **Framework:** Flask 3.1.0
- **Database:** SQLite with SQLAlchemy ORM 2.0.40
- **Server:** Gunicorn 23.0.0
- **Language:** Python 3.x
- **ORM:** Flask-SQLAlchemy 3.1.1

### Frontend
- **Template Engine:** Jinja2 3.1.5
- **Styling:** Custom CSS (Bootstrap-inspired)
- **JavaScript:** Vanilla JS for interactivity
- **DOM Manipulation:** Dynamic table operations
- **Responsive Framework:** Mobile-first design

### Data Analysis & Visualization
- **Pandas** 2.2.3 - Data manipulation
- **NumPy** 2.2.4 - Numerical computing
- **Matplotlib** 3.10.1 - Static data visualization
- **Seaborn** 0.13.2 - Statistical visualization
- **Scikit-learn** 1.6.1 - ML capabilities
- **SciPy** 1.15.2 - Scientific computing
- **Plotly** 5.24.1 - Interactive charts
- **Altair** 5.0.1 - Declarative visualization

### Deployment
- **Hosting:** Render.com (Free tier)
- **Build Tool:** Docker (optional)
- **CI/CD:** Automated deployments
- **Web Server:** Gunicorn WSGI
- **Configuration:** .render.yaml

### Utilities
- **Werkzeug** 3.1.3 - WSGI utilities
- **Click** 8.1.8 - Command-line interface
- **Jinja2** 3.1.5 - Template engine

---

## 📁 Project Structure

Mini_Project-Cost_of_living/ │ ├── 📄 app.py # Main Flask application (138 lines) ├── 📄 requirements.txt # Python dependencies (125+ packages) ├── 📄 .render.yaml # Render deployment configuration ├── 📄 README.md # Project documentation │ ├── 📁 models/ # Database models │ ├── init.py │ ├── pycache/ │ └── data.py # Countrytable model (17 lines) │ ├── 📁 templates/ # HTML templates (Jinja2) │ ├── base.html # Base template with navbar (481 lines) │ ├── index.html # Landing page (42 lines) │ ├── table.html # Public comparison view (121 lines) │ ├── tableadmin.html # Admin dashboard (210 lines) │ ├── aboutus.html # About page with team (230 lines) │ ├── financialplaning.html # Financial planning guide (289 lines) │ ├── budget.html # Budgeting tips │ ├── saving.html # Saving strategies │ ├── analyze.html # Data analysis page │ ├── insite.html # Insights dashboard │ └── requirements.txt # Template dependencies │ ├── 📁 static/ # Static assets │ ├── style.css # Main stylesheet (174 lines) │ ├── style1.css # Additional styles (657 bytes) │ ├── style2.css # Admin dashboard styles (2858 bytes) │ ├── styleabout.css # About page styles (4751 bytes) │ └── 📁 image/ # Image assets directory │ ├── 📁 utils/ # Utility functions │ └── db.py # Database utilities │ ├── 📁 instance/ # Runtime directory │ └── country.db # SQLite database (auto-generated) │ └── 📁 pycache/ # Python cache (auto-generated)

Code

---

## 🗄️ Database Schema

### Countrytable Model

```sql
CREATE TABLE countrytable (
    Rank INTEGER PRIMARY KEY,
    Country VARCHAR(255) NOT NULL,
    Cost_Of_Living INTEGER NOT NULL,
    Rent_Index INTEGER NOT NULL,
    Groceries_Index INTEGER NOT NULL,
    Restaurant_Index INTEGER NOT NULL,
    Local_Purchase INTEGER NOT NULL
);
Sample Data Record
JSON
{
  "Rank": 1,
  "Country": "Switzerland",
  "Cost_Of_Living": 140,
  "Rent_Index": 135,
  "Groceries_Index": 128,
  "Restaurant_Index": 142,
  "Local_Purchase": 132
}
Data Types
Column	Type	Constraints
Rank	INTEGER	PRIMARY KEY
Country	VARCHAR(255)	NOT NULL
Cost_Of_Living	INTEGER	NOT NULL
Rent_Index	INTEGER	NOT NULL
Groceries_Index	INTEGER	NOT NULL
Restaurant_Index	INTEGER	NOT NULL
Local_Purchase	INTEGER	NOT NULL
🔌 API Endpoints
Navigation Routes
Route	Method	Purpose	Returns
/	GET	Home page	HTML
/home	GET	Alternative home	HTML
/aboutus	GET	About page with team	HTML
/finance	GET	Financial planning guide	HTML
/budget	GET	Budgeting tips	HTML
/saving	GET	Saving strategies	HTML
/analyze	GET	Data analysis page	HTML
/insite	GET	Insights dashboard	HTML
Data Management Routes
Route	Method	Purpose	Returns
/table	GET	View all countries (public)	HTML with table
/tableadmin	GET	Admin dashboard with controls	HTML with form
/add_country	POST	Add new country	Redirect
/update_country/<rank>	POST	Update existing country	Redirect
/delete_country/<rank>	POST	Delete country	Redirect
/api/country/<rank>	GET	Fetch country as JSON	JSON
Request/Response Examples
GET /api/country/1

JSON
{
  "rank": 1,
  "country": "Switzerland",
  "costOfLiving": 140,
  "rentIndex": 135,
  "groceriesIndex": 128,
  "restaurantIndex": 142,
  "localPurchase": 132
}
POST /add_country

Code
Headers: Content-Type: application/x-www-form-urlencoded

Body:
rank=10
country=Japan
costOfLiving=130
rentIndex=120
groceriesIndex=125
restaurantIndex=135
localPurchase=128
Response: Redirects to /table on success

📦 Dependencies
Core Flask Packages
Code
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.40
Gunicorn==23.0.0
Werkzeug==3.1.3
Jinja2==3.1.5
Click==8.1.8
MarkupSafe==3.0.2
Data Science & Analytics
Code
Pandas==2.2.3
NumPy==2.2.4
Scikit-learn==1.6.1
SciPy==1.15.2
Matplotlib==3.10.1
Seaborn==0.13.2
Plotly==5.24.1
Altair==5.0.1
Jupyter & Development
Code
Jupyter==1.1.1
JupyterLab==4.3.5
IPython==8.32.0
Notebook==7.3.2
Utilities
Code
certifi==2025.1.31
requests==2.32.3
python-dateutil==2.9.0
pytz==2025.1
beautifulsoup4==4.13.1
Full list: See requirements.txt for complete dependencies (125+ packages)

🚀 Installation & Setup
Prerequisites
Python 3.7 or higher
pip package manager
Git
Virtual environment (recommended)
Step 1: Clone Repository
bash
git clone https://github.com/SuhasGowda24/Mini_Project-Cost_of_living.git
cd Mini_Project-Cost_of_living
Step 2: Create Virtual Environment
bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Initialize Database
bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
Step 5: Run Application
bash
python app.py
Step 6: Access Application
Local URL: http://localhost:5000
Home Page: http://localhost:5000/
Public Comparison: http://localhost:5000/table
Admin Dashboard: http://localhost:5000/tableadmin
Docker Setup (Optional)
bash
# Build Docker image
docker build -t cost-of-living .

# Run container
docker run -p 5000:5000 cost-of-living
📖 Usage Guide
1. View Cost Comparison
Navigate to /table
Browse all countries and their metrics
Use search bar to find specific countries
Click sort buttons (⬆️⬇️) to arrange by any column
2. Search & Filter
Enter country name in search box
Results filter in real-time
Case-insensitive search
Partial matching supported
3. Sort Functionality
Click ⬆️ for ascending order
Click ⬇️ for descending order
Sort by any column (Rank, Country, Costs, etc.)
Re-sort multiple times
4. Admin Operations (Admin Dashboard)
Go to /tableadmin
To Add:
Click "Add Country" button
Fill all fields
Click "Save"
To Edit:
Click "Edit" button on row
Modify values
Click "Save"
To Delete:
Click "Delete" button
Confirm deletion
5. Financial Planning
Visit /finance for planning tips
Explore /budget for budgeting strategies
Check /saving for saving advice
Review /analyze for data analysis
