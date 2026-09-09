# Current manuscript metadata / CMS transfer context

**Title**

Beyond Mean Foils: Auditing Worst-Foil Specificity in Frozen CLIP Region Explanations

**Authors — preserve exact order**
1. Kaixin Liu — equal contribution
2. Zhipeng Ye — equal contribution; corresponding author
3. Feng Jiang
4. Qiufeng Wang

Do not restore Jinye Li.

**Affiliations**
1. Taizhou Institute of Science and Technology, Nanjing University of Science and Technology, Taizhou 225300, Jiangsu, China
2. Department of Intelligence Science, Xi'an Jiaotong-Liverpool University, Suzhou 215123, Jiangsu, China

**Mapping**
- Kaixin Liu: 1
- Zhipeng Ye: 1
- Feng Jiang: 1
- Qiufeng Wang: 2

**Emails**
- 24107880127@nustti.edu.cn
- zhipengye@nustti.edu.cn
- jf@nustti.edu.cn
- qiufeng.wang@xjtlu.edu.cn

**Corresponding author**
Zhipeng Ye — zhipengye@nustti.edu.cn

**Keywords**
CLIP; explainability; interventions; model auditing; worst-foil specificity

**Current abstract**

A frozen CLIP region explanation can be spatially plausible while a non-target semantic foil responds more strongly than the target. We audit this failure for the actual target-only CCI selector using matched prompt-mean and aggregate worst-foil margins. On COCO/OpenAI B/16, the normalized aggregate margin is -.342, 74.0% of selected regions are negative, and hardest-foil identity has 59.8% mean pairwise agreement across held-out prompt families. A selection-stage target-tolerant reranking at epsilon=.02 switches only 2.0--2.6% of images but improves normalized aggregate margin by .0150/.0108/.0118/.0087 across COCO/VOC and B/16/B/32. All 10,000-resample paired confidence intervals are above zero, whereas held-out target-response intervals include zero. Gains persist with category-disjoint and annotation-absent foils; random and target-only feasible reranking do not explain them. Thus worst-foil debt is reproducible, while repairability is sparse and local within frozen CCI candidate sets, without implying a universally superior rule.

**ORCID**
Do not infer from names. Authors should confirm all ORCIDs in the submission system.
