# pruning

在遗传学研究中，识别并移除高度相关的个体的过程通常被称为“pruning” ([与clumping区别](pruning&clumping.md)) 。这种做法的目的在于减少由于个体间亲缘关系导致的数据冗余，从而提高统计分析的准确性和可靠性。在实际操作中，修剪通常可以在计算GRM之前完成，以确保用于构建GRM的数据集是清洁且独立的。

## 为什么在计算GRM之前进行pruning？

**1\.减少数据冗余：** 通过修剪，可以去除那些遗传上高度相关的个体，从而减少数据集中的冗余信息。这对于后续的统计分析，如GWAS（全基因组关联研究）或群体遗传学分析，尤其是在进行多因素分析或复杂性状的研究时更为重要。

**2\.提高计算效率：** 较少的个体意味着更小的GRM矩阵，这会减少计算量和内存消耗，使得计算过程更加高效。

**3\.避免假阳性结果：** 如果样本之间存在较强的遗传相关性，那么在进行GWAS时可能会出现假阳性关联，即检测到实际上不存在的关联信号。通过修剪，可以减少这类误差的发生概率。

## 如何进行pruning?

以下是使用Plink在计算GRM之前进行修剪的一个具体步骤示例：

### 步骤1：识别独立个体

使用Plink的 `--indep-pairwise` 命令来识别个体间的遗传独立性，并将结果保存在一个文件中。这里我们使用参数（50 5 0.2）来指定窗口大小、移动步长和相关系数阈值。

````bash
plink --bfile example_data \
      --indep-pairwise 50 5 0.2 \
      --out example_indep
````

这会生成一个名为example_indep.prune.in的文件，其中列出了独立个体的ID。

### 步骤2：提取独立个体
根据example_indep.prune.in文件来提取独立个体的数据，并生成一个新的BED/BIM/FAM文件组合。

````bash
plink --bfile example_data \
      --extract example_indep.prune.in \
      --make-bed \
      --out example_indep_pruned
````

这会产生一个新的数据集example_indep_pruned，其中只包含那些被认定为独立的个体。

### 步骤3：计算GRM
使用修剪后的数据集来计算GRM。

````bash
plink --bfile example_indep_pruned \
      --make-grm-gz \
      --out example_grm_pruned
````

这会生成一个压缩的GRM矩阵文件 example_grm_pruned.grm.gz，以及一个包含样本ID信息的文件 example_grm_pruned.grm.id 。

通过在计算GRM之前进行修剪（pruning），可以确保用于构建GRM的数据集是清洁且独立的。这样做不仅提高了计算效率，还增强了统计分析的准确性和结果的可靠性。具体步骤包括识别独立个体、提取这些个体的数据以及使用修剪后的数据集来计算GRM。这种方法广泛应用于各种遗传学研究中，尤其是在需要考虑个体间遗传相关性的情况下。

***
### Relate to:

[pruning and clumping](./pruning&clumping.md)