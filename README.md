# DATA_ENTRY_SYSTEM
# 🗄️ Data Entry System (Python + PostgreSQL)

A simple **menu-driven data entry system** built with **Python** and **PostgreSQL**.  
This project demonstrates CRUD operations (**Create, Read, Update, Delete**) on a user table using `psycopg2`.

---

## 🚀 Features
- Add a new user with **name, age, and department**  
- Update an existing user  
- Delete a user by ID  
- View all users in the database  
- Menu-driven CLI interface for easy interaction  

---

## 🛠️ Technologies Used
- **Python 3**
- **PostgreSQL**
- **psycopg2** (PostgreSQL adapter for Python)

---

## 📦 Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/data-entry-system.git
   cd data-entry-system
Install dependencies

bash
Copy code
pip install psycopg2
Setup PostgreSQL

Make sure PostgreSQL is installed and running.

Create a database (e.g., postgres).

Update the database credentials in your code:

python
Copy code
conn = psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="your_password",
    port=5432
)
Run the program

bash
Copy code
python main.py
📋 Example Menu
sql
Copy code
WELCOME TO DATA ENTRY SYSTEM

1. ADD A USER
2. UPDATE A USER
3. DELETE A USER
4. VIEW ALL USERS
5. EXIT
ENTER YOUR SELECTION:
📊 Example Output
bash
Copy code
Viewing all users
 1 | Alice | 22 | HR
 2 | Bob   | 25 | IT
🎯 Future Improvements
Add input validation

Add search/filter options

GUI or web version using Flask/Django
