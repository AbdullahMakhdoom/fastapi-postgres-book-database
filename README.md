postgres docker is not persistently storing 
data in volumes.

docker-compose run app alembic revision --autogenerate -m "New revision"

docker-compose run app alembic upgrade head

