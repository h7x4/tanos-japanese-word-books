
build:
	mkdir build
	mkdir build/texdata

pdf:
	mkdir pdf

build/nx.tex: build
	python python/toTex.py


tex/nx.tex: build/nx.tex
	python python/createDoc.py

main.pdf: tex/nx.tex pdf
	cd build; xelatex main.tex
	mv build/*.pdf pdf
	
nx.pdf: tex/nx.tex pdf
	cd build; for n in 5 4 3 2 1; do \ 
		xelatex ../tex/$$n.tex; \
	done
	mv build/*.pdf pdf
