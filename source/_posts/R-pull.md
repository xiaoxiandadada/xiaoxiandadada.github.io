# 提交 R Package

## 提交 R Package 到 CRAN

📎 参考链接：

* [CRAN 提交页面（Checklist 与上传入口）](https://cran.r-project.org/submit.html)
* [CRAN Repository Policy](https://cran.r-project.org/web/packages/policies.html)
* [Writing R Extensions（开发与检查手册）](https://cran.r-project.org/doc/manuals/r-release/R-exts.html)
* [R Packages（Hadley）发布章节](https://r-pkgs.org/release.html)

---
thumbnail: /images/thumbnails/thumb_R-pull.jpg

### 1. 本地检查

在提交前，必须保证包能通过严格的检查：

```r
devtools::document()
devtools::check(document = FALSE)
rcmdcheck::rcmdcheck(args = "--as-cran")
```

要求：**0 ERROR, 0 WARNING, 0 NOTE**（尽量做到）。

---

### 2. 跨平台预检

CRAN 会在不同系统（Windows/macOS/Linux，R-devel/release/oldrel）测试。

* **Win-builder**（Windows 测试）：

```r
devtools::check_win_devel()
devtools::check_win_release()
```

* **R-hub v2**（多平台测试）：

```r
install.packages("rhub")
rhub::rhub_setup()
rhub::check()
```

---

### 3. 提交到 CRAN

* 方法 1：直接在 R 中执行：

```r
devtools::submit_cran()
```

* 方法 2：手动上传：
  进入 [CRAN 提交入口](https://cran.r-project.org/submit.html)，上传 `.tar.gz` 包，并填写 `Submission comments`。

---

### 4. 常见问题

* **无效 URL**：文档里的链接必须可访问。
* **写文件权限**：不能写用户目录，只能写 `tempdir()`。
* **版权和 License**：要在 DESCRIPTION 中明确。
* **示例时间过长**：示例应快速运行，可用 `\dontrun{}` 或 `\donttest{}` 包裹。

---

### 5. 审核与反馈

* 提交后通常 1–3 天会收到 CRAN 邮件（退回/接受）。
* 遇到退回邮件，逐条修改后再提交。

---

## 发布 R Package 到 GitHub 的

📎 参考链接：

* [GitHub Releases 官方文档](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
* [usethis::use\_github 文档](https://usethis.r-lib.org/reference/use_github.html)
* [GitHub Actions for R（r-lib/actions）](https://github.com/r-lib/actions)
* [R Packages（Hadley）GitHub 发布章节](https://r-pkgs.org/release.html#release-github)

---

### 1. 推送代码到 GitHub

在 R 中使用 **usethis** 一键推送：

```r
usethis::use_git()
usethis::use_github()
```

---

### 2. 添加 CI（推荐）

启用 GitHub Actions 来跑 R CMD check：

```r
usethis::use_github_actions()
usethis::use_github_actions_badge()
```

这会在 `.github/workflows/` 下生成 CI 文件，push 后自动运行。

---

### 3. 创建 Release

在 GitHub 仓库页面 → **Releases → Draft a new release**：

1. 选择/新建 Tag（如 `v0.1.0`）；
2. 写版本说明（Changelog）；
3. 可附上构建好的 `.tar.gz` 文件；
4. 点击 **Publish release**。

---

### 4. 用户安装方式

在 README 提供安装方法：

```r
install.packages("remotes")
remotes::install_github("USER/PKG")
```

---

### 5. 更新节奏

* GitHub 不限制提交频率，可以频繁更新。
* 推荐在发布版本时打 tag，并同步更新 NEWS.md 或 Changelog。

