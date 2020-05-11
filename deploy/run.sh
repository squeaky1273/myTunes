python manage.py collectstatic --noinput
python manage.py migrate
gunicorn playlister.wsgi --bind=0.0.0.0:80