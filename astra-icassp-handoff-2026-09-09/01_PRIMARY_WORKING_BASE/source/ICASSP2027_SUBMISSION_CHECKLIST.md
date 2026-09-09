# ICASSP 2027 CMS transfer checklist - advisor experiment-filled revision

Use the frozen PDF from this package and preserve the manuscript metadata exactly.

## Exact manuscript metadata

**Title**

Beyond Mean Foils: Auditing Worst-Foil Specificity in Frozen CLIP Region Explanations

**Authors - preserve this exact order**

1. Kaixin Liu - equal contribution
2. Zhipeng Ye - equal contribution; corresponding author
3. Feng Jiang
4. Qiufeng Wang

**Affiliations**

1. Taizhou Institute of Science and Technology, Nanjing University of Science and Technology, Taizhou 225300, Jiangsu, China
2. Department of Intelligence Science, Xi'an Jiaotong-Liverpool University, Suzhou 215123, Jiangsu, China

**Affiliation mapping**

- Kaixin Liu: 1
- Zhipeng Ye: 1
- Feng Jiang: 1
- Qiufeng Wang: 2

**Emails in manuscript order**

- 24107880127@nustti.edu.cn
- zhipengye@nustti.edu.cn
- jf@nustti.edu.cn
- qiufeng.wang@xjtlu.edu.cn

**Corresponding author**

Zhipeng Ye - zhipengye@nustti.edu.cn

**Keywords / Index Terms**

CLIP; explainability; interventions; model auditing; worst-foil specificity

## Exact current abstract

A frozen CLIP region explanation can be spatially plausible while a non-target semantic foil responds more strongly than the target. We audit this failure for the actual target-only CCI selector using matched prompt-mean and aggregate worst-foil margins. On COCO/OpenAI B/16, the normalized aggregate margin is -.342, 74.0% of selected regions are negative, and hardest-foil identity has 59.8% mean pairwise agreement across held-out prompt families. A selection-stage target-tolerant reranking at epsilon=.02 switches only 2.0--2.6% of images but improves normalized aggregate margin by .0150/.0108/.0118/.0087 across COCO/VOC and B/16/B/32. All 10,000-resample paired confidence intervals are above zero, whereas held-out target-response intervals include zero. Gains persist with category-disjoint and annotation-absent foils; random and target-only feasible reranking do not explain them. Thus worst-foil debt is reproducible, while repairability is sparse and local within frozen CCI candidate sets, without implying a universally superior rule.

## ORCID - confirm manually in CMS

Do not guess an ORCID from name similarity.

- Kaixin Liu: author confirmation / valid ORCID required.
- Zhipeng Ye: author confirmation / valid ORCID required.
- Feng Jiang: previously cross-checked as `0000-0001-5362-3234`; author should confirm.
- Qiufeng Wang: previously cross-checked as `0000-0002-0918-4606`; author should confirm.

## Final file/content checks

- 5 pages total, US Letter; pages 1-4 contain technical content and page 5 contains references only.
- Final printed bibliography contains exactly 15 cited references (no `\nocite` padding).
- No dedicated Limitations paragraph remains; page-4 space is used for additional experimental analyses.
- Page 5 contains references only.
- No page numbers.
- All fonts embedded; no Type 3 fonts.
- Figure 1 method schematic is vector.
- Figure 2 identification controls are vector.
- Figure 3 is the intended 2200 x 1397 raster qualitative panel and is deliberately smaller than the earlier full-width layout.
- Tables 1-4 are present: main actual-CCI comparison, cross-foil/annotation-absent controls, same-feasible-set baselines, and foil-count sensitivity.
- Author names and order in CMS exactly match the four-author PDF.
- CMS must contain exactly the four authors listed above, in that order.
- Corresponding author: Zhipeng Ye.
- Title, abstract, keywords, and affiliations match the PDF.
- Confirm all four ORCIDs and live 2027 track/EDICS selections.
- Confirm all authors have approved this submitted version.

## Acknowledgment / AI-use disclosure

The paper retains a short funding acknowledgment and a concise disclosure that ChatGPT assisted language/formatting checks and schematic drafting, while experimental data and numerical results were not AI-generated.
