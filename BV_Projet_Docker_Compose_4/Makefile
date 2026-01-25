# Variables
COMPOSE = docker-compose

.PHONY: all up down purge-bdd purge-all

all: up

up:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down

# Supprime uniquement les données de la base de données (volume)
purge-bdd:
	$(COMPOSE) stop database
	docker volume rm $$(docker volume ls -q | grep db_data) || true
	$(COMPOSE) up -d database

# Nettoyage total : containers, réseaux, images et tous les volumes
purge-all:
	$(COMPOSE) down -v --rmi all
	docker system prune -f