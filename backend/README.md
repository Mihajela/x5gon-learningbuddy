## Installation guide

Create **.env** file (in this directory) with the following:

```
SECRET_KEY = <key>
PRODUCTION = <leave empty if not in production>
DATABASE_NAME = <name>
DATABASE_USER = <user>
DATABASE_PASSWORD = <password>
DATABASE_PORT = <port>
DATABASE_HOST = <host>
MSCRIPTS_PORT = <mscripts_port>
MSCRIPTS_HOST = <mscripts_host>
```

Then `pip install -r requirements.txt` (preferably in virtual env)

Run backend with `python manage.py runserver`
