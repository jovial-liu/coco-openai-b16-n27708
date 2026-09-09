# Figure assets for the Astra working base

The LaTeX baseline refers to three figure slots:

- `figure1_method_compact.pdf` — method schematic.
- `figure2_identification.pdf` — held-out identification controls.
- `qualitative_cases_wide.png` — qualitative CCI/WF examples.

The user wants Astra to **redesign the figures rather than preserve the latest ChatGPT redraws**. For that reason this GitHub handoff prioritizes browsable source/reference material rather than treating the last generated PDF figures as authoritative.

Use the raw material in:

`../../../../04_ORIGINAL_FIGURE_ASSETS/previous_gpt6_ultra_package/`

In particular:
- `references/figure1_schematic_reference.svg` is a small browsable vector schematic reference;
- `references/old_figure1_plot.png` is the old identification-control plot;
- `data/figure1_data.csv` contains exact Full/Cross point/CI data plus Absent-only point estimates;
- `brief/` contains the scientific constraints and figure-design brief.

The exact Absent-only CI endpoints were later verified from the archived `round2_identification.csv`; keep the endpoints already stated in the manuscript/README and do not infer them visually.

The large local handoff also contained the exact user-provided `figure1_full_vector_redraw_v5.svg` and the full-resolution qualitative PNG, but those large local-only assets were not duplicated through this connector. If Astra receives them separately, treat them as raw references, not as mandatory final layout.