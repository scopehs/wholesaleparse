# CSV Parser

Parses CSV Data and Imports to SQL to consume with metabase

## Requirements

- python
- mysql-connector
- docker

``pip install -r requirements.txt`` <br>
``py -m pip install -r requirements.txt``

## Run Docker/SQL Setup

``docker compose up ``<br>
``docker run -d -p 3000:3000 metabase/metabase``<br>

## Set up the docker network
``docker network create myNetwork``<br>
``docker network connect myNetwork mysql-mysql-1 (name of sql container)``<br>
``docker network connect myNetwork hungry_hertz (name of metabase container)``<br>

## Inspect Network for Database IP

Metabase configuration
``docker network inspect myNetwork``

## Run

``py .\main.py``
