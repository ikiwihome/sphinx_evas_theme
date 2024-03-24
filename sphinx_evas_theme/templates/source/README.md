# 项目介绍

Sphinx EVAS Theme是一个为企业文档标准化而构建的sphinx主题，支持html和pdf标准渲染输出。

**项目亮点**:

- 简化了文档构建过程,用户只需关注文档内容而无需关心复杂配置
- 提供了美观、符合企业标准的HTML、PDF和Word渲染输出样式
- 针对PDF输出优化了LaTeX模板和封面样式,美化了PDF渲染效果
- 嵌入了适合打印美观的免费商用中文(SourceHanSansSC)和英文字体(DejaVuSans)
- 新增了Word输出模板和构建命令,实现Word输出与PDF保持一致样式
- 引入了常用的Sphinx扩展作为默认配置,减少用户配置工作
- 提供了evas命令快速初始化文档项目模板,make命令进行编译构建
- 所有配置参数均有中文注释说明,降低了使用门槛

本主题是基于sphinx_rtd_theme作为基础主题构建，做出了如下修改：

- 新增latex导言和封面的模板，美化了PDF渲染样式
- 嵌入了适合打印美观的免费商用中英文字体
- 简化了PDF构建过程，由make latexpdf命令更改为make pdf命令
- 新增word模板和构建命令，美化了word渲染样式，样式保持与PDF基本一致
- 新增make all命令，以及环境检查
- 简化conf.py配置过程，只需要更改文档内容信息即可
- 引入常用的sphinx扩展(默认)

> 具体的配置参数在evas命令生成的项目模板source/conf.py文件中，每个配置参数均已中文注释详细说明。

用户通过简单的命令即可实现项目文档模板初始化(evas命令，取代sphinx-quickstart)、文档构建(make html, make pdf以及make all)工作。

```{image} _static/flow.png
:class: bg-primary
:scale: 100 %
```


## 项目参考

感谢下列开源项目为本项目提供支持

