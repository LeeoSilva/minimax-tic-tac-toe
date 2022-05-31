run: 
	python -m src.main

test: 
	python -m pytest tests -p no:cacheprovider -v 
