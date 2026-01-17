---
title: awk
date: 2026-01-15 15:35:40
thumbnail: /images/thumbnails/thumb_use-awk.jpg
categories: [DL-notes]
---
# awk

```bash
awk options 'pattern {action}' file
```


- **options**：是一些选项，用于控制 awk 的行为。
- **pattern**：是用于匹配输入数据的模式。如果省略，则 awk 将对所有行进行操作。
- **{action}**：是在匹配到模式的行上执行的动作。如果省略，则默认动作是打印整行。

## options description 
- -F <分隔符> 或 --field-separator=<分隔符>： 指定输入字段的分隔符，默认是空格。使用这个选项可以指定不同于默认分隔符的字段分隔符。

- -v <变量名>=<值>： 设置 awk 内部的变量值。可以使用该选项将外部值传递给 awk 脚本中的变量。

- -f <脚本文件>： 指定一个包含 awk 

- -V 或 --version： 显示 awk 的版本信息。

- -h 或 --help： 显示 awk 的帮助信息，包括选项和用法示例。

## Examples
打印整行：
```bash
awk '{print}' file
```

打印特定列：
```bash
awk '{print $1, $2}' file
```

使用分隔符指定列：
```bash
awk -F',' '{print $1, $2}' file
```

打印行数：
```bash
awk '{print NR, $0}' file
```

打印行数满足条件的行：
```bash
awk '/pattern/ {print NR, $0}' file
```

计算列的总和：
```bash
awk '{sum += $1} END {print sum}' file
```

打印最大值：
```bash
awk 'max < $1 {max = $1} END {print max}' file
```

格式化输出：
```bash
awk '{printf "%-10s %-10s\n", $1, $2}' file
```

### 筛选出p值小于5×10⁻⁸的行，假设文件名是data.txt

读取文件data.txt，并筛选出第13列（即p.value列）小于5×10⁻⁸的行
```bash
awk '$13 < 5e-8' data.txt
```
`NR==1` 部分确保标题行保留，`$13 < 5e-8` 部分筛选p值小于5×10⁻⁸的行
```bash
awk 'NR==1 || $13 < 5e-8' data.txt
```

用 `>` 输出筛选出的行数
```bash
awk 'NR==1 || $13 < 5e-8' data.txt > significant_data.txt
```

`wc -l` 统计显著位点个数
```bash
wc -l significant_p_snps.txt
```

还可以用 `-v` 定义一个变量 `threshold`
```bash
awk -v threshold=0.05 '$13 <= threshold {print}' data.txt
```

使用 `>>` 追加信息，不覆盖之前的文件
```bash
awk -v threshold=0.05 '$10 <= threshold' data.txt | wc -l 
>> significant_data.txt
```

### Refer to:

- <https://www.runoob.com/linux/linux-comm-awk.html>
