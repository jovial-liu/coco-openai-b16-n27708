# Added experiment/data provenance

This revision fills previously unused technical-page space with **existing archived results only**. No model forward, new data collection, or post-hoc hyperparameter search was run for this revision.

## 1. Predeclared epsilon frontier (Table 5)

Source artifact:
- Repository: `jovial-liu/cci`
- Branch: `reviewer-cci-preserving-repair-v1`
- Generating commit: `30099a19c4c2b546d6270b04062d1f4a61ae7e3f`
- File: `derived/reviewer_cci_preserving_v1/03_target_preserving_summary.csv`

The archived audit declares the grid `epsilon = {0, .01, .02, .05, .10, .20}` before analysis. Table 5 reports full-sample point estimates for switch rate, normalized aggregate worst-foil gain, held-out target-response delta, bbox-precision delta, and aggregate negative-margin rate. The manuscript continues to use `epsilon=.02` as the fixed main operating point; its inferential CIs remain the 10,000-resample values in Table 1. The auxiliary archived frontier used 1,000 paired bootstrap draws for QA, but Table 5 does not report those auxiliary CIs.

## 2. Failure-transition diagnostic at epsilon=.02

Source artifact:
- Same repository / branch / generating commit as above.
- File: `derived/reviewer_cci_preserving_v1/03_failure_transitions.csv`

For COCO/OpenAI B/16 at `epsilon=.02`, the aggregate sign-transition counts are 42 fail-to-pass and 0 pass-to-fail, corresponding to a 0.1516 percentage-point net negative-margin-rate reduction. At the held-out prompt-event level, the counts are 128 fail-to-pass and 3 pass-to-fail. These values are used to explain why mean margin gains can be substantial on switched cases while the binary failure rate changes only slightly.

## 3. Existing results retained

All previously reported main, cross-foil, annotation-absent, matched-count, prompt-stability, switch-conditioned, locality, and bootstrap-seed results are unchanged. No numerical value in Tables 1--4 or Figures 1--3 was altered by this revision.

## 4. Switch-conditioned repair accounting (Table 7)

Source artifacts:
- Repository: `jovial-liu/cci`
- Branch: `reviewer-cci-preserving-repair-v1`
- Generating commit: `30099a19c4c2b546d6270b04062d1f4a61ae7e3f`
- Files: `derived/reviewer_cci_preserving_v1/03_target_preserving_summary.csv`,
  `derived/reviewer_cci_preserving_v1/03_target_preserving_per_sample.csv`, and
  `derived/reviewer_cci_preserving_v1/03_failure_transitions.csv`.

At `epsilon=.02`, the archived summary gives 663 switches among 27,708 images,
mean switched-image aggregate margin change `+0.6256239282`, switched-image
improvement probability `0.9215686275`, mean switched-image target-response
change `+0.0021808350`, and mean switched-image bbox-precision change
`-0.0494958015`. Thus 611 of 663 switched images improve. The manuscript's
previously reported switched-image median aggregate change is `+0.406`. The
identity `0.0239281074 x 0.6256239282 = 0.0149699966` recovers the archived
full-sample aggregate gain and is an arithmetic decomposition, not a new
experiment. Transition counts remain reported in Table 5 rather than duplicated
in Table 7.

## Cross-setting repair concentration table (layout-rebalanced revision)
Table 7 is an algebraic re-expression of the already reported Table 1 values, not a new experiment. For each setting, the displayed conditional value is approximately the displayed full-sample delta divided by the displayed switch rate. The approximation symbol is retained because Table 1 values are rounded for print. The identity is justified because unchanged selections contribute zero selector delta.
