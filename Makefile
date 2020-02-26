IMAGE_PREFIX = org.reynoldsm88
IMAGE_NAME = "interstellar"
IMG := $(IMAGE_PREFIX)/$(IMAGE_NAME)

python-build:
	pip3 install -r requirements.txt
	python3 setup.py build
	python3 setup.py test

docker-build: python-build
	docker build -t $(IMG):latest .

docker-push: docker-build
	docker push $(IMG)