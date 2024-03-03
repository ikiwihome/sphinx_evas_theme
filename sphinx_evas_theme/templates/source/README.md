# 中文技术文档写作风格指南

网页浏览地址：<https://zh-doc-guide.readthedocs.io/zh-cn/latest/>

本仓库存储的是《中文技术文档写作风格指南》的源文件，欢迎任何人进行贡献！

## 如何使用

### 文件目录说明

```
│
├───docs                        # 工程文档和配置脚本文件夹，install和make脚本都在这里
│   │
│   └───source                  # 工程文档存放文件夹
│       │
│       ├─────_static           # 文档自定义的html样式，默认空
│       │
│       ├─────_templates        # 文档自定义的html页面元素，默认空
│       │
│       ├─────conf.py           # sphinx的配置文件
│       │
│       └─────index.rst         # 文档目录文件，必须有，否则报错
│
└───env                         # windows python本地环境文件夹，双击install.bat会解压python环境
    │
    ├───_static                 # html样式css和js文件夹
    │
    ├───_templates              # html页面模板文件夹
    │
    └───latex_templates         # latex样式模板(生成pdf的样式)
        │
        └───fonts               # pdf字体文件夹
```

项目采用三级文件夹结构，第一级为操作系统级环境(包含了readthedocs的构建脚本以及windows本地python环境)，第二级为项目级脚本(例如install, makefile以及html/pdf主题样式)，一般无需修改，第三级为具体文档工程的样式和内容，例如文档的配置文件 conf.py 在docs/source 文件夹下。

所有的源文件都存放在 docs/source 文件夹下，用户通常只需要增删修改docs/source文件夹下的内容即可。

- 配置文件为 conf.py 文件
- 各章节目录为各个 index.rst 文件
- 各章节页面为各个 xxx.md 文件

一级和二级目录内容不要修改，如需修改，**请直接修改 docs/source 文件夹下的相应文件。**

### 前提
- Linux 环境：python >3.7，运行docs/install.sh安装
- Windows 环境：双击docs文件夹下的install.bat解压python压缩包
- 先执行```cd docs``` 命令切换到docs目录下
- 生成pdf需要安装MikTex或者TexLive，以及Perl
    - Miktex: https://miktex.org/download
    - Perl: https://strawberryperl.com/

### 创建html

```
make html
```

### 创建pdf

```
make pdf
```

### 创建html和pdf

```
make all
```

### 清空_build文件夹

```
make clean
```

## License

MIT

## Reference

- [Sphinx 入门 — Sphinx 1.8.5 文档](https://sphinx-doc.readthedocs.io/zh_CN/master/usage/quickstart.html#adding-content)

- [readthedocs/recommonmark: A markdown parser for docutils](https://github.com/readthedocs/recommonmark#linking-to-headings-in-other-files)

- [Specifying Dependencies — Read the Docs 5.4.3 documentation](https://docs.readthedocs.io/en/latest/guides/specifying-dependencies.html)

- [reStructuredText — Sphinx 1.8.5 文档](https://sphinx-doc.readthedocs.io/zh_CN/master/usage/restructuredtext/index.html)
