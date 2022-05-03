# Work/Force - Final Year Project Source Code

## Github Code
[https://github.com/bvalenciaa/qmulworkforce](https://github.com/bvalenciaa/qmulworkforce/)

## Deployment Information
1. First, make sure you have Django and Pip installed / updated:

> `$ python -m django --version`

2. Then, install all the dependencies (available in the `requirements.txt` file)

> `$ pip install -r requirements.txt`

3. Since you will be running this code on your local server, you need to create a superadmin:

> `$ python manage.py createsuperuser`

4. Enter your desired username, email and password and wait for the confirmation message.

5. Run the server:

> `$ python manage.py runserver`

6. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with the superadmin credentials

7. Go to 'Groups' and create two user groups - **admin** and **member** (ALL LOWERCASE)

This will make sure that all new users are placed in the member group, and can therefore use the app

## Database Problems
If you are having problems connecting to the database, go to `settings.py` and locate the following code:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DEMO_TEST',
        'USER': 'postgres',
        'PASSWORD': 'muffinpower',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Change this code snippet to the following:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Questions
Please contact me if the steps above do not seem to be working for you, I'll be happy to help.

Blanca Valencia

Student ID: 190192477

University Email: bvalencia@se19.qmul.ac.uk
