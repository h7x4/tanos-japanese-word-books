#!/usr/bin/env bash

python3 ./toTex.py
xelatex main.tex
numberOfPages=$(pdfinfo main.pdf | awk '/^Pages:/ {print $2}')

echo $numberOfPages

cat >wrapper.tex <<EOF
\\documentclass[a4paper, twoside]{article}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{pdfpages}
\\begin{document}
  \\includepdf[pages=-,nup=1x2,signature=${numberOfPages},landscape,booklet=true]{main.pdf}
\\end{document}
EOF

pdflatex wrapper.tex