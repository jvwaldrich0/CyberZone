import os


if os.name == 'nt':
    os.system('pip install -r requirements.txt --no-dependencies; python src/manage.py runserver')
else:
    os.system('pip install -r requirements.txt --no-dependencies; python src/manage.py runserver || python3 src/manage.py runserver')