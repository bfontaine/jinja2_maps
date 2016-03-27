SRC=jinja2_maps

COVERFILE:=.coverage
COVERAGE_REPORT:=report -m

VENV=venv
BINPREFIX=$(VENV)/bin/

PIP=$(BINPREFIX)pip
PYTHON=$(BINPREFIX)python

PY_VERSION:=$(subst ., ,$(shell python --version 2>&1 | cut -d' ' -f2))
PY_VERSION_MAJOR:=$(word 1,$(PY_VERSION))
PY_VERSION_MINOR:=$(word 2,$(PY_VERSION))
PY_VERSION_SHORT:=$(PY_VERSION_MAJOR).$(PY_VERSION_MINOR)

ifdef TRAVIS_PYTHON_VERSION
PY_VERSION_SHORT:=$(TRAVIS_PYTHON_VERSION)
endif

.PHONY: check check-versions stylecheck covercheck coverhtml docs

default: deps check-versions

deps: $(VENV)
	$(PIP) install -r requirements.txt
ifeq ($(PY_VERSION_SHORT),2.6)
	$(PIP) install unittest2
endif
ifneq ($(PY_VERSION_MAJOR),3)
	$(PIP) install wsgiref==0.1.2
endif

$(VENV):
	virtualenv $@

check:
	$(PYTHON) tests/test.py

check-versions:
	$(BINPREFIX)tox

stylecheck:
	$(BINPREFIX)pep8 $(SRC)

covercheck:
	$(BINPREFIX)coverage run --source=$(SRC) tests/test.py
	$(BINPREFIX)coverage $(COVERAGE_REPORT)

coverhtml:
	@make COVERAGE_REPORT=html covercheck
	@echo '--> open htmlcov/index.html'

clean:
	find . -name '*~' -delete
	rm -f $(COVERFILE)
	$(MAKE) -C docs clean

publish: stylecheck check-versions
	cp README.rst README
	$(PYTHON) setup.py sdist upload
	rm -f README

docs:
	PATH="../$(VENV)/bin:$$PATH" $(MAKE) -C docs html
