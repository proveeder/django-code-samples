# Overview

This repository includes 2 projects: 'shop' and 'warehouse-api'. Warehouse works only as an API to shop and an admin  page for manager who packs orders.
Shop, by itself, sometimes updates list of books available in it and for each order sends data to warehouse to form a package for customers. 

## Features description

- Sheduled updating list of books available in shop from warehouse.
- Sending data to warehouse API as in json format.
- Session-based cart for orders with full representation of items in it and info about each.
- PostgreSQL database.
- Management commands for filling database with fake data and manual updating data from warehouse in shop project.
- DRF-based API in warehouse.
- Admin page in warehouse project.
- Logging

## Quick Start

Assuming you have Python 3.9.19, PostgreSQL and RabbitMQ installed, run the following commands:

```sh
# configure db
docker exec -it <container_name> bash # if running postgres as a container
psql -U admin
create database "django_code_samples_shop";
create database "django_code_samples_warehouse";
exit;

# first terminal window
cd shop
cp .env.sample .env # adjust configuration
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json # optional - fills database with dump data
python manage.py createsuperuser # Create a superuser (optionally)
python manage.py runserver 8000

# second terminal window
cd warehouse-api
cp .env.sample .env # adjust configuration
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json # optional - fills database with dump data
python manage.py createsuperuser # Create a superuser (optionally)
python manage.py runserver 8080

# third terminal window
cd shop
source .venv/bin/activate
celery -A shop worker -l INFO -B
```

## Linter

Run `flake8` under virtual environment.