[sphinx：开源文档构建工具](https://github.com/sphinx-doc/sphinx)

[sphinx_rtd_theme：使用最为广泛的Sphinx主题](https://github.com/readthedocs/sphinx_rtd_theme)

[sphinx_idf_theme：乐鑫科技的Sphinx主题](https://github.com/espressif/sphinx_idf_theme)

[sphinx-jupyterbook-latex：支持LaTeX 输出的Sphinx扩展](https://github.com/executablebooks/sphinx-jupyterbook-latex)

[esp-docs：乐鑫科技基于Sphinx开源文档构建环境](https://github.com/espressif/esp-docs)

## 效果预览

HTML显示效果

```{image} _static/html_preview1.jpg
:class: bg-primary
:scale: 50 %
:align: center
```

```{image} _static/html_preview2.jpg
:class: bg-primary
:scale: 50 %
:align: center
```

PDF显示效果

```{image} _static/pdf_preview.jpg
:class: bg-primary
:scale: 50 %
:align: center
```



## 环境准备

sphinx_evas_theme支持在windows和linux环境下构建文档，目前已在windows 11以及ubuntu 22.04上进行了测试。

sphinx_evas_theme在windows下需要安装python, perl, xelatex以及latexmk。

sphinx_evas_theme是基于sphinx创建的主题，而sphinx本身是一个python脚本/库，所以先需要安装python，建议版本为3.7以上。

具体python的安装方式请参考官网以及其他教程，python安装完后会自动将python根目录以及Scripts目录添加到path系统环境变量中：

- python官网：[https://www.python.org](https://www.python.org)

在构建pdf时，由于sphinx使用了latex语言作为中间语言，而编译latex需要latex编译环境，推荐安装texlive完整版。

- Texlive 2024 (Windows)下载地址：\
[https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)

- Texlive和python3在ubuntu环境一键安装命令:
```bash
apt-get install -y python3 python-is-python3 latexmk texlive-latex-recommended texlive-fonts-recommended texlive-xetex fonts-freefont-otf fonts-lmodern texlive-lang-chinese
```

- Linux环境下不需要安装perl



由于Texlive自带了perl脚本环境，例如我的Texlive安装在了`C:\texlive`路径下，请将以下几个路径添加到windows path系统环境变量中：

- `C:\texlive\tlpkg\tlperl\bin`
- `C:\texlive\bin\windows`
- `C:\texlive\texmf-dist`


```{image} _static/path_env.jpg
:class: bg-primary
:scale: 50 %
:align: center
```

在上述环境安装完成后，请在windows cmd命令行或者linux终端中运行如下几个命令，如果没有显示错误，则代表环境安装完毕

- python
- xelatex
- latexmk
- perl (仅windows)


## 如何安装Sphinx EVAS Theme

sphinx_evas_theme托管在[PyPI](https://pypi.org/)中，通过python的pip安装：

```python
pip install sphinx_evas_theme
```

安装过程会将所有主题的依赖包一并安装。



### 在venv python虚拟环境下安装

在venv python虚拟环境下安装的命令如下，先新建一个空文件夹，然后在文件夹中输入：

```python
pip install virtualenv

python -m venv venv

.\venv\Scripts\activate.bat   # windows环境

source venv/bin/activate    # linux环境

pip install sphinx_evas_theme
```


## 如何使用

**第一步**

本项目的使用非常简单，只需要在任意空文件夹下执行`evas`命令，即可创建项目模板

```{image} _static/evas_init.jpg
:class: bg-primary
:scale: 50 %
:align: center
```


**提示：** 默认source目录下，除了index.rst和conf.py为必需，其他均为示例文件，可删除。


**第二步**

创建一个markdown文件，并将文件名添加到index.rst文件末尾。

**示例:** 例如markdown文件为readme.md，则添加readme到index.rst文件末尾。

**第三步**

修改conf.py文件，填写标题、子标题、作者等信息

**第四步**

构建html、pdf、docx文档


```
evas            # 创建项目模板

make html       # 生成html网页，文件在_build/html路径下，index.html为入口

make docx       # 生成office word文档，文件在_build/docx路径下

make pdf        # 生成office pdf文档，文件在_build/pdf路径下

make all        # 一次同时生成html, word, pdf

make clean      # 清空_build文件夹

make livehtml   # 编辑markdown时实时预览html网页
```


> windows下每次执行make命令时会自动检查环境，如果python, perl, xelatex, latexmk均OK，则会根据命令参数构建对应文档，否则会直接中断

```{image} _static/env_check.jpg
:class: bg-primary
:scale: 50 %
:align: center
```

> 目前pdf封面左下角会显示evas版权信息，如果您需要修改，请自行fork此项目并在\sphinx_evas_theme\latex_templates\titlepage.tex 第45行修改版权信息



### 本项目引入了哪些Sphinx扩展？

引入的扩展有：

- myst_parser
- sphinx_markdown_tables
- sphinx_markdown_checkbox
- sphinx_copybutton
- sphinx_design
- sphinx.ext.intersphinx
- sphinx.ext.autodoc
- sphinx.ext.autosummary
- sphinx.ext.mathjax
- sphinx.ext.viewcode
- sphinx.ext.githubpages
- sphinx.ext.napoleon
- sphinx_togglebutton
- docxbuilder


### 文档编写语言

Sphinx EVAS Theme已经默认开启了reStructuredText和Markdown支持

- 如果你更倾向于使用Markdown，请遵循MyST Markdown，初始模板中已提供示例，使用其他Markdown语法可能会导致html，word或pdf内容缺失无法显示或者显示异常。

    MyST Markdown语法请参考：https://mystmd.org/guide/typography

- 如果你更倾向于使用reStructuredText，请参考reStructuredText语法。


## Sphinx EVAS Theme 目录结构

```
sphinx_evas_theme
│
│
├───sphinx_evas_theme          # 主题主目录
│   ├───docx_templates         # 支持word文档输出，以及word模板文件
│   │
│   ├───latex_templates        # latex模板，包含导言和封面样式
│   │   └───fonts              # pdf字体文件
│   ├───locale                 # 国际化翻译，仅支持中文和英文
│   │
│   ├───static                 # html js, css, logo
│   │   ├───css                # html css样式
│   │   │   └───fonts          # html字体文件
│   │   └───js
│   └───templates              # 项目模板，详见下一章
│       └───source
│           ├───_static
│           └───_templates
│
└───tests                      # pytest 测试用例
```

## 项目模板目录结构

```
├───source             # 文档内容存放目录
│   ├───_static        # 文档自定义html静态元素，如css,js存放目录，默认为空
│   └───_templates     # 文档自定义html模板，如自定义页眉页脚等，默认为空，详细请参考Sphinx教程
└───_build             # 构建目录，存放生成的文档
    ├───doctrees
    ├───docx           # word生成路径
    ├───html           # html生成路径
    ├───latex          # 构建pdf中生成的latex目录
    └───pdf            # pdf生成路径
```


## Live Preview 实时在线预览

如果你想在编辑文档时实时查看更改后的html，不必每次都重新make html，然后打开html，可以使用如下命令：

```
make livehtml
```

按照提示打开这个链接：http://127.0.0.1:8000

```{image} _static/live_preview.jpg
:class: bg-primary
:scale: 50 %
:align: center
```


这样你在每次更改完markdown后，内容都会直接呈现在html网页中。

> 如果你使用的是VS Code进行MyST Markdown编写，强烈建议安装MyST-Markdown扩展，它支持语法高亮、实时预览