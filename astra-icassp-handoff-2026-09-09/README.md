# ICASSP 2027 paper handoff to Astra

## What the user wants now
Do not continue the last ChatGPT visual redesign. The user explicitly rejected the latest typography/figure redraw. Astra should take over both layout and figure design while preserving the scientific content and verified numbers.

## Recommended starting point
Start from:
- `01_PRIMARY_WORKING_BASE/source/main.tex`
- the source assets under `01_PRIMARY_WORKING_BASE/source/figures/`

This is the best pre-redraw layout baseline. It has the 4-author version, 15 references, no Limitations section, Figure 3 in one column, and the denser page flow the user/teacher asked for.

Use `02_LATEST_TEXT_REFERENCE_DO_NOT_COPY_FIGURES/main.tex` only as a textual/scientific delta reference. It contains some later wording/Table-7 cleanup, but the user dislikes the redrawn Figure 1/2/3 visuals in that version. Do NOT blindly reuse `rejected_figures/`.

## Figure assets Astra should use as raw material
Prefer the original/pre-redraw assets in `04_ORIGINAL_FIGURE_ASSETS/`:
- `figure1_full_vector_redraw_v5.svg` — user-provided method schematic reference.
- `figure1_combined.svg` and `figure1_combined_editable.svg` — earlier combined Figure-1 attempts.
- `rebalanced_figures/figure1_method_source.svg` / `figure1_method_compact.svg` — pre-redraw method assets.
- `rebalanced_figures/figure2_identification_source.svg` / `figure2_identification.svg` — pre-redraw identification plot assets.

## Scientific content that must not drift
Paper title: BEYOND MEAN FOILS: AUDITING WORST-FOIL SPECIFICITY IN FROZEN CLIP REGION EXPLANATIONS

Authors: Kaixin Liu, Zhipeng Ye, Feng Jiang, Qiufeng Wang. Do NOT restore Jinye Li.

Core method:
- Original CCI: R_CCI = argmax_R d_R^sel(t).
- Selection margin: M^sel(R,t) = d_R^sel(t) - max_{f in F_t} d_R^sel(f).
- Feasible set: R_epsilon = {R : d_R^sel(t) >= d_R_CCI^sel(t) - epsilon}.
- Rerank: R_WF(epsilon) = argmax_{R in R_epsilon} M^sel(R,t).
- epsilon = .02 is the fixed main operating point.
- Held-out prompts are evaluated only after the selected region is fixed. No held-out feedback into selection.

Main protocol:
- K=8 frozen CCI candidate regions.
- COCO val2014: 27,708 eligible images.
- VOC2007 test: 1,943 images.
- OpenAI CLIP ViT-B/16 and ViT-B/32.
- Main intervention blocks selected patch K/V columns across all ViT blocks/heads while retaining prefix token.
- 10,000 paired unique-image bootstrap, main seed 1701.
- Cross-foil uses fixed category folds; annotation-absent is a separate identification control.
- LAION is excluded from new direct-reranking claims because historical text-normalization provenance was not safely recoverable.

Main Table-1 numbers at epsilon=.02:
- COCO B/16: P_CCI -.342; Delta P +.0150 [+.0131,+.0169]; Delta d_t +.00005 [-.00034,+.00044]; Delta bbox -.00118 [-.00199,-.00036]; switch 2.39%; fail 74.04 -> 73.89%.
- COCO B/32: -.304; +.0108 [+.00945,+.0122]; -.00010 [-.00046,+.00027]; -.00080 [-.00162,+.00002]; 2.21%; 73.91 -> 73.75%.
- VOC B/16: +.168; +.0118 [+.00677,+.0183]; -.00085 [-.00227,+.00059]; -.00340 [-.00652,-.00034]; 2.57%; 58.16 -> 57.59%.
- VOC B/32: +.186; +.00867 [+.00441,+.0143]; -.00069 [-.00184,+.00040]; +.00023 [-.00288,+.00341]; 1.96%; 55.89 -> 55.58%.

Identification controls — Cross-foil exact gains:
- COCO B/16 +.01052 [+.00901,+.01198]
- COCO B/32 +.00728 [+.00629,+.00846]
- VOC B/16 +.00705 [+.00296,+.01140]
- VOC B/32 +.00438 [+.00131,+.00784]

Annotation-absent point estimates:
- +.00939, +.00697, +.00809, +.00443.
Exact archived CI endpoints were later verified from `round2_identification.csv`; if Astra needs them, retain the values already present in the source/figure, do not estimate them visually.

Same-feasible-set baselines (WF / lambda=.1 / Mean / Uniform / 2nd d_t):
- COCO B/16 .0150 / .0147 / .0025 / .0006 / .0002
- COCO B/32 .0108 / .0106 / .0015 / -.0025 / -.0023
- VOC B/16 .0118 / .0113 / .0073 / .0010 / .0026
- VOC B/32 .0087 / .0083 / .0055 / -.0044 / -.0046

Important later diagnostics already in the source:
- COCO B/16 at epsilon=.02: 663/27,708 images switch.
- Among switched images, archived exact mean aggregate improvement is +.625624; median approximately +.406; 611/663 = 92.2% improve.
- Mean switched target-response delta +.00218; mean bbox delta -.0495.
- Aggregate failure transitions for COCO B/16: 42 fail->pass, 0 pass->fail; prompt-event: 128 fail->pass, 3 pass->fail.
- Prompt-family hardest-foil identity agreement: 59.25%, 66.82%, 53.32%; mean pairwise 59.80%; all-three exact 46.36%; semantic-family 53.69%.
- Foil-count sensitivity and epsilon/tolerance-frontier tables are already in the source; keep only if they remain legible and genuinely useful.

## Claim discipline
The paper is an audit + sparse/local repairability study, NOT a claim of a universally superior explanation method.
Do not write that "worst-foil debt is sparse"; prevalence can be high. The sparse quantity is region switching / local repairability.
Do not collapse target response, specificity, and spatial locality into one metric.
Do not imply annotation-absent or cross-foil is human semantic ground truth.
Do not reintroduce LAION into the new direct-reranking claim.
Keep the qualitative counterexample/trade-off evidence.

## Layout requirements from the user/teacher
- Maximum 5 pages.
- Pages 1-4 should be dense technical content; avoid obvious half-page holes.
- Page 5 should be references only; 10-15 references is the target (currently 15). It does not need to be artificially filled with irrelevant citations.
- No `Limitations` section.
- Figure 3 should be single-column so the other column can carry text/tables.
- Avoid `[H]`, unnecessary `\clearpage`, `\newpage`, and float choices that create large holes.
- Do not solve density by making tables/figure labels tiny.
- Figure 1/2 should remain vector where possible.
- The user dislikes the latest ChatGPT-redrawn Figure 1/2; redesign them from the original assets with cleaner ICASSP aesthetics.

## What Astra should deliver
1. A visually improved 5-page PDF.
2. Full compilable LaTeX source.
3. Editable vector source for Figure 1 and Figure 2 (SVG/PDF; scripts if used).
4. No scientific-number changes without explicit justification.
5. Visual inspection of all 5 rendered pages, especially float flow on pages 3-4.

## Repository note
This GitHub handoff intentionally stores the project expanded rather than as ZIP archives. Text/LaTeX/SVG assets are directly browsable. Large binary duplicates from historical versions are intentionally omitted when the same content is available as source/vector assets.