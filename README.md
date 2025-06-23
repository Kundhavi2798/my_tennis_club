# my_tennis_club
This Django project is a simple tennis club member management system. It allows you to add, view, edit, and delete club members through a web interface. Members' details such as name, email, and phone number are managed and displayed in a user-friendly way.

## Getting Started

### 1. Create a New Django Project
```bash
python3 -m venv venv
source venv/bin/activate
pip install django

# Create a new Django project
python3 -m django startproject my_tennis_club
cd my_tennis_club

# Create the members app
python3 manage.py startapp members
```

### 2. Add the App to Installed Apps
- Open `my_tennis_club/settings.py` and add `'members',` to the `INSTALLED_APPS` list.

### 3. Create the Member Model
- Define your `Member` model in `members/models.py`.

### 4. Make Migrations and Migrate
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Create a Superuser (for Admin Access)
```bash
python3 manage.py createsuperuser
```
Follow the prompts to set up your admin account.

### 6. Register the Model in Admin
- Register the `Member` model in `members/admin.py`.

### 7. Set Up URLs and Views
- Configure your URLs and views to display, add, edit, and delete members.

### 8. Run the Development Server
```bash
python3 manage.py runserver
```

### 9. Access the Application
- Visit `http://127.0.0.1:8000/` for the welcome page.
- Visit `http://127.0.0.1:8000/members/` to view all members.
- Visit `http://127.0.0.1:8000/admin/` to access the Django admin panel.

### 10. Add, Edit, or Delete Members
- Use the web interface to add, edit, or delete members.
- Use the admin panel for advanced management.
