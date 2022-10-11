define \n


endef
CMDL_GEN = \
		   test/runXonY.csv \
		   test/runXonY.dot \
		   test/web/runXonY.json \
		   test/relplot.svg
ALL_GEN = test/runXonY.svg test/runXonY.dot test/web/test.js \
		  gnuclad/gnuclad.svg index.html
all: ${ALL_GEN}

test/web/test.js: test/web/test.ts
	tsc $<

gnuclad/gnuclad.csv: runXonY.csv scripts/genGnucladCsv.py
	$(word 2,$^) > $@

${CMDL_GEN} &: scripts/lib.py scripts/data.py scripts/cmdl.py
	scripts/cmdl.py \
		-c test/runXonY.csv \
		-d test/runXonY.dot \
		-j test/web/runXonY.json \
		-r test/relplot.svg

gnuclad/gnuclad.svg: gnuclad/gnuclad.csv gnuclad/gnuclad.conf
	gnuclad $< $@ $(word 2,$^)

test/runXonY.svg: test/runXonY.csv gnuclad/gnuclad.conf
	gnuclad $< $@ $(word 2,$^)

index.html: index.md web/template.html web/head.html
	pandoc --metadata title="runXonY" \
		--template $(word 2,$^) \
		-H $(word 3,$^) \
		--toc \
		-o $@ \
		$(word 1,$^)

clean:
	$(foreach x,${ALL_GEN},rm -f ${x}${\n})
	$(foreach x,${CMDL_GEN},rm -f ${x}${\n})
