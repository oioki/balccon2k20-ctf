NAME=let-me-see
VERSION=7.19.3

all: docker/bin/curl docker

docker/bin/curl:
	curl -O https://curl.haxx.se/download/archeology/curl-${VERSION}.tar.gz
	tar xf curl-${VERSION}.tar.gz
	cd curl-${VERSION} && ./configure && make
	mkdir -p docker/bin docker/lib
	cp curl-${VERSION}/src/.libs/curl docker/bin/
	cp curl-${VERSION}/lib/.libs/libcurl.so* docker/lib/

docker: docker/app/app.py
	docker build docker -t ${NAME}

run:
	docker run --rm -d -p 5000:5000 --name ${NAME} ${NAME}

clean:
	rm -rf curl-${VERSION} curl-${VERSION}.tar.gz
	rm -rf docker/bin docker/lib
