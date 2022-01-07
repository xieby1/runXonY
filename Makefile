all: gnuclad.svg

gnuclad.csv: runXonY.csv scripts/genGnucladCsv.py
	$(word 2,$^)

gnuclad.svg: gnuclad.csv gnuclad.conf
	gnuclad $< $@ $(word 2,$^)

clean:
	rm -f gnuclad.svg
	rm -f gnuclad.csv
