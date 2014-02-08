all: interoperability.tex

pdf: interoperability.pdf

%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

%.tex: %.md
	multimarkdown -t latex -f $< | convert_latex.py > $@

clean:
	rm -f interoperability.pdf interoperability.aux interoperability.glo interoperability.idx interoperability.ist interoperability.log interoperability.out interoperability.pdf interoperability.tex
