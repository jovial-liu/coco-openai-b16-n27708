# Version map

## `current_latex/`
Newest text/data integration and latest QA. Use as the primary manuscript content source. Its newest Figure 1/2 visual redesign was rejected by the user, so do not treat those SVGs as the desired style.

## Rebalanced source / older visual references
Use the rebalanced source and older SVGs as the safer visual/layout comparison base. The most useful assets are:
- older/rebalanced method SVGs;
- intermediate combined Figure 1 SVG;
- earlier identification-control forest plot SVG;
- wide/compact qualitative-case images.

## `svg_versions/`
- `figure1_OLD_reference.svg`: older method reference already on this branch.
- `figure1_LATEST_rejected.svg`: latest redraw; content reference only, not a style target.
- `figure2_LATEST_rejected.svg`: latest identification redraw; likewise not a style target.

Additional exact SVGs are being handed off separately/directly where necessary, including `figure1_full_vector_redraw_v5.svg` and `figure1_combined_editable.svg`.

## Rule
Do not blindly merge source trees. Use CURRENT for text/data, REBALANCED/HISTORY for layout and figure design cues.
