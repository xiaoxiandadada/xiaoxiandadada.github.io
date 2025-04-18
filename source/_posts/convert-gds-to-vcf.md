---
title: Convert GDS Format to VCF Format
date: 2024-12-06
---

a. 创建下载目录（可选）
为了组织文件，建议在下载前创建一个专门的目录：

b. 使用 wget 下载未压缩的 FASTA 文件
直接下载未压缩的 FASTA 文件，然后使用 bgzip 进行压缩。

注意：尽管 UCSC 提供的是 .fa.gz 格式，但这是标准的 gzip 压缩文件。为了与 samtools faidx 兼容，需重新使用 bgzip 压缩。

如果下载过程中出现中断，可以使用 -c 选项继续下载：

c. 验证下载文件的完整性
检查下载的文件大小是否接近 1.4 GB。

如果文件大小仍然较小（如 926M），可能下载过程中仍存在问题。此时，可以尝试以下方法：

更换下载镜像：尝试从其他镜像站点下载。
检查网络连接：确保下载过程中网络连接稳定。
使用下载管理工具：如 aria2，支持多线程下载，提高下载稳定性。
d. 解压并使用 bgzip 重新压缩
确保已安装 bgzip。通常，bgzip 随 htslib 或 samtools 一起安装。如果未安装，可以使用 Conda 安装：

然后，解压并使用 bgzip 重新压缩：

e. 为重新压缩的文件建立索引
使用 samtools faidx 为 bgzip 压缩的文件建立索引：

这将生成 hg19.fa.gz.fai 索引文件。

f. 验证索引文件
确认索引文件已正确生成：