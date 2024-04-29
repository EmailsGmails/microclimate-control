# README
# Microclimate Control
## Introduction
This is a centralized management platform for optimizing indoor environments through precise monitoring and adjustment of humidity, CO2 levels, temperature, and other parameters.

## Technical introduction
This is a REST API built with Django that utilizes a number of endpoints by hierarchy projects > objects > data-points | responsibles, with permissions.

### Permissions

Permissions are set up in a way such that:
- Admin has permissions to do anything (Create, Read, Update, Delete)
- Only admin can create / delete a Project
- User with access permissions for a whole Project has capabilities to view a Project and view all its Objects, but requires Project update permission for updating Project fields, as well as separate permissions for Object mutations
- User with access permissions only for Objects can view only the Objects he has permissions to, not other objects in the project

## Setup and Running the application

### Prerequisites
- Docker Compose v2 (OR the technologies listed below if running without Docker)

### Technologies used
- Python 3.10
- Postgres 16
- Django 4.2
- Redis 7.2

## Installation

NOTE: This assumes you have a working installation of docker compose

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a .env file and fill it in based on the .env.sample file.
4. Run `docker-compose up --build -d` to set up the whole project and run it.
5. Setup the database by running `docker-compose -it web python manage.py migrate`.
6. [Optional] Populate the database with sample data `docker-compose -it web python populate.py`.

## REST API URLs
`/admin/*`

`/api/token/`

`/api/token/refresh/`

`/api/token/verify/`

`/projects/`

`/projects/<pk>/`

`/projects/<project_pk>/objects/`

`/projects/<project_pk>/objects/<object_pk>/data-points/`

`/projects/<project_pk>/objects/<object_pk>/data-points/<pk>/`

`/projects/<project_pk>/objects/<object_pk>/responsibles/`

`/projects/<project_pk>/objects/<object_pk>/responsibles/<pk>/`

`/projects/<project_pk>/objects/<pk>/`

## Utilizing some of the REST calls

This isn't a comprehensive list of all possible REST calls, but a typical usage

### Authentication
Authenticate with a user (for sample data check populate.py for username/password):
```
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "my.user", "password": "my.password"}'
```

### Projects

`GET` a list of Projects (putting your access token in place of auth_token for this and all subsequent calls):
```
curl -X GET http://localhost:8000/projects/ \
-H "Authorization: Bearer auth_token"
```

`POST` a new Project if you're authenticated as admin:
```
curl -X POST http://localhost:8000/projects/ \
-H "Authorization: Bearer auth_token" \
-H "Content-Type: application/json" \
-d '{"name": "Another Project", "description": "Another Project"}'
```

`PATCH` an existing Project if you have update permissions for the Project:
```
curl -X PUT http://localhost:8000/projects/1/ \
-H "Authorization: Bearer auth_token" \
-H "Content-Type: application/json" \
-d '{"name": "Renamed project"}'
```

### Objects

`GET` a list of Objects from a Project:
```
curl -X GET http://localhost:8000/projects/1/objects/ \
-H "Authorization: Bearer auth_token"
```

`POST` a new Object if you have permission to create new Objects for the Project:
```
curl -X POST http://localhost:8000/projects/1/objects/ \
-H "Authorization: Bearer auth_token" \
-H "Content-Type: application/json" \
-d '{"name": "Another Object", "location": "Another Location", "users": ["2"]}'
```

### Data Points

`GET` a list of Data Points from an Object:
```
curl -X GET http://localhost:8000/projects/1/objects/1/data-points/ \
-H "Authorization: Bearer auth_token"
```

`POST` a new Data Point if you have permission to create new objects for the project:
```
curl -X POST http://localhost:8000/projects/1/objects/ \
-H "Authorization: Bearer auth_token" \
-H "Content-Type: application/json" \
-d '{"name": "Another Object", "location": "Another Location", "users": ["2"]}'
```

### Responsibles

`GET` a list of Repsonsible persons from an Object:
```
curl -X GET http://localhost:8000/projects/1/objects/1/responsibles/ \
-H "Authorization: Bearer auth_token"
```
