init:
	pip install -r requirements.txt

test: init
	python3 setup.py test

build:
	python3 setup.py build