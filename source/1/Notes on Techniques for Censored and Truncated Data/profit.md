# profit

排除掉vscode中遍历的大内存文件

"explorer.fileNesting.patterns": {
        "*.vcf": "$(capture).vcf.gz, $(capture).vcf.gz.csi, $(capture).vcf.gz.tbi",
    },
    "files.watcherExclude": {
        "**/.git/objects/**": true,
        "**/.git/subtree-cache/**": true,
        "**/.hg/store/**": true,
        "/path to file/**": true,
    },