#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Checked vector PDFs are the authoritative build assets. Editable SVG sources
# are included, but are not regenerated automatically so renderer differences
# cannot silently change the submitted figures.
for f in \
  main.tex authors.tex references.bib icassp2027_paperkit.sty \
  figures/figure1_method_final.pdf \
  figures/figure2_identification_final.pdf \
  figures/qualitative_cases_compact_labels.png; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 2; }
done

rm -f main.aux main.bbl main.blg main.log main.out main.pdf
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex8 main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
