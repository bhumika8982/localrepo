# Expense Tracker 
##  Project Description

The **Expense Tracker** is a web-based application developed using **Django** that helps users track, manage, and analyze their daily expenses efficiently. The project allows users to record income and expenses, categorize them, and monitor spending habits in a structured way.

This project focuses on **user authentication, database management, and CRUD operations** using Django’s powerful ORM. It is designed to be beginner-friendly while following real-world development practices.

---

## Features

* User Registration & Login (Django Authentication)
* Add, Edit, and Delete Expenses
* Categorize Expenses (Food, Travel, Shopping, etc.)
* Track Date-wise Expenses
* Secure User-specific Data
* Simple & Clean UI
* Database integration using Django ORM

---

## Technologies Used

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

##  Project Structure

```
Expense_Tracker/
│── manage.py
│── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── expenses/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│── static/
│── db.sqlite3
```

---

##  Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd expense-tracker
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open browser and visit:

   ```
   http://127.0.0.1:8000/
   ```

---

##  Learning Outcomes

* Understanding Django project structure
* Working with Django ORM
* Implementing authentication system
* Handling CRUD operations
* Git & GitHub workflow

---

##  Future Enhancements

* Monthly & yearly expense reports
* Expense charts and analytics
* Export expenses to CSV/PDF
* Improved UI/UX

---

