IMAGE_PREFIX = docker.causeex.com/dart/
IMAGE_NAME = "interstellar"
IMG := $(IMAGE_PREFIX)$(IMAGE_NAME)

init:
	pip install -r requirements.txt

build: init
	python3 setup.py build

test: build
	python3 setup.py test

docker-build: test
	docker build -t $(IMG):latest .

clean:
	docker images | grep $(IMG) | grep -v IMAGE | awk '{print $3}'
	docker system prune --force