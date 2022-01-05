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
# Dev README

## Logging (logger.py) 

### Priority
  
  1 - Low Priority
  
  2 - Mid Priority
  
  3 - Critical Priority

### Logfiles
   system
   user
   misc

## Example usage in app.py

### Low Priority System
   
   logger.log("system",text,"1")

### Mid Priority System
   
   logger.log("system",text,"2")

### High Priority User
   
   logger.log("user",text,"3")
