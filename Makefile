init:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +
	find . -name '*__pycache__' -exec rm --recursive --force  {} +

lint:
	flake8

.PHONY: init clean lint
