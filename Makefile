LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

.PHONY: resources

all: html resources adrszbb

css:
	scss resources/pinout.scss > resources/pinout.scss.css

html:
	./generate-html.py $(LANG)

adrszbb:
	./generate-html-adrszbb.py $(LANG)

resources:
	cp -r resources output/$(LANG)/

devel: css all
	./serve.py ${LANG}

clean:
	rm -rf output/$(LANG)/*

serve: all
	./serve.py $(LANG)
