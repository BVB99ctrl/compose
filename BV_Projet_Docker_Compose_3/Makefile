# Variables
COMPOSE = docker-compose

.PHONY: help up down restart logs ps clean

help: ## Affiche cette aide
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Lance les conteneurs en arrière-plan et construit si nécessaire
	$(COMPOSE) up -d --build

down: ## Arrête et supprime les conteneurs
	$(COMPOSE) down

restart: ## Redémarre proprement tous les services
	$(COMPOSE) down
	$(COMPOSE) up -d --build

logs: ## Affiche les logs de tous les services en continu
	$(COMPOSE) logs -f

ps: ## Affiche l'état des services
	$(COMPOSE) ps

clean: ## Nettoie tout : conteneurs, images et volumes non utilisés
	$(COMPOSE) down --rmi all --volumes --remove-orphans