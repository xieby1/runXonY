all: test/runXonY.svg test/runXonY.dot gnuclad/gnuclad.svg index.html

gnuclad/gnuclad.csv: runXonY.csv scripts/genGnucladCsv.py
	$(word 2,$^) > $@

test/runXonY.csv test/runXonY.dot &: scripts/lib.py scripts/data.py scripts/cmdl.py
	scripts/cmdl.py -c test/runXonY.csv -d test/runXonY.dot

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
	rm -f gnuclad/gnuclad.svg
	rm -f gnuclad/gnuclad.csv
	rm -f index.html
