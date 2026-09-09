# Added-experiment provenance

All quantitative additions use the same frozen-candidate OpenAI CLIP audit chain as
the main results; no new model forward pass is claimed.

Table 7 reports exact archived COCO/OpenAI B/16 statistics at epsilon=.02:
- switched images: 663 / 27,708 (2.39%)
- improving switches: 611 / 663 (92.2%)
- mean / median switched-image aggregate margin gain: +0.625624 / +0.406
- mean held-out target-response delta: +0.002180835
- mean bbox-precision delta: -0.0494958

The earlier cross-setting table of conditional values inferred from rounded Table 1
entries was removed, eliminating the possible +.626 versus approx +.628 presentation
mismatch.
