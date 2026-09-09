# Binary / exact assets to upload alongside the GitHub handoff

The GitHub connector used for this handoff can write text/SVG files but cannot directly push the local binary PDF/PNG assets. Upload these exact files into the Astra chat together with the GitHub branch link.

## Required

1. `liu_icassp2027_final_typography.pdf`
   - current compiled manuscript used as the latest visual/text reference
   - SHA-256: `49d23a5fab1c5bbbe25da15177f4b9d5d3026c91f66a15ea53fc5b0af3d964e2`

2. `qualitative_cases_compact_labels.png`
   - exact qualitative Figure 3 image referenced by the latest current LaTeX
   - 1780 x 1185 PNG
   - SHA-256: `9fe7d145353e1a8fe420496ca53cfc802aa72df68788d3312836c1bf06f5c727`

## Strongly recommended visual references

3. `figure1_full_vector_redraw_v5.svg`
   - important older method SVG / visual reference
   - SHA-256: `03c08522ebbd3879f72c1d335d3bb510e2cfbdbcbe78248d690307924ad5cc82`

4. `figure1_combined_editable.svg`
   - intermediate combined Figure 1 / identification-control vector reference
   - SHA-256: `e1d62573400c6390c093a5c171e2c054349e3e4024071086742b922946306b75`

5. `figure1_combined.svg`
   - another intermediate combined vector version
   - SHA-256: `e9a22f4c5222d963f142a0686755ea85664694ea92eb910a5a4b92ed62d79bd5`

6. `liu_icassp2027_layout_rebalanced.pdf`
   - earlier visually safer/rebalanced paper version for side-by-side layout comparison
   - SHA-256: `be69230e1b3f3a3ab092e1b96f44bab57c4185f497d57a7349b7d8b1274d2291`

Astra should use the GitHub `current_latex/main.tex` as the newest text/data source, but compare these older vector/layout assets when redesigning the figures and page flow.
