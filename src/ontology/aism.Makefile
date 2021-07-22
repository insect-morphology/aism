## Customize Makefile settings for aism
##
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

TEMPLATE=https://docs.google.com/spreadsheets/d/e/2PACX-1vTB08Ra6nDGZYa4sDBnyJsBXrodFPAh7yioiG9_1c5pA9RTi3Ss4ZxFbqQDy-PiO87FQ30mVhtCIjKj/pub?gid=0&single=true&output=tsv

TEMPLATESDIR=../templates

TEMPLATES=$(patsubst %.tsv, $(TEMPLATESDIR)/%.owl, $(notdir $(wildcard $(TEMPLATESDIR)/*.tsv)))

.PHONY: templates
templates: $(TEMPLATES)

.PHONY: prepare_templates
prepare_templates: 
	make $(TEMPLATESDIR)/aism1_template.tsv -B

$(TEMPLATESDIR)/%.owl: $(TEMPLATESDIR)/%.tsv $(SRC)
	$(ROBOT) -vvv merge --prefix "EX: http://aism.ex/EX_" -i $(SRC) template --template $< --output $@ && \
	$(ROBOT) -vvv annotate --input $@ --ontology-iri $(ONTBASE)/components/$*.owl -o $@

$(TEMPLATESDIR)/aism1_template.tsv:
	wget "$(TEMPLATE)" -O $@

