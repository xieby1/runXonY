define \n


endef
ALL_GEN = src/images/timeline.svg src/images/relplot.svg \
		  test/web/test.js
all: ${ALL_GEN}
	mdbook build

test/web/test.js: test/web/test.ts
	tsc --target es6 $<

CMDL_GEN = data/timeline.csv test/web/runXonY.json src/images/relplot.svg
${CMDL_GEN} &: src/lib.py src/data.py src/cmdl.py
	src/cmdl.py \
		-c $(word 1,${CMDL_GEN}) \
		-j $(word 2,${CMDL_GEN}) \
		-r $(word 3,${CMDL_GEN})

# gnuclad svg lacks of viewBox,
# which will causing cannot resizing by css
# add one to generated svg
# https://stackoverflow.com/questions/644896/how-do-i-scale-a-stubborn-svg-embedded-with-the-object-tag
src/images/timeline.svg: data/timeline.csv data/gnuclad.conf
	gnuclad $< $@ $(word 2,$^)
	identify -format 'viewBox="0 0 %w %h"\n' $@ | sed -i '/height/r /dev/stdin' $@

clean:
	$(foreach x,${ALL_GEN},rm -f ${x}${\n})
	$(foreach x,${CMDL_GEN},rm -f ${x}${\n})
