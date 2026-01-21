NAME = simple_app

all:
	docker-compose up --build -d

clean:
	docker-compose stop

fclean:
	docker-compose down --rmi all --volumes

re: fclean all

.PHONY: all clean fclean re