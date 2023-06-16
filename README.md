## Gridkey Test

## Requirements

- Python 3.10.7
- Django 4.2.2

## Quickstart

python -m venv <name of Envireonment>  # Create Virtual Environment
<name of Envireonment>/Scripts/activate  # Activate Virtual Environment
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Admin login credentials:
login:- admin
password:- 123456

API list:-
1) https://github.com/SSJagani/-gridkey-test.git
        For An API which returns average buy price and balance quantity after any day.
2) http://127.0.0.1:8000/api/v1/transaction/create
        For An API which enables addition of above mentioned 3 types of transactions.
