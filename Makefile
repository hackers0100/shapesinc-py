PYTHON ?= python
htmldocs:
	$(PYTHON) -m pip install -r docs/requirements.txt
	$(MAKE) -C docs html
