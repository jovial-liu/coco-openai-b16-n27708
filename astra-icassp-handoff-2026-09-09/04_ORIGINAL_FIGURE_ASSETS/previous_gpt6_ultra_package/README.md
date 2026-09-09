# Figure 1 redesign package for GPT-6 Ultra

## Goal

Create **one final all-vector Figure 1** that combines:

1. a compact method schematic explaining selection-stage target-tolerant worst-foil reranking and strict held-out audit separation; and
2. a compact empirical identification-control panel carrying the strongest evidence from the old Figure 1.

The final figure should be suitable for an **ICASSP / IEEE two-column paper**, not a slide or poster.

## Recommended composition

Use a single wide figure with two side-by-side panels:

- **(a) Selection and held-out audit:** ~60-62% of width.
- **(b) Identification controls:** ~38-40% of width.
- Total figure height target: roughly **47-50 mm** at final paper placement; avoid exceeding ~53 mm.

### Panel (a): compact method schematic

The reviewer should understand the following sequence in one glance:

`Original CCI -> epsilon-feasible set -> worst-foil rerank -> REGION FIXED -> held-out audit`

Keep only the essential equations / labels:

- Original CCI: `R_CCI = argmax_R d_R^sel(t)`
- Feasible set: `d_R^sel(t) >= d_R_CCI^sel(t) - epsilon`, with `epsilon = 0.02`
- Rerank objective: maximize `d_R^sel(t) - max_f d_R^sel(f)` inside the feasible set
- A visually explicit divider between **SELECTION STAGE** and **HELD-OUT AUDIT**
- Make `REGION FIXED` the key visual node. Add small text `before held-out evaluation`.
- Held-out outputs should be three compact endpoints: `Specificity`, `Target response`, `Locality`.
- No feedback arrow from held-out audit into selection.
- If response traces are shown, label them `illustrative / not to scale`; however, preferred design is to remove most response-trace decoration and save space.

Do not use `Negative -> Less negative` as a general label. Use neutral wording such as `lower margin -> improved margin`, or omit it.

### Panel (b): compact forest plot

Redraw the old Figure 1 as a **horizontal mini forest plot**, not as the current large grouped vertical error-bar chart.

Four rows:

- COCO B/16
- COCO B/32
- VOC B/16
- VOC B/32

Three series, distinguished by both marker shape and color so the figure remains readable in grayscale:

- Full foils: circle
- Cross-foil: square
- Absent-only: triangle

Use a vertical zero-reference line. Horizontal axis: normalized aggregate gain `Delta P_max^agg` (norm.). Keep the range compact around 0 to 0.020. Slightly offset the three markers vertically within each row to avoid CI overlap.

Use exact values in `data/figure1_data.csv`. **Do not invent missing annotation-absent CI endpoints.** If they cannot be recovered from source artifacts, either (i) show absent-only point markers without CI bars and state this clearly in the caption, or (ii) recover the exact archived endpoints before drawing.

## Visual style

- IEEE paper aesthetic: restrained, clean, technical.
- Full vector SVG/PDF output. Do not rasterize text or plots.
- White background, no gradients, no shadows.
- Very light rounded corners only (2-3 pt equivalent), not pill-shaped cards.
- Main stroke ~0.75-0.85 pt; secondary rules ~0.55-0.65 pt.
- Use at most two accent colors plus neutral gray/black structure.
- Marker shape must carry series identity in addition to color.
- Final printed text should generally stay at **>= 6.5-7 pt**, panel titles ~8-8.5 pt.
- Avoid border collisions, arrow/text overlap, excessive internal padding, and large empty whitespace.
- Keep arrows aligned; do not let arrowheads touch boxes or labels.

## Panel labels

Use concise headings:

- `(a) Selection and held-out audit`
- `(b) Identification controls`

Do not use a long marketing-style title inside the figure.

## Suggested caption

**Figure 1: Selection-audit separation and identification controls.** (a) Target-tolerant reranking uses only selection-stage responses: candidates within epsilon of the original CCI target response are reranked by their target-worst-foil margin, and the selected region is fixed before held-out evaluation. Specificity, target response, and spatial locality are then evaluated separately. (b) Held-out normalized aggregate worst-foil gains at epsilon=.02 for full foils, category-disjoint cross-foil evaluation, and annotation-absent evaluation. Points denote paired estimates and bars denote 95% confidence intervals where exact endpoints are available.

## Files in this package

- `paper/liu_submission_compliance_final_oldfig_reference_compressed.pdf` - paper reference with the original empirical Figure 1; use the equations, terminology, and page layout as scientific context.
- `references/old_figure1_plot.png` - isolated old identification-control plot.
- `references/old_figure1_plot_and_caption.png` - plot plus original caption.
- `references/figure1_schematic_reference.svg` - compact reconstructed vector reference based on the previously supplied schematic; use it as a layout/content reference, not as a mandated exact design.
- `data/figure1_data.csv` - exact values available from the paper text/table, with missing absent-only CI endpoints explicitly left blank.
- `brief/PAPER_KEY_CONTEXT.md` - relevant equations and scientific constraints.

## Deliverables requested from GPT-6 Ultra

Please return:

1. editable SVG source;
2. vector PDF export suitable for `\includegraphics` in LaTeX;
3. optionally the drawing script/source used to generate the figure;
4. one compact version optimized for two-column ICASSP width;
5. verify no clipped text, overlapping borders, broken math symbols, or rasterized labels.
