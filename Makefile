install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 start_tests.py

format:
	black *.py

lint:
	pylint --disable=R,C sample.py

all: install lint test
