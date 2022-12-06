echo 'building the project...'
python3.9 -m pip install psycopg2-binary
python3.9 -m pip install django==4.0
python3.9 -m pip install dj-database-url
python3.9 -m pip install django-environ
python3.9 -m pip install gunicorn
python3.9 -m pip install boto3
python3.9 -m pip install django-cors-headers
python3.9 -m pip install django-tinymce
python3.9 -m pip install urllib3
python3.9 -m pip install whitenoise
python3.9 -m pip install six
python3.9 -m pip install Pillow
python3.9 -m pip install s3transfer
python3.9 -m pip install sqlparse
python3.9 -m pip install tzdata
python3.9 -m pip install django-storages
python3.9 -m pip install jmespath
python3.9 -m pip install python-dateutil
python3.9 -m pip install pytz
python3.9 -m pip install django-heroku
python3.9 -m pip install asgiref
python3.9 -m pip install botocore



echo 'Make migrations...'
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo 'Collect static...'
python3.9 manage.py collectstatic --noinput --clear