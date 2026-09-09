# Build instructions

The checked PDF assets in `figures/` are authoritative build inputs. Editable SVG sources are included for Figures 1 and 2, but `build.sh` intentionally does not regenerate their PDFs; this avoids renderer-dependent visual drift.

Required tools: `pdflatex` and `bibtex8`.

```bash
bash build.sh
```

The script removes prior LaTeX build products, runs `pdflatex`, `bibtex8`, then two final `pdflatex` passes, and produces `main.pdf`.

This revision contains 5 US-Letter pages. Pages 1--4 contain technical content; page 5 contains references only. Added Tables 5--7 and the associated diagnostic paragraphs are grounded in existing archived frozen-tensor outputs documented in `ADDED_EXPERIMENTS_PROVENANCE.md`. Figure 3 is intentionally single-column so the opposite column can carry quantitative analyses.
