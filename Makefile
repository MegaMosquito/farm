all: build run

build:
	docker build -t ibmosquito/farm:1.0.0 -f Dockerfile .

dev: build stop
	docker run -it --privileged \
	    --name farm \
	    -p 5000:5000 \
	    --volume `pwd`:/outside \
	    ibmosquito/farm:1.0.0 /bin/bash

run: stop
	docker run -d --privileged --restart unless-stopped \
	    --name farm \
	    -p 5000:5000 \
	    ibmosquito/farm:1.0.0

test:
	echo "Connect to port 5000 on this host to test."

exec:
	docker exec -it farm /bin/sh

push:
	docker push ibmosquito/farm:1.0.0

stop:
	-docker rm -f farm 2>/dev/null || :

clean: stop
	-docker rmi ibmosquito/farm:1.0.0 2>/dev/null || :

.PHONY: all build dev run test exec push stop clean
