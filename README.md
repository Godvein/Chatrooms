# Chatroom Website

A web-based chatroom application that allows users to communicate in real time. The chatroom is designed to be simple, fast, and user-friendly.

## Demo Video

Watch a short demo of my project in action:


https://github.com/user-attachments/assets/924f8b50-2cbe-4328-800d-773f78461017


## Features

- Real-time messaging
- User authentication
- Multiple chatrooms support
  
## Installation (for testing the current progress)

1. Clone the repository:
   ```bash
   git clone https://github.com/Godvein/Chatrooms.git
   
Once cloned, navigate to the project directory:

```bash
cd Chatrooms
```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage your project dependencies.

1. Install `pipenv` if you don’t have it installed:

    ```bash
    pip install pipenv
    ```

2. Create a virtual environment and activate it:

    ```bash
    pipenv shell
    ```

If you're not using `pipenv`, you can use `venv` instead:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate   # For Windows
```

### Step 3: Install Dependencies

If you're using `pipenv`, install the dependencies from the `Pipfile`:

```bash
pipenv install
```

Alternatively, if you're using `venv`, install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database

By default, this project uses SQLite, which comes pre-installed with Django. There is no need for extra configuration for SQLite.

If you want to use a different database (such as PostgreSQL or MySQL), you will need to configure the database settings in the `settings.py` file and install the necessary database adapters.

### Step 5: Run Database Migrations

To set up the database schema, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the necessary tables in your SQLite database (or the database of your choice).

### Step 6: Create a Superuser (Admin)

To access the Django admin panel, you'll need to create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### Step 7: Detele and Rename
From chatproject folder delete productionsettings.py and rename developmentsettings.py to settings.py

### Step 8: Run the Development Server

To start the Django development server, use the following command:

```bash
daphne -b 127.0.0.1 -p 8000 chatproject.asgi:application
```

Once the server is running, visit `http://127.0.0.1:8000/` in your web browser to access the application.

You can also visit the admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials created earlier.

## Optional: Deactivate the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

If you’re using `pipenv`, simply exit the shell:

```bash
exit
```


## License

This project is licensed under the [MIT License](LICENSE).
