Python coding task
---

**Prerequierets**

`Python3, Flask`

Install all requirements from `requirements.txt`. Just run

```bash
pip3 install -r requirements.txt
```

**Before using**

Create sqlite db with just calling

```bash
python db_create.py
```

**Using**

You can use this app locally in two ways:


**1. Locally.**

```bash
python wsgi.py
``` 
REST API will be available at 127.0.0.1:5000 


**2. Docker.**

You will need `docker`, `gunicorn` and `docker-compose` installed into your environement 
Run
```bash
docker-composer build
docker-composer up
```

REST API will be available at 127.0.0.1:5001. 


After that you can call
```bash
GET http://127.0.0.1:<port>/fleets
GET http://127.0.0.1:<port>/users
GET http://127.0.0.1:<port>/fleet/<fleet_id>/users
GET http://127.0.0.1:<port>/vehicles
GET http://127.0.0.1:<port>/fleet/<fleet_id>/vehicles
POST http://127.0.0.1:<port>/fleet
POST http://127.0.0.1:<port>/user
POST http://127.0.0.1:<port>/vehicle
```

**Logging**

All logs are available in `fleet-test.log` file, but critical errors also logged into db  