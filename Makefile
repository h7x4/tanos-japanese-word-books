.PHONY: clean all

all: wrapper-main.pdf wrapper-nx.pdf

clean:
	rm -r build pdf

dirs:
	mkdir build
	mkdir build/texdata
	mkdir pdf

build/texdata/nx.tex: dirs 
	python python/htmlToTex.py

build/nx.tex: build/texdata/nx.tex
	python python/createMainDoc.py

main.pdf: build/nx.tex
	cd build; xelatex main.tex
	
nx.pdf: build/nx.tex
	cd build; for n in 5 4 3 2 1; do \
		xelatex n$$n.tex; \
	done

wrapper-main.pdf: main.pdf
	python python/createWrapperDoc.py main.pdf main-wrapper.tex
	cd build; pdflatex main-wrapper.tex
	mv build/main-wrapper.pdf pdf/main.pdf

wrapper-nx.pdf: nx.pdf
	for n in 5 4 3 2 1; do \
		python python/createWrapperDoc.py n$$n.pdf n$$n-wrapper.tex; \
	done;

	cd build; for n in 5 4 3 2 1; do \
		pdflatex n$$n-wrapper.tex; \
		mv n$$n-wrapper.pdf ../pdf/n$$n.pdf; \
	done;