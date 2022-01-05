# flask-login
A boilerplate account system programmed in Flask and Jinja with MongoDB integration


# SETUP

It is reccomended to run this application in a virtual environment to stop dependency clashing.

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cp ./app/.env.example ./app/.env  
```

To complete the setup you need to update your copied .env file!

```
db_user=changeme
db_pwd=changeme
db_host=changeme
db_database=changeme

secret_key=changeme
```

To run the app use
```
python3 ./app.wsgi
```
