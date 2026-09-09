# ICASSP 2027 paper — full handoff to Astra

## 0. What to edit

Primary working manuscript: `../current_latex/main.tex`.

The current manuscript contains the newest text/data integration, but the user does **not** like the latest Figure 1/2 redraws. Treat the current figure SVGs as content references, not visual style targets.

For layout/visual work, compare against the rebalanced source assets and figure-history files listed below. Use the current source for text/data, but use older/rebalanced SVGs for the visual language.

Do **not** modify the repository `main` branch. Work on a separate branch/folder and return editable SVG/PDF plus a clean LaTeX source.

## 1. User/teacher requirements

- Keep the paper at 5 pages.
- Pages 1–4 should be technically dense and visually well filled; page 5 should contain references only.
- Keep references around 10–15; current bibliography has 15.
- No `Limitations` section.
- Four authors only: Kaixin Liu, Zhipeng Ye, Feng Jiang, Qiufeng Wang. Do **not** restore Jinye Li.
- Figure 3 / qualitative cases should be single-column so the other column can carry experiments/text.
- Do not fill space with weak prose or by shrinking text to unreadable sizes. Prefer useful quantitative analysis and correct float flow.
- Avoid unnecessary `[H]`, forced `\newpage`, `\clearpage`, or float barriers that create large blank regions. The latest current source still contains a `\newpage` before switch-conditioned repair accounting; re-evaluate whether it is needed after re-layout.
- Figure 1 should be professional, academic, restrained, and vector. The user rejected the most recent ChatGPT redraw; do not imitate it.
- Figure 2 should be a compact vector identification-control forest plot; no PPT-like internal title.
- Keep all experimental numbers/formulas unless an archived source is explicitly re-checked.

## 2. Scientific positioning — do not drift

The paper is an **audit + sparse/local repairability** paper, not a claim that worst-foil reranking is a universally superior explanation method.

Core framing:
- Frozen CLIP/CCI can have high target response/locality while still carrying ontology-relative worst-foil specificity debt.
- The audit separates target response, worst-foil specificity, and locality.
- Reranking is a controlled test of local repairability inside the frozen candidate set.
- Only about 2% of selections switch at epsilon=.02, but switched cases can have large conditional improvements.
- Held-out evaluation occurs only after the selected region is fixed. No held-out feedback to selection.

Reviewer-defense chain that should remain visible:
1. selection-stage vs held-out separation / no leakage;
2. category-disjoint cross-foil control;
3. annotation-absent control;
4. matched foil-count control;
5. same-feasible-set baselines (random/uniform, target-only runner-up, mean-foil, Max-.1);
6. held-out target-response and bbox endpoints reported separately;
7. qualitative counterexample/non-dominance;
8. LAION direct-reranking exclusion due unresolved historical text-normalization provenance.

## 3. Canonical formulas

Intervention response:
`d_R(c) = s_m(x,c) - s_m(I(x,R),c)`.

Original CCI selector:
`R_CCI = argmax_{R in R(x)} d_R^sel(t)`.

Selection-stage worst-foil margin:
`M^sel(R,t) = d_R^sel(t) - max_{f in F_t} d_R^sel(f)`.

Feasible set:
`R_epsilon = {R: d_R^sel(t) >= d_{R_CCI}^sel(t) - epsilon}`.

Rerank:
`R_WF(epsilon) = argmax_{R in R_epsilon} M^sel(R,t)`.

Held-out matched estimands:
`P_max^pm = mean_h [d~_h(t) - max_f d~_h(f)]`.
`P_max^agg = mean_h d~_h(t) - max_f mean_h d~_h(f)`.

Fixed operating point in the main claim: `epsilon = .02`.

## 4. Canonical main numbers

Table 1 / main actual-CCI comparison at epsilon=.02:

