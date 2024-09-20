# bpmc
Created in July 2024 to integrate timekeeping, mobile devices, and AI technologies.

### Requirements:
*   Python 3.10 or newer
*   Django 5.0.7 or newer.
*   Sqlite3
*   Clone bpmc repository from cmd line as follows:
```
git clone https://github.com/bpmc-group/bpmc.git
```

### System Checks:

#### Python (from cmd line)
*   python --verson or python3 --version will display the currently installed version of python. 
*   If python is not installed or an older version of python is installed, please install an appropriate version by following the instructions on https://www.python.org/downloads/

#### Django (from cmd line in bpmc folder)
*   python manage.py --version 
*   If this command doesn't return 5.0.x or new, install an appropriate version of Django by following the instructions at https://www.djangoproject.com/download/

#### Sqlite3
Sqlite3 is the default lightweight relational database manager; Python can create, read and write Sqlite3 database files without requiring separate database drivers. Different databases can be substituted for Sqlite.

### Project Startup

From the cmd line in bpmc folder, enter the following command:

```
python manage.py runserver
```

Django will perform some system checks and then will run the server on localhost:8000/ Depending on your setup you may have to use http://127.0.0.1:8000/ instead of localhost.

In a web browser, enter localhost:8000/ in the address bar. The login screen will be displayed. At this time, any user name and password will be accepted and take you to the Dashboard.

### Project Shutdown

To exit the web page, close the tab on the browser or exit the browser.

To stop the server, press Ctrl-c  (the break command)
