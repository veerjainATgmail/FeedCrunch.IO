%~d1
cd "%~p1"
cd "../.."
call venv\Scripts\activate.bat
call cmd /k python manage.py runserver 0.0.0.0:5000
PAUSE;