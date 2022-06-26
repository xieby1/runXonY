all: gnuclad/gnuclad.svg index.html

gnuclad/gnuclad.csv: runXonY.csv scripts/genGnucladCsv.py
	$(word 2,$^) > $@

gnuclad/gnuclad.svg: gnuclad/gnuclad.csv gnuclad/gnuclad.conf
	gnuclad $< $@ $(word 2,$^)

index.html: index.md web/template.html web/head.html
	pandoc --metadata title="runXonY" \
		--template $(word 2,$^) \
		-H $(word 3,$^) \
		-o $@ \
		$(word 1,$^)

clean:
	rm -f gnuclad/gnuclad.svg
	rm -f gnuclad/gnuclad.csv
	rm -f index.html
