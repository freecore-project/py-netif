PYTHON ?= /usr/local/bin/python3
PREFIX ?= /usr/local

build:
	${PYTHON} setup.py build

install:
	${PYTHON} setup.py install --prefix ${PREFIX}
