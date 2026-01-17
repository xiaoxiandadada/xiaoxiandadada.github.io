---
title: use torch in Jupyter Notebook
date: 2026-01-15 15:35:40
thumbnail: /images/thumbnails/thumb_use-torch-in-jupyter.jpg
categories: [DL-notes]
---
# use torch in Jupyter Notebook

在搭好pytorch的环境后，希望能够在 Jupyter Notebook 里面尝试运行一下，但选择 Python 内核的时候有一些疑问，似乎选择conda内置的 python 环境并不 work，然后探索了一下, 可以给 Jupyter Notebook 添加内核(as a kernel)

**1、查看torch：** 

这里仍然先查看一下 conda 环境,确定一下torch的环境名称

``` bash
conda info --env

# conda environments:
#
base                  *  /opt/miniconda3
pytorch_env              /opt/miniconda3/envs/pytorch_env
```

**2、激活torch：** 

``` bash
conda activate pytorch_env
```

**3、安装ipykernel：** 

在 pytorch_env 这个环境中安装 ipykernel, 这里也直接用conda 装了

``` bash
conda install ipykernel
```

**4、把环境加入 Jupyter kernels：** 

``` bash 
python -m ipykernel install --user --name pytorch_env --display-name "Python (pytorch_env)"
```

简单解释一下：

- `python -m ipykernel install`:

  - `-m` 参数是 Python 命令的一部分，用来运行指定模块 (ipykernel) 中的代码。这里的 ipykernel 模块是 Jupyter 使用的内核模块，用于处理 Notebook 中的 Python 代码执行。

  - `install` 命令则是安装并注册一个新的 Jupyter kernel。

- `--user`: 
    - 这个选项表示将内核安装到当前用户的目录中，而不是系统目录。这可以避免需要管理员权限，且每个用户可以拥有独立的内核。
- `--name pytorch_env`:
    - 这个选项为内核指定一个名字。在这个例子中，内核名称是 pytorch_env，它与 Conda 环境的名字一致。这个名字是用于 Jupyter 内部识别的，类似于一个 ID。
- `--display-name "Python (pytorch_env)"`:
    - 这个选项是你在 Jupyter Notebook 中看到的内核显示名称。在 Jupyter 的内核选择器中，内核会显示为 Python (pytorch_env)，帮助识别它。

**5、测试一下**

下面可以打开 Jupyter Notebook 测试一下

``` python
import torch

# 测试 torch 是否正常工作
print(torch.__version__)
```

