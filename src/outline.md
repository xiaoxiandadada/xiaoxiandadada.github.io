# 快速了解 GWAS 领域需要知道的内容

## 基本概念

### 遗传变异（genetic variation）
- **SNP（单核苷酸多态性）**：单个核苷酸位置上的变异。
- **CNV（拷贝数变异）**：基因组区域的拷贝数变化。
- **插入/缺失变异（Indels）**：基因组中的插入或缺失变异。
- **短串联重复序列（STRs）**：短串联重复序列的变异。

### 表型（phenotype）
- **疾病表型**：如何定义和分类疾病表型，如二元表型（有/无疾病）。
- **性状表型**：如连续性状、定量性状等，如何进行测量和记录。
- **表型的遗传性**：如何估算表型的遗传度，及其在GWAS中的应用。

### 基因型（genotype）
- 个体在其基因组中携带的具体遗传变异形式。例如，对于一个特定的 SNP 位点，基因型可以是 AA、Aa 或 aa，其中 A 和 a 是该位点上的两种可能的等位基因。

## GWAS的目的
- **寻找与特定表型相关的遗传变异**。
- **识别参与疾病发生发展的基因座**。

## 遗传变异的作用机制
- **遗传变异如何影响基因表达和蛋白质功能，从而导致表型的变化**。

## 表型数据

### 疾病表型
- **定义与分类**：如何定义和分类疾病表型，如二元表型（有/无疾病）。
- **数据收集**：如何设计和实施表型数据收集方案。

### 性状表型
- **测量与记录**：如何进行连续性状和定量性状的测量与记录。

### 遗传性估算
- **如何评估表型的遗传度及其在 GWAS 中的应用**。

## 统计方法

### 单变量关联分析
- **t检验、卡方检验、逻辑回归**等基本统计方法。

### 全基因组关联分析
- **全基因组范围内的统计测试**。

### 混合模型
- **用于控制遗传背景和家系关系**。

## 数据准备

### 基因型数据
- **数据格式**：如 PLINK 格式、VCF 格式。
- **质量控制步骤**：SNP 过滤、样本过滤、Hardy-Weinberg 平衡测试等。
- **数据转换**：如何转换不同软件间的数据格式。

### 表型数据
- **收集方案设计**：如何设计和实施表型数据收集方案。
- **数据清洗与标准化**：数据清洗、缺失值处理等。

## 共变量的处理

### 环境因素
- **如何在模型中纳入环境变量**。

### 人口统计学数据
- **调整年龄、性别等因素的影响**。

## 分析方法

### 多重检验校正
- **Bonferroni 校正**：严格的显著性校正方法。
- **FDR 控制**：较为宽松的多重检验校正方法，适用于 GWAS。

### 遗传结构控制
- **PCA（主成分分析）**：用于控制种族混杂的分析方法。
- **LMM（线性混合模型）**：如何同时考虑遗传结构和关联分析。

### 稀有变异分析
- **Burden tests**：用于分析稀有变异的累积效应。
- **SKAT（序列核酸关联测试）**：适用于稀有变异的灵活分析方法。

## 结果解释

### 显著性阈值
- **GWAS 中常用的阈值**：如 5e-8。

### 功能注释
- **将关联 SNP 映射到基因功能**。

### 通路分析
- **识别相关生物通路**。

## 可视化

### 曼哈顿图（Manhattan Plot）
- **展示全基因组的 p 值分布**。

### QQ 图
- **评估统计测试的偏差**。

## 后续分析

### 遗传风险评分（PRS）
- **基于 GWAS 结果计算个体遗传风险**。

### 交互作用分析
- **基因-环境交互作用**：如何检测和解释基因与环境因素的交互作用。
- **基因-基因交互作用**：探索不同基因间的交互效应。

### 验证与复现
- **使用独立样本集验证发现**。
- **Meta 分析**：通过汇总多个研究的结果提高统计效能。