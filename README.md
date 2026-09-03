# coco_openai_b16_n27708 — ChatGPT 可读版数据集

COCO 2014（val）上的 CLIP ViT-B/16 视觉概念编辑数据集，共 **27,708 个样本**、**8 个聚类**、**196 个 patch**（14×14 网格）。

本仓库是**为 ChatGPT（GitHub 插件）直接读取而整理的文本版**：全部文件为 JSON / JSONL 纯文本，单个文件均 <1MB，ChatGPT 可直接读取内容。原始二进制 `.pt` 张量（PyTorch）保存在本地，未上传（二进制文件 ChatGPT 无法读取内容；如需作为备份上传可另行处理）。

## 仓库结构

```
README.md                     本说明
dataset_info.json             数据集顶层信息（类别、prompt、聚类数等）
cluster_masks_summary.json    聚类掩码汇总（每聚类 × 196 patch 的掩码频率）
chunks_index.json             嵌入块结构说明 + 全局统计 + 记录示例
chunks_map/chunks_XXXX-XXXX.jsonl   chunk → 样本索引映射（4 个分片）
metadata/samples_00000-27707.jsonl  每个样本的元数据（28 个分片，每片 1000 条）
folds/foil_folds_00000-27707.jsonl  评测折分配（28 个分片，每片 1000 条）
```

## 字段说明

### dataset_info.json
- `dataset`: coco；`samples`: 27708；`clusters`: 8；`patches`: 196
- `category_ids` / `category_names` / `category_families`：80 个 COCO 类别的 ID、名称、语义族
- `category_fold`：每个类别所属的评测折
- `selection_prompt`：选择阶段模板 `a photo of a {category}`
- `evaluation_prompts`：评测阶段模板（3 条）

### metadata/*.jsonl（每行一个样本）
- `image_id`、`path`（原图路径）、`width` / `height`
- `target_id` / `target_name` / `target_boxes`：目标对象（编辑主体）及边界框
- `distractor_id` / `distractor_name` / `distractor_ids` / `distractor_boxes`：干扰对象（foil）及边界框

### folds/*.jsonl（每行一个样本）
- `sample`：样本索引（与 metadata 对齐）
- `fold0_categories` / `fold1_categories`：两个评测折各自的训练类别集合（只列 True 的类别 ID，未列出的为 False）

### cluster_masks_summary.json
- 原始张量 `[27708, 8, 196]`（bool，每样本 × 8 聚类 × 196 patch 掩码）
- 此处提供压缩可读形式：`patch_mask_frequency_per_cluster`（每聚类每 patch 被掩码的样本占比）与每聚类整体掩码比例

### chunks_index.json + chunks_map/*.jsonl
- 原始 `chunks/chunk_*.pt`（3464 个）为 PyTorch 保存的 drop 扰动权重张量，二进制、总 284MB，未转文本
- `chunks_index.json`：字段形状/类型/全局统计（min/max/mean/std）
- `chunks_map`：每个 chunk 覆盖的样本索引区间（`sample_indices`）

## 给 ChatGPT 的提示

可直接让 ChatGPT 读取 `dataset_info.json` 了解全局，再按需读取 `metadata/` 与 `folds/` 的任意分片；`cluster_masks_summary.json` 和 `chunks_index.json` 提供张量数据摘要。

## 数据来源与校验

- 全部 63 个文件经 `jq -e .` 与 Python `json.loads` 双重校验通过
- 文本内容由原始 `metadata.json`、`foil_folds.pt`、`cluster_masks.pt` 转换，样本顺序与原始数据一致
