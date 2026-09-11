# Pre-submission revision: items 1, 3, 4, 5, 6

Item 2 was explicitly excluded by the user; this pass does not certify that
the manuscript satisfies every conference policy.

## Changes

1. Enlarged ordinary Figure 1/2/3 labels to at least 9 pt at the actual inclusion
   widths. Simplified long labels; preserved soft colors and vector text.
   Mathematical scripts retain conventional smaller sizes, as in the body.
3. Added target selection, image eligibility, full-foil ontology, alternating
   category folds, and within-image pooling before bootstrap. Clarified base
   versus setting/metric-specific bootstrap seeds.
4. Replaced ambiguous semantic-family wording with **all-three** agreement.
   53.69% is unchanged and must be compared to 46.36% all-three exact ID,
   not 59.80% mean pairwise exact ID. Families are frozen metadata categories.
5. Removed duplicate foil-count, sparse-switching, tolerance and concentrated
   repair explanations; retained all six tables and their experimental values.
6. Defined qualitative delta as normalized aggregate gain; described archived
   rule selection rather than implying random/representative sampling. Replaced
   “Predeclared” with “Tolerance sensitivity”. Explicitly stated that CIs
   containing zero do not establish equivalence/no loss. Explained precision
   differences and changed rounded arithmetic equality to approximation.

## Source checks

Authenticated repository files read from branch `reviewer-identification-round2-v1`
of `jovial-liu/cci`:

- `code/run_coco_bbox_specificity_audit.py`: select_samples / select_voc_samples
  choose the largest-area annotated instance; require a distinct category and
  area fraction [.02,.8]. COCO excludes crowd annotations. VOC uses box area.
- `code/run_coco_cci_specificity_audit.py`: full category mask excludes target.
- `code/run_reviewer_identification_round2.py`: make_identity_split alternates
  permuted categories into two folds; summarize_cross_direction averages the
  seed/direction deltas within image, then bootstraps unique images. metric_seed
  deterministically offsets the base seed for settings/metrics.
- Its qualitative_examples function and the supplied 15_qualitative_examples.csv
  confirm Figure 3 image IDs 440528, 191096, 343978 and normalized aggregate gains
  4.576487660641386, .783033091096189, -.9771392535347265. These are archived
  examples 05, 02 and 06; no cases or photographic pixels were replaced.
- Supplied PROMPT_STABILITY_FOR_PAPER.csv contains all_three_family =
  .53688465425147969 and all_three_exact = .46358452432510461.

Copies of the consulted scripts/metadata and CSVs are in source/provenance/.
They are evidence records, not a complete runnable experiment environment.

Six-author order (Xihang Zhou added last on 2026-09-10), IDEA reference and original displayed equation environments
are retained. All table numeric entries and identification CSV bytes remain
unchanged. Validation checks five pages, references on page 5, embedded figure
text bounds, minimum ordinary SVG label size, and unchanged Figure 3 image pixels.
