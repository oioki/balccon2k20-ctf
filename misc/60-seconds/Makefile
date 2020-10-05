NAME=60-seconds

all: docker/Dockerfile docker/app/server.py docker/app/game.py
	docker build docker -t ${NAME}

run:
	docker run --rm -d -p 1100:1100 --name ${NAME} ${NAME}
