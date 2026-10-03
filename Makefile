PYTHON ?= python3

.PHONY: validate list dist clean

validate:
	$(PYTHON) scripts/validate.py

list:
	@find skills -mindepth 1 -maxdepth 1 -type d -print | sed 's#skills/##' | sort

dist: validate
	$(PYTHON) scripts/pack.py

clean:
	rm -rf dist
