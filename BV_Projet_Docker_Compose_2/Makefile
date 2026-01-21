NAME = user_app

all:
	docker-compose up --build -d

clean:
	docker-compose down

fclean: clean
	docker system prune -a --force

re: fclean all

purge:
	rm -rf ./data/*.db
	@echo "Base de données réinitialisée."

.PHONY: all clean fclean re purge