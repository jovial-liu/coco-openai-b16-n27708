# Prior-version map

The local handoff contained several historical PDFs/source ZIPs. They are intentionally not duplicated here as ZIP archives; the useful evolution is summarized below so Astra can browse the current working source directly.

## `refbalanced`
Reduced the bibliography from 27 to 15 genuinely cited references and used the released space for method/protocol/results detail.

## `teacher_experiment_filled`
Removed the `Limitations` section at the teacher's request and filled technical-page space with existing archived quantitative analyses rather than filler text.

## `floatflow`
Fixed the large page-3 hole by removing a forced `\\clearpage`, using normal top floats instead of rigid placement, and allowing Additional Results text to flow into page 3.

## `experiment_rich`
Added archived epsilon-frontier and failure-transition diagnostics. These are the source of the current frontier/transition values; no new model forwards were run.

## `singlecol_filled`
Made the qualitative Figure 3 single-column so the adjacent column could contain quantitative analysis. This layout direction was explicitly preferred by the user.

## `layout_rebalanced` — recommended base
Balanced page 4 after Figure 3 became single-column; retained the dense 5-page layout, 15 references, and pre-redraw figures. This is the source copied under `01_PRIMARY_WORKING_BASE/source/`.

## `final_typography` — text-only reference, visuals rejected
Tried to enlarge/redraw figure typography and replaced the approximate cross-setting Table 7 with exact COCO/B16 archived switch-conditioned statistics. The user rejected its figure appearance. The textual differences are preserved in `00_START_HERE/main_rebalanced_vs_latest_typography.diff` and `02_LATEST_TEXT_REFERENCE_DO_NOT_COPY_FIGURES/main.tex`.

Astra should start from `layout_rebalanced`, selectively take later text/scientific cleanup, and redesign figures independently.