- COCO B/16: P_CCI -.342; Delta P +.0150 [+.0131,+.0169]; Delta d_t +.00005 [-.00034,+.00044]; Delta bbox -.00118 [-.00199,-.00036]; switch 2.39%; negative 74.04 -> 73.89%.
- COCO B/32: P_CCI -.304; Delta P +.0108 [+.00945,+.0122]; Delta d_t -.00010 [-.00046,+.00027]; Delta bbox -.00080 [-.00162,+.00002]; switch 2.21%; negative 73.91 -> 73.75%.
- VOC B/16: P_CCI +.168; Delta P +.0118 [+.00677,+.0183]; Delta d_t -.00085 [-.00227,+.00059]; Delta bbox -.00340 [-.00652,-.00034]; switch 2.57%; negative 58.16 -> 57.59%.
- VOC B/32: P_CCI +.186; Delta P +.00867 [+.00441,+.0143]; Delta d_t -.00069 [-.00184,+.00040]; Delta bbox +.00023 [-.00288,+.00341]; switch 1.96%; negative 55.89 -> 55.58%.

Cross-foil exact gains/CIs:
- COCO B/16 +.01052 [+.00901,+.01198]
- COCO B/32 +.00728 [+.00629,+.00846]
- VOC B/16 +.00705 [+.00296,+.01140]
- VOC B/32 +.00438 [+.00131,+.00784]

Annotation-absent exact gains/CIs:
- COCO B/16 +.00939 [+.00819,+.01062]
- COCO B/32 +.00697 [+.00594,+.00804]
- VOC B/16 +.00809 [+.00438,+.01274]
- VOC B/32 +.00443 [+.00214,+.00727]

Same-feasible-set baselines (WF / Max-.1 / Mean / Uniform / 2nd d_t):
- COCO B/16 .0150 / .0147 / .0025 / .0006 / .0002
- COCO B/32 .0108 / .0106 / .0015 / -.0025 / -.0023
- VOC B/16 .0118 / .0113 / .0073 / .0010 / .0026
- VOC B/32 .0087 / .0083 / .0055 / -.0044 / -.0046

COCO/B16 switch-conditioned exact accounting at epsilon=.02:
- 663 / 27,708 switched (2.39%)
- 611 / 663 improving (92.2%)
- mean/median Delta P_max^agg among switches +.6256 / +.406
- mean Delta d_t among switches +.00218
- mean Delta bbox precision among switches -.0495
- aggregate sign transition 42 fail->pass, 0 pass->fail
- prompt-event transition 128 fail->pass, 3 pass->fail

Prompt-family stability (COCO/OpenAI B/16):
- pair 1–2 59.25%
- pair 1–3 66.82%
- pair 2–3 53.32%
- mean pairwise 59.80%
- all-three exact 46.36%
- semantic-family agreement 53.69%

Foil-count sensitivity (COCO):
- B/16 negative: 45.8%@5, 63.5%@19, 74.0%@all; gain +.00872@5, +.01074@19
- B/32 negative: 45.0%@5, 62.8%@19, 73.9%@all; gain +.00841@5, +.00947@19

Predeclared COCO/B16 tolerance frontier:
- eps .01: switch 1.23%, full Delta P +.00791, Delta P|switch +.642, Pr(+) 90.9%
- eps .02: 2.39%, +.01497, +.626, 92.2%
- eps .05: 6.24%, +.03906, +.626, 91.6%
- eps .10: 11.68%, +.07643, +.654, 92.0%
- eps .20: 21.87%, +.14479, +.662, 92.9%

Other reported COCO/B16 diagnostics:
- 41.18% of original selections simultaneously have bbox precision >= .5, positive aggregate mean-class margin, and negative worst-foil margin.
- At eps=.02: target constraint violations = 0; selection target-drop loss mean .000245, median 0, max .01989; no exact target-score/reranking-margin ties.
- Violation breadth: V_rate .18973 -> .18751; V_mass .05878 -> .05708.

## 5. Experimental protocol invariants

