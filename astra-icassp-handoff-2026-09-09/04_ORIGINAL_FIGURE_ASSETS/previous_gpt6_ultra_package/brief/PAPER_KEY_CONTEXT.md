# Paper context for Figure 1 redesign

Paper: **Beyond Mean Foils: Auditing Worst-Foil Specificity in Frozen CLIP Region Explanations**.

## Core selection / audit definitions

For region R and concept prompt c:

`d_R(c) = s_m(x,c) - s_m(I(x,R),c)`.

Original CCI selects only by the selection-stage target response:

`R_CCI = argmax_{R in R(x)} d_R^sel(t)`.

Selection-stage worst-foil margin:

`M^sel(R,t) = d_R^sel(t) - max_f d_R^sel(f)`.

With fixed epsilon = 0.02, form the target-tolerant feasible set:

`R_epsilon = {R : d_R^sel(t) >= d_R_CCI^sel(t) - epsilon}`.

Then rerank only inside that feasible set:

`R_WF(epsilon) = argmax_{R in R_epsilon} M^sel(R,t)`.

**Critical protocol point:** Eq. 6 reads only selection-stage tensors. Held-out prompts are used only after the region is fixed. Do not depict any feedback arrow from held-out evaluation back into selection.

## Held-out audit

Held-out evaluation uses three prompt families. Report separately:

- worst-foil specificity (`P_max^agg` / `P_max^pm`)
- held-out target response
- spatial locality / bbox precision

`P_max` is ontology-relative, not a human semantic ground-truth score and not a standalone explanation-quality score.

## Main claim the right-hand evidence panel must support

The gain is not merely selector-endpoint reuse. Category-disjoint cross-foil selection/evaluation remains positive in all four OpenAI settings; annotation-absent evaluation also remains positive.

Cross-foil normalized aggregate gains:

- COCO B/16: +0.01052 [0.00901, 0.01198]
- COCO B/32: +0.00728 [0.00629, 0.00846]
- VOC B/16: +0.00705 [0.00296, 0.01140]
- VOC B/32: +0.00438 [0.00131, 0.00784]

Annotation-absent point estimates:

- COCO B/16: +0.00939
- COCO B/32: +0.00697
- VOC B/16: +0.00809
- VOC B/32: +0.00443

Paper states all paired annotation-absent CIs are above zero, but the exact endpoints are not printed in the prose. Do **not** invent those endpoints; use the old plot only as visual reference unless exact archived values are recovered.

## Full-foil Table 1 values

- COCO B/16: +0.0150 [0.0131, 0.0169]
- COCO B/32: +0.0108 [0.00945, 0.0122]
- VOC B/16: +0.0118 [0.00677, 0.0183]
- VOC B/32: +0.00867 [0.00441, 0.0143]

## Important caveat for the schematic

Do not label the general transition as `Negative -> Less negative`. VOC baseline aggregate margins are positive (`P_CCI = +0.168/+0.186`). Use neutral language such as `lower margin -> improved margin`, or omit that micro-panel entirely.
