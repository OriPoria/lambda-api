# lambda-api

The purpose of this repository is to test migration from basic FastApi project to AWS lambda

## How to run
run server locally
```
python -muvicorn main:app --reload
```

## Requirements
- fastapi
- sqlalchemy
- sqlalchemy_aurora_data_api

## Project structure
* main.py <br>
The module where all the FastAPI endpoints are located.
The 'get_db' function return a sqlalchemy session for each new request
to one of the API endpoints.

* database.py <br>
In database.py there is a function that create a connection to existing database located on RDS cluster in AWS, called 'get_connection'.
and with sqlalchemy_aurora_data_api lib there connection is done.
Locally, there is a file called 'database_config.json' with credentials to connect to the RDS cluster.
* models.py <br>
Module that contains the DDL of the tables in the RDS cluster database.