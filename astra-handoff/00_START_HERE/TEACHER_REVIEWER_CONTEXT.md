# Teacher / reviewer context distilled from the revision process

## Teacher-driven layout requests
- Remove Jinye Li from the author list.
- Remove unnecessary image-adjacent prose and the standalone ethics/limitation-style blocks that waste space.
- Do not keep a `Limitations` section.
- Reference list should be about 10–15 items rather than 27; current target is 15.
- Add more method/experiment substance instead of leaving half-page blank regions.
- Qualitative examples previously occupied too much space; keep them compact and preferably one column.
- Add/use the method SVG as a proper paper figure, but make it academic rather than AI/PPT-like.
- First four pages should look full; do not force section starts that create large blank areas.
- User expects actual visual inspection after compilation, not just a LaTeX warning check.

## Reviewer-facing risks to defend
- Is held-out evaluation leaking into selection?
- Is worst-foil max a trivial operator with no real contribution?
- Is the gain only selector–endpoint reuse?
- Is the result only an extreme-value/foil-count effect?
- Is specificity purchased by target-response or locality damage?
- Is a ~2% switch rate meaningful?
- Are historical LAION results compatible/provenance-valid?

## Desired answer embedded in the paper
- Region is fixed before held-out evaluation; selection-stage tensors only.
- Cross-foil + annotation-absent + matched-count controls survive.
- Same-feasible-set random/target-only/mean baselines do not explain the effect.
- Continuous margin improvement can be substantial while binary failure-rate changes are small because many switches reduce debt without crossing zero.
- Target response and locality are separate endpoints; qualitative counterexample prevents a per-image dominance claim.
- LAION is excluded from new direct-reranking claims because provenance is unresolved.
