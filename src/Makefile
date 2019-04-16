.PHONY: all pack clean test doc run profile
APP_NAME = "RunySoft_Calculator"
VENV_NAME = "ivs"
VENV_ACTIVATE =. $(VENV_NAME)/bin/activate
PYTHON = $(VENV_NAME)/bin/python3

.DEFAULT: all

setup:
	sudo apt-get -y install python3.5 python3-pip
	python3 -m pip install virtualenv
	make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -e .
	touch $(VENV_NAME)/bin/activate

all: setup 

pack:
	cd ../;\
	zip -r $(APP_NAME) src docs plan mockup profiling skutecnost.txt hodnoceni.txt debugging.png screenshot.png README.md dokumentace.pdf

clean: 
	test -f ../$(APP_NAME).zip || make pack
	ls ../ | grep -v ${APP_NAME}.zip | sed -e 's/^/..\//' |xargs rm -r 
	unzip ${APP_NAME}.zip
