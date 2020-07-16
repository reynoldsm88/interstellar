IMAGE_PREFIX = reynoldsm88
IMAGE_NAME = interstellar
VERSION := latest
IMG := $(IMAGE_PREFIX)/$(IMAGE_NAME):$(VERSION)

python-build:
	pip3 install -r requirements.txt
	python3 setup.py build
	python3 setup.py test

docker-build: python-build
	docker build -t $(IMG) .

docker-push: docker-build
	docker push $(IMG)
