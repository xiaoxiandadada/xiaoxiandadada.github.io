# 处理 plink 文件的压缩

### **推荐方案：分步压缩（优先处理大文件）**
#### 1. **单独压缩超大文件 `ukb_imputed_QC_wb.bed`**
   ```bash
   # 使用 pigz（并行 gzip，需安装）加速压缩（假设已安装）
   pigz -k -v ukb_imputed_QC_wb.bed
   # 如果未安装 pigz，用普通 gzip
   gzip -v ukb_imputed_QC_wb.bed
   ```
   - `-k`：保留原始文件（防止误删）
   - **注意**：`.bed` 文件可能是二进制数据，压缩率可能不高，但可减少传输时间。

#### 2. **打包剩余目录和文件**
   ```bash
   tar -czvf data_copy-yulab-old_remaining.tar.gz genotype main_data ukb_imputed_QC_wb.bim ukb_imputed_QC_wb.fam
   ```
   - 若子目录 `genotype` 和 `main_data` 较小，直接打包即可。

---

### **备选方案：直接压缩整个目录**
#### 1. **使用 `tar` 分卷压缩（适合传输或存储限制）**
   ```bash
   tar -czvf - data_copy-yulab-old | split -d -b 100G - data_copy-yulab-old.tar.gz.part
   ```
   - 分卷为 100GB 的片段（按需调整 `-b 100G`）
   - 解压时合并：`cat data_copy-yulab-old.tar.gz.part* | tar -xzvf -`

#### 2. **仅打包不压缩（快速归档）**
   ```bash
   tar -cvf data_copy-yulab-old.tar data_copy-yulab-old
   ```
   - 不压缩（`-c` + `-v` + `-f`），速度最快，但文件体积不变。

---

### **关键注意事项**
1. **磁盘空间检查**：
   - 执行前用 `df -h` 确认磁盘剩余空间至少是待压缩数据的 1.5 倍。
   - 压缩完成后用 `ls -lh` 检查压缩包大小。

2. **压缩性能优化**：
   - 使用 `pigz` 替代 `gzip`（多线程加速）：
     ```bash
     sudo apt install pigz  # 安装（若未预装）
     tar -cvf - data_copy-yulab-old | pigz > data_copy-yulab-old.tar.gz
     ```

3. **解压命令参考**：
   ```bash
   # 解压 .tar.gz
   tar -xzvf data_copy-yulab-old.tar.gz
   # 解压分卷压缩包
   cat data_copy-yulab-old.tar.gz.part* | tar -xzvf -
   ```