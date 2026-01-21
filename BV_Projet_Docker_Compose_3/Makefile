.PHONY: build up down logs ps

# Lancer le projet
up:
	docker-compose up -d --build

# Arrêter le projet
down:
	docker-compose down

# Voir les logs (notamment pour vérifier l'IP de sortie Tor)
logs:
	docker-compose logs -f

# Statut des conteneurs
ps:
	docker-compose ps

# Nettoyage complet
clean:
	docker-compose down --rmi all --volumes