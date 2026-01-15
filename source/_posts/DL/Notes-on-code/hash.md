---
title: hashlib
date: 2026-01-15 15:35:40
categories: [DL-notes]
---
# hashlib

# hashlib —— 安全哈希与消息摘要库

> 本文档面向 Python 开发者，介绍标准库 `hashlib` 的核心概念、常见算法、典型用法及注意事项，并给出可直接运行的代码示例。

---

## 1 概述

- **作用**：为字符串或字节数据生成**固定长度**的哈希值（散列值、摘要）。  
- **算法**：支持 SHA-1、SHA-224/256/384/512、BLAKE2b/2s、MD5、SHAKE 等。  
- **用途**：文件完整性校验、口令加盐存储、缓存键生成、数字签名前置步骤等。

> ⚠️ 警告：MD5、SHA-1 已被证实存在碰撞风险，**绝不可用于密码学安全场景**（如数字签名、SSL），仅做完整性校验或缓存键即可。

---

## 2 快速上手

### 2.1 单次哈希（一次性读入内存）

```python
import hashlib

data = b"hello world"
digest = hashlib.sha256(data).hexdigest()
print(digest)          # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```

### 2.2 缓存键生成（PyTorch ImageFolder 场景）

```python
import hashlib
import os

def _get_cache_path(root: str) -> str:
    h = hashlib.sha1(root.encode()).hexdigest()
    path = os.path.join("~", ".torch", "vision", "datasets", "imagefolder", f"{h[:10]}.pt")
    return os.path.expanduser(path)

print(_get_cache_path("py_file"))
# -> b2697cb545.pt
```