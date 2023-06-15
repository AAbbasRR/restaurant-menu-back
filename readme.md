## Restaurant Menu Backend

env variables:

    # ___Project Setup___ #
    SECRET_KEY = string
    DEBUG = bollean
    # ___DataBase___ #
    USE_MYSQL = boolean
    MYSQL_NAME = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_USER = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_PASS = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_HOST = url[localhost](if USE_MYSQL is true, need to set this variable.)
    MYSQL_PORT = int(if USE_MYSQL is true, need to set this variable.)
    USE_POSTGRES = boolean
    POSTGRES_NAME = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_USER = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_PASS = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_HOST= url[localhost](if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_PORT = int(if USE_POSTGRES is true, need to set this variable.)
    DEFAULT_DATABASE_NAME = str[set mysql or postgresql]


How To Run:

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

For Run Test Project Service:

    python manage.py test --pattern="tests_*.py"