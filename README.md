# flask-login
Flask-login is a boilerplate account system programmed in Flask and Jinja with MongoDB integration.


# SETUP

It is recommended to run this application in a virtual environment to stop dependency clashing.

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cp ./app/.env.example ./app/.env  
```

To complete the setup you need to update your copied .env file.

```
db_user=changeme
db_pwd=changeme
db_host=changeme
db_database=changeme

secret_key=changeme
```

To run the app use:
```
python3 ./app.wsgi
```
# Dev README

If you wish to work with, or maintain this project, the following documentation explains function calls that are specific to this repository.

## Logging (logger.py) 

### Priority
  
  1 - Low Priority
  
  2 - Mid Priority
  
  3 - Critical Priority

### Logfiles

There are 3 types of log file:

- system
- user
- misc

Each log file will be created in the /logs/ folder if they do not exist when the function is called.

## Example usage in app.py

logger.log() expects 3 parameters with every call with usage cases shown below:

### Low Priority System
   
   ```logger.log("system",text,"1")```

### Mid Priority System
   
   ```logger.log("system",text,"2")```

### Critical Priority User
   
   ```logger.log("user",text,"3")```
