# ICASSP paper — final author and layout revision

Start with `paper_author_revision_5pages.pdf`; edit `source/main.tex`.
Latest Figure 1 spacing pass: wider/taller candidate cells, numerals centered by
their actual glyph outlines, three horizontal process arrows on one shared
baseline, and a clear gap between the fixed-region label and the template box.
The reranking arrow now follows a gentle curve; the boundary reads “Region
fixed” in lighter title case. Endpoint glyphs are a bullseye, a descending
response curve and a patch-grid localization box.
The latest pass implements review items 1, 3, 4, 5 and 6. Read
`PRESUBMISSION_REVISION.md` for the exact changes and evidence.
The compiled manuscript is five pages: four pages of paper content and one
page of references. Do not change the paperkit margins or body font size.

## Authorized changes in this revision

- Authors: Kaixin Liu, Zhipeng Ye, Feng Jiang, Qiufeng Wang, Hao Li, **Xihang Zhou**.
  Xihang Zhou is last; his Toronto affiliation and email are user-supplied.
  Hao Li's affiliation and email were transcribed from the supplied
  ProtoZoom manuscript; see CITATION_AND_AUTHOR_PROVENANCE.md.
- Added IDEA in the Introduction, with the final journal citation, key
  `ye2026idea`. Existing bibliography entries are preserved.
- Merged Additional Results into Results; Conclusion remains a closing
  paragraph. Removed the redundant manual page break.
- Figure 1 restores the previous scatter/epsilon-feasible-region design at the
  user's request. The bar-based redesign was rejected. Small vector glyphs
  now reinforce fixed-region locking, specificity contrast, target-response
  drop and spatial overlap. Soft blue, ochre and teal remain. The response
  geometry is illustrative, not measured data. Its
  geometry is approximately 178 × 49.4 mm. It is illustrative, not measured.
- Acknowledgment removal, scope discussion, table formatting and vector
  Figure 3 labels from the preceding authorized revision are retained.

## Scientific invariants

Main equations, table estimates and confidence intervals were compared with
the baseline. The exact Figure 2 data are in
`source/data/round2_identification.csv`; Absent-only intervals come from that
archived CSV, not visual estimation. See source/FIGURE_PROVENANCE.md.
The original qualitative image and final vector labels are included. The
photographic crops and intervention overlays are pixel-identical to the
supplied image. This package is not a full raw-experiment archive.

## Build

From `source/`, with a TeX installation providing the required packages:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python verify_artifacts.py
```

Figure generation needs Python, Matplotlib, NumPy and Pillow; verification also
needs PyMuPDF. Final PDF/SVG/PNG assets are already included, so regeneration
is unnecessary for ordinary text edits. `python make_figures.py` regenerates
all three figures, invoking draw_figure1.py and draw_figure3.py for their
respective panels. All ordinary labels are >=9 pt; math scripts are smaller.

`identification_controls_archived_table.tex` contains the exact removed table
whose data are displayed in Figure 2. Baseline files support the numeric
comparison and are not the current paper. VALIDATION.txt records the final
checks. No GitHub push or main-branch modification was performed.
