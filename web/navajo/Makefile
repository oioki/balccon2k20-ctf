NAME=navajo

docker:
	docker build src -t ${NAME}

run:
	docker run --rm -d -p 8000:80 --name ${NAME} ${NAME}
