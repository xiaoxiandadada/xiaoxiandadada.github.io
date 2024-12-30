# Configuring Pytorch Environment in macOS

这里我没有用推荐的Python 3.9 版本配置torch环境，而是用了最新的python 3.12 版本，后续有使用问题再更新。

## Step 1: 下载conda 

去清华镜像源下载：
- <https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/>

这里就直接下载最新的版本 Miniconda3-latest-MacOSX-arm64.pkg,在 mac 中双击就可以直接安装。

安装好后，在终端输入 `conda info --env` 可以查看是否有 base 环境。

## Step 2: 创建新的 Conda 环境

**1、创建新环境：** 使用 `conda create` 命令创建一个新的环境，并指定 Python 3.12

```bash
conda create -n pytorch_env python=3.12
```
**2、激活新环境：** 

```bash
conda activate pytorch_env
```

## Step 3: 安装 PyTorch

**1、 安装 CPU 版本的 PyTorch**

```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

**2、为 Apple Silicon 安装 PyTorch**

对于 Apple Silicon（M1/M2 芯片），目前没有官方的 CUDA 支持，但 PyTorch 提供了针对 Apple Silicon 优化的版本。您可以直接安装这些版本，它们通常标记为 `apple` 或 `arm64` 架构。

```bash
conda install pytorch torchvision torchaudio -c pytorch -c apple
```
## Step 4: 验证安装
在终端输入 `python` ，运行一些简单的 PyTorch 代码来验证安装是否成功：

### input

```python
import torch

print(torch.__version__)
print(torch.backends.mps.is_available())  
# 如果有 Metal Performance Shaders 支持，这应该返回 True
x = torch.rand(5, 3)
print(x)
```
### output

```python
>>> print(torch.__version__)
2.4.1
>>> print(torch.backends.mps.is_available())  
True
>>> x = torch.rand(5, 3)
>>> print(x)
tensor([[0.0688, 0.9942, 0.5581],
        [0.2363, 0.1216, 0.6837],
        [0.8435, 0.1174, 0.1823],
        [0.1920, 0.7750, 0.8696],
        [0.3480, 0.8162, 0.7248]])
```

这样就安装好啦，yep！

