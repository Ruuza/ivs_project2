.PHONY: all pack clean test doc run profile
APP_NAME = "RunySoft_Calculator"
CACHE := $(wildcard */__pycache/)
DOCS = "sphinx_doc/build"
EXE = "runycalc"
TEAM = "xruzan00_xkratk17_xlebod00_xandrl08"

all: 

pack: doc makefolder createzip clean

createzip:
	@cd ../..; zip -r ivs_project2/$(TEAM).zip $(TEAM)

makefolder:
	@mkdir -p ../../$(TEAM)/repo
	@mkdir ../../$(TEAM)/installer
	@mkdir ../../$(TEAM)/doc
	@cp -a ../. ../../$(TEAM)/repo
	@cp -a $(DOCS)/ ../../$(TEAM)/doc
	@cp -a ../$(EXE).deb ../../$(TEAM)/installer

clean: 
	@rm -rf ../../$(TEAM)


test:
	@cd tests && python3 test_calc_lib.py

doc:
	@cd sphinx_doc; make html

run:
	@$(EXE)

profile:
	
	



