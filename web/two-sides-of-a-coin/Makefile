NAME=two-sides-of-a-coin

all: docker/app/app.py docker/app/board.db docker/Dockerfile
	docker build docker -t ${NAME}

docker/app/board.db: src/prepare.py
	cd src && ./prepare.py

run:
	docker run --rm -d -p 5002:5002 --name ${NAME} ${NAME}

clean:
	rm -rf docker/app/board.db docker/app/__pycache__
