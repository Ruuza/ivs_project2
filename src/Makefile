.PHONY: all pack clean test doc run profile
APP_NAME = "RunySoft_Calculator"
CACHE := __pycache__/
DOCS = "sphinx_doc/build"
EXE = "runycalc"

all: 


pack:
	@make clean
	@cd ../;\
	zip -r $(APP_NAME) src plan mockup profiling skutecnost.txt hodnoceni.txt debugging.png screenshot.png README.md dokumentace.pdf

clean: 
	@rm -rf $(DOCS)


test:
	@cd tests; python3 test_calc_lib.py

doc:
	@cd sphinx_doc; make html

run:
	@$(EXE)

profile:
	
	



