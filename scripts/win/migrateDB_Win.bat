%~d1
cd "%~p1"
cd "../.."
call venv\Scripts\activate.bat
call python manage.py makemigrations feedcrunch
call python manage.py migrate
call python manage.py createcachetable
PAUSE;