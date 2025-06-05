PYTHON ?= python
htmldocs:
	$(PYTHON) -m pip install -e .[docs]
	$(MAKE) -C docs html
