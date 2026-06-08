# Tank Note API

REST API built with FastAPI (Python).

## Features

-   FastAPI framework
-   Modular structure (routers, services, schemas)
-   Ready for JWT authentication
-   Ready for PostgreSQL integration

## Requirements

-   Python 3.10+
-   pip
-   virtualenv

## Installation

``` bash
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

## Run project

``` bash
uvicorn app.main:app --reload --port 9000
```

## Docs

Swagger UI: http://localhost:9000/docs

## Structure

app/ main.py routers/ schemas/ services/ database/ core/