- K=8 frozen CCI candidate regions.
- COCO val2014: 27,708 eligible images.
- VOC2007 test: 1,943 images.
- OpenAI CLIP ViT-B/16 and ViT-B/32.
- Main intervention blocks selected patch K/V columns across all ViT blocks/heads while retaining prefix token.
- Selection template: `a photo of a {category}`.
- Held-out templates: `a picture of the {category}`, `an image containing a {category}`, `the {category}`.
- Main CIs: 10,000 paired unique-image bootstrap resamples, seed 1701.
- Cross-foil: ten fixed seeds 1701,2701,...,10701; disjoint category folds; pool both directions.
- LAION direct reranking excluded because historical text-normalization provenance is unresolved.

## 6. Figure guidance

### Figure 1
Use an all-vector academic method schematic. Scientific story:
`Original CCI -> epsilon-feasible candidates -> worst-foil rerank -> REGION FIXED -> held-out audit`.

Must make selection/audit separation obvious. Preferred wording is target **drop**, not generic target response where d_R is the plotted quantity. Avoid claims such as `Negative -> Less negative`, because VOC P_CCI is positive. Use `lower margin -> improved margin` if any such cue remains.

Compare the older/rebalanced SVGs in `svg_versions/` and any additional rebalanced assets supplied by the user. The newest `current_latex/figures/figure1_method_final.svg` is rejected as a style target; it can still be used to recover content/notation.

### Figure 2
Compact horizontal forest/dot-CI plot. Four rows: COCO B/16, COCO B/32, VOC B/16, VOC B/32. Series: Full, Cross-foil, Absent-only. Use shape + restrained color for grayscale readability. Keep zero reference line. No large internal title; caption carries the title.

### Figure 3
Use the exact qualitative case image supplied separately as `current_latex/figures/qualitative_cases_compact_labels.png` (or archived original if redesigning labels). Keep it single-column unless a clearly better layout is proven. Do not change the cases/masks/numbers without source evidence.

Qualitative cases:
- (a) locality gain, dining table, Delta P +4.58, bbox .46 -> 1.00
- (b) specificity-locality trade-off, person, Delta P +.78, bbox .81 -> .11
- (c) counterexample, person, Delta P -.98, bbox .02 -> .88

## 7. Layout target

Desired rough pagination:
- Page 1: title/abstract/introduction + method begins.
- Page 2: method/protocol/results; no large blank lower-column region.
- Page 3: Figure 1 + Table 1 + Figure 2/Tables 2–4 + some results text flowing below.
- Page 4: single-column Figure 3 + remaining quantitative diagnostics + conclusion/acknowledgment, with both columns visually balanced.
- Page 5: references only; 15 references are fine even if a little bottom whitespace remains.

Do not use forced pagination merely to make a section start at top. Let floats/text flow naturally where possible.

## 8. Build and QA

After redesign:
- 5 pages, US Letter;
- page 5 references only;
- no undefined citations/refs;
- no overfull boxes;
- no Type 3 fonts;
- all fonts embedded;
- Figure 1/2 vector;
- qualitative image readable at print size;
- visually inspect rendered pages at 100% and ~150–200% zoom, especially pages 3–4.

## 9. Data/provenance source locations

Canonical frozen-tensor reviewer archive is in repository `jovial-liu/cci` on branches including:
- `reviewer-cci-preserving-repair-v1`
- `reviewer-cci-preserving-multisetting-v1`
- `reviewer-identification-round2-v1`

Important files:
- `derived/reviewer_cci_preserving_v1/03_target_preserving_summary.csv`
- `derived/reviewer_cci_preserving_v1/03_failure_transitions.csv`
- `derived/reviewer_cci_preserving_v1/02_prompt_foil_stability.csv`
- `derived/reviewer_cci_preserving_v1/multisetting/04_multisetting_frontier.csv`
- round-2 identification CSV/script for Cross-foil/Absent-only exact CI provenance.

Do not mix settings from a different historical experiment chain merely because they have similar names. In particular, historical LAION/SigLIP or mismatched B/32 summaries should not be merged into the current main claim without a reproduction/provenance gate.

## 10. Final handoff rule

Astra may redesign figures and page flow aggressively, but scientific numbers, formulas, author set, experiment provenance, and claim scope are frozen unless explicitly re-verified against the archived source.
