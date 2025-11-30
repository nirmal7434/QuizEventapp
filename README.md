# 🎓 Quiz Events App - Setup Guide
---
## ✨ What This App Does

A list of all quizzes appears on the website.
When a user clicks a quiz, the questions open.
Each question can be:
Multiple choice
Text answer
After answering all questions, the user clicks Submit.
The system checks all answers and shows the final score.

---


Before you start, make sure you have these installed:

### Windows
- **Python 3.10+** → Download from https://www.python.org/downloads/
  - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation


```


## 🚀 Installation (Step-by-Step)

### Step 1:Clone the Project
```bash
# Extract the ZIP file
# Open Command Prompt/Terminal in that folder
cd /path/to/QuizEventApp
path:(.venv) PS C:\Users\Lenovo\PycharmProjects\quiezproject\QuizEventApp>
```
---
### Step 2: Create Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1



### Step 3: Install Dependencies
Make sure your virtual environment is activated.
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

#### macOS/Linux
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

---

### Step 4: Create Database & Admin User

# Create admin user
py manage.py createsuperuser

# Run development server
py manage.py runserver

# Create new Django app
py manage.py startapp myapp

# Run tests
py manage.py test

#### Windows
```powershell
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

**When prompted for `createsuperuser`, enter:**
- Username: `quiz`
- 
- Password: `9090` (or your own)

✅ **Remember these credentials - you'll use them to login to admin panel**

---

### Step 5: Load Sample Data (Optional but Recommended)

This project uses SQLite3 as the default database.
A database file named db.sqlite3 is already included with the project.
So, when you run the project on any computer, all sample data (quizzes, questions, events, users, etc.) will automatically be available.

#### Windows
```powershell
py manage.py populate_sample_data
```
You should see: `✅ Sample data created successfully!`

---

## 🎯 Configuration

### File: `config/settings.py`

Key settings you might want to change:

```python
# Line ~25: Debug Mode (set to False for production)
DEBUG = True  # Set to False when deploying

# Line ~27: Allowed Hosts (add your domain here for production)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Line ~40: Database (use PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Line ~80: Email Configuration (optional)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## 🏃 Running the App

### Start the Development Server

#### Windows
```powershell
py manage.py runserver
```
You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---
---

## 📖 Using the App

### For End Users

#### Register & Login
1. Visit http://127.0.0.1:8000/users/register/
2. Enter username, email, password
3. Click "Register"
4. You're automatically logged in!



#### Login to Admin Panel
1. Visit http://127.0.0.1:8000/admin/
2. Enter admin credentials (username: `quiz`, password: `9090`)
3. Click "Log in"


### Problem: "Python not recognized"

**Solution:**
- Windows: Uninstall Python, reinstall and ✅ check "Add Python to PATH"
- macOS/Linux: Use `python3` instead of `python`

```bash
python3 --version
python3 -m venv venv
```

---

### Problem: "ModuleNotFoundError: No module named 'django'"

**Solution:** Make sure virtual environment is activated

```bash
# Windows - you should see (venv) in prompt
.\venv\Scripts\Activate.ps1


```

Then install dependencies:
```bash
pip install -r requirements.txt
``



## 📄 Version Info

- **Django**: 5.2.8 (LTS)
- **Python**: 3.10+
- **Last Updated**: November 2025
- **Status**: Production Ready

---

## 📋 Requirements File (`requirements.txt`)

```
Django==5.2.8
djangorestframework==3.16.1
python-decouple==3.8
Pillow==10.1.0
gunicorn==21.2.0
```


**Made with ❤️ using Django, Tailwind CSS.
