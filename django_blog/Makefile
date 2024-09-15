# Makefile

# Define the default target
all: db

# Target to handle database migrations
db: makemigrations migrate

# Target to create new migrations
makemigrations:
	python manage.py makemigrations


# Target to apply migrations
migrate:
	python manage.py migrate
