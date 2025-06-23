# 💰 Personal Budget Tracker (Flask Web App)

This is a cross-platform, system-agnostic **personal budget tracker** built with Flask. It allows you to manage income and expenses, view summaries, and visualize data — all through a clean web interface.

## 🚀 Features

- Add, edit, and delete income/expense entries
- Dashboard with total income, total expenses, and net balance
- Interactive visualizations with Chart.js (line + pie chart)
- Tables page with pagination, modal editing, and delete confirmation
- Sidebar navigation and responsive layout using Bootstrap

## 🧱 Tech Stack

- Python 3.x
- Flask + SQLAlchemy
- SQLite (local database)
- Bootstrap 5
- Chart.js

## 🖥️ Screenshots

> 📌 _Insert screenshots here for dashboard, charts, and tables._

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/budget-tracker.git
cd budget-tracker
```

### 2. Create & Activate Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python run.py
```

Visit `http://localhost:5000` in your browser.

## 📁 Project Structure

```
budget-tracker/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── layout.html
│       ├── index.html
│       ├── add_entry.html
│       ├── tables.html
│       └── visualizations.html
├── instance/
│   └── budget.db
├── static/
│   └── style.css
├── run.py
├── requirements.txt
└── README.md
```

## 📝 To-Do / Ideas

- Date range filtering
- User login / accounts
- CSV export / import
- Dark mode toggle

## 📄 License

MIT License. Use freely for personal or commercial projects.
