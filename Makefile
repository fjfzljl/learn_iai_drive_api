install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 start_tests.py

format:
	black *.py
