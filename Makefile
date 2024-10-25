install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=python_library test_*.py

format:	
	black *.py
	black python_library/*.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py python_library/*.py
	
all: install lint test format

activate:
	source /home/vscode/venv/bin/activate