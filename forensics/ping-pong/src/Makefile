all: hans ping-responder bin

hans:
	git clone https://github.com/friedrich/hans.git

bin: bin/hans bin/ping-responder.py

bin/hans: hans
	mkdir -p bin
	cd hans && (patch --forward -p1 < ../hans.patch || true) && make && cp hans ../bin/

ping-responder:
	git clone https://github.com/PixelsCamp/ping-responder

bin/ping-responder.py:
	cd ping-responder && (patch --forward -p1 < ../ping-responder.patch || true) && cp src/ping-responder.py ../bin/

clean:
	rm -rf hans ping-responder bin
