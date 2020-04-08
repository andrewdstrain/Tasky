# Tasky
Tasky is a simple task manager. It was originally written to be run on the IBM Cloud, but this version has all of the IBM Cloud code removed.

## Getting Started
First, be sure that Python 3 is installed. If not, be sure and install it now.

Next, make a virtual environment for Python 3 (macOS/Linux/UNIX):

```shell script
python3 -m venv venv
```

On Windows 10:

```shell script
python -m venv venv
```

Invoke the virtual environment (macOS/Linux/UNIX):

```shell script
source venv/bin/activate
```

On Windows 10:

```shell script
venv\Scripts\activate.bat
```

Then install the packages needed to run Tasky:

```shell script
python -m pip install -r requirements.txt
```

Copy the `dotenv-default` file to `.env` and change the `SECRET_KEY` variable to something unique for your Tasky app.

Finally, run the local Tasky server:

```shell script
python manage.py run
```

## Other Things ...
### Other Databases
By default, Tasky uses the SQLite3 database. Using another database is pretty easy. Do the following steps:

1. Install the SQLAlchemy version of your database driver.
2. In the `.env` file, change the environment variable `DATABASE_URL` to the new connection URL.

### Flask Shell
You can play around with the database by running the Flask shell:

```shell script
flask shell
```

For this to work, the `.env` file must be in place OR you can set the environmental variables before running the command.

The `app`, `db`, and `login` variables are already setup as are the `TaskyUser` and `TaskyTask` classes. This saves a bit of work when working with the Python interpreter.

### Google reCAPTCHA v2
Tasky supports using a reCHAPCHA on the signup page. Follow these steps to set it up:

1. Sign up for the [Google reCAPTCHA v2](http://www.google.com/recaptcha/admin).
2. Copy the contents of the `dotenv-recaptcha` file and paste them into the `.env` file.
3. Change the `RECAPTCHA_PUBLIC_KEY` variable to your public key.
4. Change the `RECAPTCHA_PRIVATE_KEY` variable to your private key.
5. If you want to use SSL, change the `RECAPTCHA_USE_SSL` variable to True.
