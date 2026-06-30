# CLI Password Manager

A command-line password manager built in Python with a MySQL backend. Supports user registration, login, and secure password generation.

---

## Features

- **Sign up** with email and password
- **Sign in** with email validation and limited attempts
- **Generate strong passwords** with customizable length
- **Store credentials** securely in a MySQL database
- **Email format validation** on all inputs

---

## Project Structure

```
password_manager/
│
├── main.py          # Entry point — sign in or sign up
├── auth.py          # sign_up() and sign_in() logic
├── database.py      # MySQL connection and user operations
├── generator.py     # Random password generator
├── utils.py         # Email validation
└── README.md
```

---

## How It Works

```
Start
  ↓
Sign in or Sign up?
  ↓
SIGN UP:
  → Enter email (validated)
  → Enter password manually or generate one
  → Account saved to database
  → Redirected to sign in

SIGN IN:
  → Enter email → 3 attempts max
  → Enter password → 3 attempts max
  → Access granted or denied
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| MySQL | Database for storing users |
| mysql-connector-python | Connect Python to MySQL |
| `secrets` module | Cryptographically secure password generation |
| `re` module | Email format validation |

---

## Setup

**1. Install dependencies**

```
pip install mysql-connector-python
```

**2. Create the database in MySQL**

```sql
CREATE DATABASE passwords;
USE passwords;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

**3. Update credentials in `database.py`**

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="passwords"
)
```

**4. Run the app**

```
python main.py
```

---

## Password Generator

Generates a random password between 8 and 12 characters using letters, digits, and symbols.

```
enter the length of the password: 10
your password is: aB3!xK9@mN
```
