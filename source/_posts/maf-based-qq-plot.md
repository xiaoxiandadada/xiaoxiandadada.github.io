---
title: MAF-based QQ Plot
date: 2024-12-06
---

# MAF-Based QQ Plot

做GWAS的过程中会发现用R包 `qqnorm（）` 画QQ 图有点 unattractive，因此可以尝试画分类的 QQ 图。

## 根据 MAF 的数值分类

- ### 示例代码

可以通过将数据按 MAF 值分成数量相等的四个区间来实现分类，可以使用 在`quantile()` 函数来确定 MAF 值的分位数区间，然后将数据分配到这四个区间中。

```r
# 加载必要的包
library(dplyr)
library(ggplot2)

# 读取数据
df <- read.table("C:/Users/xiaox/Documents/UKB处理/step 3文件/sampled_lines.txt", header = TRUE)

# 计算 MAF 值的四个分位数
maf_quantiles <- quantile(df$AF_Allele2, probs = c(0, 0.25, 0.5, 0.75, 1))

# 使用 cut() 函数将 MAF 划分为四个区间
df$MAF_class <- cut(df$AF_Allele2, breaks = maf_quantiles, include.lowest = TRUE,
                    labels = c("Q1", "Q2", "Q3", "Q4"))

# 查看 MAF 分类结果
table(df$MAF_class)

# 输出 MAF 值的四个分位数
maf_quantiles

# 输出每个区间的 MAF 值范围
cat("Q1 (Lowest 25%):", maf_quantiles[1], "to", maf_quantiles[2], "\n")
cat("Q2 (25%-50%):", maf_quantiles[2], "to", maf_quantiles[3], "\n")
cat("Q3 (50%-75%):", maf_quantiles[3], "to", maf_quantiles[4], "\n")
cat("Q4 (Highest 25%):", maf_quantiles[4], "to", maf_quantiles[5], "\n")

```

- ### 示例输出

```r
> table(df$MAF_class)
   Q1  Q2  Q3  Q4 
  250 250 250 250 
> maf_quantiles
0%          25%          50%          75%         100% 
0.0001     0.0004      0.0050       0.0778       0.4991 

> # 输出每个区间的 MAF 值范围
Q1 (Lowest 25%): 0.0001 to 0.0004 
Q2 (25%-50%): 0.0004 to 0.0050 
Q3 (50%-75%): 0.0050 to 0.0778 
Q4 (Highest 25%): 0.0778 to 0.4991
```