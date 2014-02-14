## Requirements:
# https://github.com/fletcher/MultiMarkdown-4
# https://github.com/fletcher/peg-multimarkdown-latex-support
# https://code.google.com/p/dot2tex/
# https://pypi.python.org/pypi/Pygments
# https://github.com/gniezen/n3pygments
# LaTeX
# LaTeX modules: minted, graphviz, etc. (earlier: Tikz, dot2texi.)
#
# On Ubuntu Linux:  
#
# apt-get install texlive-latex-extra dot2tex python-pygments
# git clone https://github.com/fletcher/MultiMarkdown-4.git
# cd MultiMarkdown-4/
# git submodule init
# git submodule update
# make -j4
# sudo make install
# sudo easy_install https://github.com/gniezen/n3pygments/archive/master.zip
# git clone https://github.com/fletcher/peg-multimarkdown-latex-support.git ~/texmf/tex/latex/mmd
# git clone https://github.com/drayside/graphviz.sty.git  ~/texmf/tex/latex/graphviz
# sudo texhash


all: interoperability.tex

pdf: interoperability.pdf

%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

%.tex: %.md
	multimarkdown -t latex -f $< | ./convert_latex.py > $@

clean:
	rm -f interoperability.pdf interoperability.aux interoperability.glo interoperability.idx interoperability.ist interoperability.log interoperability.out interoperability.pdf interoperability.tex
