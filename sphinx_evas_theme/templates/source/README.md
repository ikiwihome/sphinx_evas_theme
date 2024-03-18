# 项目介绍

Sphinx EVAS Theme是一个为企业文档标准化而构建的sphinx主题，支持html和pdf标准渲染输出。

相比于Sphinx原始的PDF渲染样式，Sphinx EVAS Theme提供了更加美观简洁，符合企业标准的html和pdf渲染样式。

本主题是基于sphinx_rtd_theme作为基础主题构建，增加了latex导言和封面的模板，并引入了常用的sphinx扩展。

项目使用也相比sphinx以及其他主题更加简单，用户无需关注具体的sphinx以及主题配置参数，只需要填写文档元素例如标题，子标题，作者等信息，从而把精力专注在文档撰写上。

- 具体的配置参数在evas命令生成的项目模板source/conf.py文件中，每个配置参数均已中文注释详细说明。

用户通过简单的命令即可实现项目文档模板初始化(evas命令，取代sphinx-quickstart)、文档构建(make html, make pdf以及make all)工作。



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

- Texlive 2023 (Windows)下载地址：\
[https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive2023-20230313.iso](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)

- Texlive和python3在ubuntu环境一键安装命令:
``` bash
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

除此之外，本项目也支持Miktex，但在构建pdf时需要安装宏包，比较麻烦，不推荐。

- MikTex下载地址：\
[https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/win32/miktex/setup/windows-x64/basic-miktex-24.1-x64.exe](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/win32/miktex/setup/windows-x64/)
- MikTex需要单独安装perl脚本环境
  - perl下载地址：[https://strawberryperl.com](https://strawberryperl.com)



在上述环境安装完成后，请在windows cmd命令行或者linux终端中运行如下几个命令，如果没有显示错误，则代表环境安装完毕

- python

- xelatex

- latexmk

- perl (仅windows)



## 如何安装Sphinx EVAS Theme

sphinx_evas_theme托管在[PyPI](https://pypi.org/)中，通过python的pip安装：

``` python
pip install sphinx_evas_theme
```

安装过程会将所有主题的依赖包一并安装。



### 在venv python虚拟环境下安装

在venv python虚拟环境下安装的命令如下，先新建一个空文件夹，然后在文件夹中输入：

``` python
pip install venv

python -m venv venv

\venv\Scripts\activate.bat   # windows环境下

source venv/bin/activate    # linux环境下

pip install sphinx_evas_theme
```



## 如何使用

sphinx_evas_theme的使用非常简单，只需要在目标路径/文件夹下执行`evas`命令，即可创建sphinx_evas_theme项目模板

```{image} _static/evas_init.jpg
:class: bg-primary
:scale: 50 %
:align: center
```


### 创建项目模板

```
evas
```



### 创建html

```
make html
```

> 构建好的html在 _build/html路径下，index.html为入口


### 实时预览

```
sphinx-autobuild source source/_build/html
```


### 创建pdf

```
make pdf
```

> 构建好的html在 _build/pdf路径下，文件名为project参数



### 创建html和pdf

```
make all
```



### 清空_build文件夹

```
make clean
```



> windows下每次执行make命令时会自动检查环境，如果python, perl, xelatex, latexmk均OK，则会根据命令参数构建对应文档，否则会直接中断

```{image} _static/env_check.jpg
:class: bg-primary
:scale: 50 %
:align: center
```

> 目前pdf封面左下角会显示evas版权信息，如果您需要修改，请自行fork此项目并在\sphinx_evas_theme\latex_templates\titlepage.tex 第45行修改版权信息



### Sphinx EVAS Theme引入了哪些Sphinx扩展？

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


### 文档编写语言

Sphinx EVAS Theme已经默认开启了reStructuredText和Markdown支持

- 如果你更倾向于使用Markdown，请遵循MyST Markdown，初始模板中已提供示例，使用其他Markdown语法可能会导致html和pdf无法显示或者显示异常。

    MyST Markdown语法请参考：https://mystmd.org/guide/typography

- 如果你更倾向于使用reStructuredText，请参考reStructuredText语法。


## Sphinx EVAS Theme 目录结构

```

sphinx_evas_theme
│
├───docs                       # 主题示例文档
│
├───screenshot                 # README.md 图片
│
├───sphinx_evas_theme          # 主题主目录
│   ├───latex_templates        # latex模板，包含导言和封面样式
│   │   └───fonts              # pdf字体文件
│   ├───locale                 # 国际化翻译，仅支持中文和英文
│   │
│   │
│   ├───static                 # html js, css, logo
│   │   ├───css                # html css样式
│   │   │   └───fonts          # html字体文件
│   │   └───js
│   └───templates              # 项目模板，详见下一章
│       └───source
│           ├───_static
│           └───_templates
├───src                        # 暂时无用
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
    ├───html           # html生成路径
    ├───latex          # 构建pdf中生成的latex目录
    └───pdf            # pdf生成路径

```


## Live Preview 实时在线预览

如果你想在编译文档时实时查看更改后的html，不必每次都重新make html，然后打开html，可以使用如下命令：

```
sphinx-autobuild source source/_build/html
```

按照提示打开这个链接：http://127.0.0.1:8000

```{image} _static/live_preview.jpg
:class: bg-primary
:scale: 50 %
:align: center
```


这样你在每次更改完markdown后，内容都会直接呈现在html网页中。

> 如果你使用的是VS Code进行MyST Markdown编写，强烈建议安装MyST-Markdown扩展，它支持语法高亮、实时预览