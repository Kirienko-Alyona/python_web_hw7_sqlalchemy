docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
poetry add alembic sqlalchemy
alembic init alembic #--> alembic.ini
alembic revision --autogenerate -m 'Init'
