all: gnuclad.svg

gnuclad.csv: runXonY.csv genGnucladCsv.py
	./genGnucladCsv.py

gnuclad.svg: gnuclad.csv gnuclad.conf
	gnuclad $< SVG $(word 2,$^)

clean:
	rm -f gnuclad.svg
	rm -f gnuclad.csv
