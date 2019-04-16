.PHONY: all pack clean test doc run profile
APP_NAME = "RunySoft_Calculator"
VENV_NAME = "ivs"
VENV_ACTIVATE =. $(VENV_NAME)/bin/activate
PYTHON = $(VENV_NAME)/bin/python3

.DEFAULT: all

all: 

pack:
	cd ../;\
	zip -r $(APP_NAME) src docs plan mockup profiling skutecnost.txt hodnoceni.txt debugging.png screenshot.png README.md dokumentace.pdf

clean: 
	rm -rf ivs

test:
	cd tests; python3 test.py

doc:
	cd ../docs; make html