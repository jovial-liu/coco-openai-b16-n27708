# Canonical data / provenance source map

The manuscript text and tables should remain grounded in the frozen-tensor reviewer audit archives. Use these repositories/branches to verify any number before changing it.

## Core actual-CCI / target-tolerant archive
Repository: `jovial-liu/cci`
Branch: `reviewer-cci-preserving-repair-v1`

Important paths:
- `derived/reviewer_cci_preserving_v1/03_target_preserving_summary.csv` — COCO/OpenAI B/16 epsilon frontier and exact switch-conditioned summary fields.
- `derived/reviewer_cci_preserving_v1/03_target_preserving_bootstrap.csv` — paired bootstrap results.
- `derived/reviewer_cci_preserving_v1/03_failure_transitions.csv` — aggregate/prompt-event sign transitions.
- `derived/reviewer_cci_preserving_v1/02_prompt_foil_stability.csv` — prompt-family hardest-foil stability.
- `derived/reviewer_cci_preserving_v1/01_original_cci_summary.csv` — original CCI audit summary.
- `derived/reviewer_cci_preserving_v1/03_target_preserving_provenance.json` — provenance for the reranking analysis.

## Multi-setting archive
Repository: `jovial-liu/cci`
Branch: `reviewer-cci-preserving-multisetting-v1`

Important path:
- `derived/reviewer_cci_preserving_v1/multisetting/04_multisetting_frontier.csv`

Caution: do not mix a historical/reproduction-mismatched setting into the paper merely because the dataset/model name looks similar. The current paper's four-setting Table 1 values are the frozen manuscript values listed in `ASTRA_MASTER_HANDOFF.md`; any change needs explicit provenance reconciliation.

## Identification controls
Repository: `jovial-liu/cci`
Branch: `reviewer-identification-round2-v1`

The exact Cross-foil and annotation-absent estimates/CIs came from the round-2 identification archive (`round2_identification.csv`) and its old plotting/validation scripts. The current manuscript values are listed explicitly in `ASTRA_MASTER_HANDOFF.md`.

## Provenance rule
LAION direct-reranking results stay excluded from the new main claim because historical text-normalization provenance is unresolved. Do not reintroduce them without passing a reproduction/provenance gate.
