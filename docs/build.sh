pandoc -o "Kurs.pdf" chapter/*.md --from markdown --template "template/eisvogel.tex" --listings --toc --pdf-engine=xelatex