all: gnuclad.svg index.html

gnuclad.csv: runXonY.csv scripts/genGnucladCsv.py
	$(word 2,$^)

gnuclad.svg: gnuclad.csv gnuclad.conf
	gnuclad $< $@ $(word 2,$^)

index.html: index.md template.html head.html
	pandoc --metadata title="runXonY" \
		--template ./template.html \
		-H ./head.html \
		-o $@ ./index.md

clean:
	rm -f gnuclad.svg
	rm -f gnuclad.csv
	rm -f index.html
