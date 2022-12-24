
## FastAPI with SQLAlchemy, Postgres, Alembic
In this project, a book database is created using python.

- __SQLAlchemy__ is used for Object Relational Mapping (ORM).
- __FastAPI__ endpoints are created for adding book and author data (post requests) and to query books data (get request).
- Database Migration is done using __Alembic__, migrating from __SQLAlchemy__ to __PostgresSQL__.
- __PGAdmin__ is a using for administration of PostgreSQL db.
- FastAPI, PostgresSQL and PGAdmin are run in sperate __Docker__ containers.
- __docker-compose__ is used for running multiple containers.

Note : postgresql docker is not persistently storing data in volumes.

Before running the services, type a password in `.env` file.

To run the services, use `docker-compose up`

After running the services, migration needs to be done from SQLAlchemy to PostgreSQL.

Run the following commands,

`docker-compose run app alembic revision --autogenerate -m "New revision"`

`docker-compose run app alembic upgrade head`



