[![Pypi Version](https://img.shields.io/pypi/v/sphinx_evas_theme.svg)](https://pypi.python.org/pypi/sphinx_evas_theme)
[![License](https://img.shields.io/pypi/l/sphinx_evas_theme.svg)](https://pypi.python.org/pypi/sphinx_evas_theme/)
[![Documentation Status](https://readthedocs.org/projects/sphinx-evas-theme/badge/?version=latest)](http://sphinx-evas-theme.readthedocs.io/en/latest/?badge=latest)

**sphinx_evas_theme V2.0.0 版本现已支持生成word文档，赶快输入make docx尝试一下！**

# 为企业文档标准化而构建的sphinx主题

# 项目介绍

Sphinx EVAS Theme是一个为企业文档标准化而构建的sphinx主题，支持html，word和pdf标准渲染输出。

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

用户通过简单的命令即可实现项目文档模板初始化(evas命令，取代sphinx-quickstart)、文档构建(make html, make docx, make pdf以及make all)工作。

![](https://www.helloimg.com/i/2025/01/25/67946d6765c67.png)


## 项目参考

感谢下列开源项目为本项目提供支持

[sphinx](https://github.com/sphinx-doc/sphinx)：开源文档构建工具

[sphinx_rtd_theme](https://github.com/readthedocs/sphinx_rtd_theme)：使用最为广泛的Sphinx主题

[sphinx_idf_theme](https://github.com/espressif/sphinx_idf_theme)：乐鑫科技的Sphinx主题

[sphinx-jupyterbook-latex](https://github.com/executablebooks/sphinx-jupyterbook-latex)：支持LaTeX 输出的Sphinx扩展

[esp-docs](https://github.com/espressif/esp-docs)：乐鑫科技基于Sphinx的开源文档构建环境

## 效果预览

HTML显示效果

![html_preview1.jpg](https://www.helloimg.com/i/2025/01/25/67946d66a77be.jpg)

![html_preview2.jpg](https://www.helloimg.com/i/2025/01/25/67946d68a26b6.jpg)
PDF显示效果

![pdf_preview.jpg](https://www.helloimg.com/i/2025/01/25/67946d6b72e53.jpg)

## 环境准备

sphinx_evas_theme支持在windows和linux环境下构建文档，目前已在windows 11以及ubuntu 22.04上进行了测试。

sphinx_evas_theme在windows下需要安装python, perl, xelatex以及latexmk。

sphinx_evas_theme是基于sphinx创建的主题，而sphinx本身是一个python脚本/库，所以先需要安装python，建议版本为3.7以上。

具体python的安装方式请参考官网以及其他教程，python安装完后会自动将python根目录以及Scripts目录添加到path系统环境变量中：

- python官网：[https://www.python.org](https://www.python.org)

在构建pdf时，由于sphinx使用了latex语言作为中间语言，而编译latex需要latex编译环境，推荐安装texlive完整版。

- Texlive 2024 (Windows)下载地址：[https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)
- Texlive和python3在ubuntu环境一键安装命令：

```bash
apt-get install -y python3 python-is-python3 latexmk texlive-latex-recommended texlive-fonts-recommended texlive-xetex fonts-freefont-otf fonts-lmodern texlive-lang-chinese
```

- Linux环境下不需要安装perl

由于Texlive自带了perl脚本环境，例如我的Texlive安装在了 `C:\texlive`路径下，请将以下几个路径添加到windows path系统环境变量中：

- `C:\texlive\tlpkg\tlperl\bin`
- `C:\texlive\bin\windows`
- `C:\texlive\texmf-dist`

![path_env.jpg](https://www.helloimg.com/i/2025/01/25/67946d690cefb.jpg)

除此之外，本项目也支持Miktex，但在构建pdf时需要安装宏包，比较麻烦，不推荐。

- MikTex下载地址：[https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/win32/miktex/setup/windows-x64/basic-miktex-24.1-x64.exe](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/win32/miktex/setup/windows-x64/)
- MikTex需要单独安装perl脚本环境

  - perl下载地址：[https://strawberryperl.com](https://strawberryperl.com)

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

![evas_init.jpg](https://www.helloimg.com/i/2025/01/25/67946d66347ba.jpg)

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

![env_check.jpg](https://www.helloimg.com/i/2025/01/25/67946d66ee158.jpg)

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

- 如果你更倾向于使用Markdown，请遵循MyST Markdown，初始模板中已提供示例，使用其他Markdown语法可能会导致html和pdf无法显示或者显示异常。

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

![live_preview.jpg](https://www.helloimg.com/i/2025/01/25/67946d66ce640.jpg)

这样你在每次更改完markdown后，内容都会直接呈现在html网页中。

> 如果你使用的是VS Code进行MyST Markdown编写，强烈建议安装MyST-Markdown扩展，它支持语法高亮、实时预览




# MyST Markdown 语法入门

MyST Markdown MyST MyST（全称 Markedly Structured Text）专为 Sphinx 项目使用而设计的 Markdown 风格。 它是 CommonMark Markdown 和一些额外的语法片段的组合，以支持 Sphinx 的功能，因此您可以用纯 Markdown 编写 Sphinx 文档。

[MyST-Parser官网语法教程](https://myst-parser.readthedocs.io)

> 下方有部分MyST Markdown语法与Github Markdown语法不兼容，已省略，详细请安装后参考项目模板。

## 标题

为了兼容考虑，用一个空格在 `#` 和标题之间进行分隔。

```
# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题
```

显示效果：

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

## 有序列表

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。  
数字不必按数学顺序排列，但是列表应当以数字 1 起始。

```markdown
1. 条目1
2. 条目2
3. 条目3
    - 缩进条目
    - 缩进条目
```

显示效果

1. 条目1
2. 条目2
3. 条目3
    - 缩进条目
    - 缩进条目

---

## 无序列表

要创建无序列表，请在每个列表项前面添加破折号 (-)、星号 (*) 或加号 (+) 。缩进一个或多个列表项可创建嵌套列表。

```markdown
- 条目1
- 条目2
- 条目3
- 条目4
    - 缩进条目
    - 缩进条目

* 条目1
* 条目2
* 条目3
* 条目4
    * 缩进条目
    * 缩进条目

+ 条目1
+ 条目2
+ 条目3
+ 条目4
    + 缩进条目
    + 缩进条目
```

显示效果

- 条目1
- 条目2
- 条目3
- 条目4
    - 缩进条目
    - 缩进条目


* 条目1
* 条目2
* 条目3
* 条目4
    * 缩进条目
    * 缩进条目


+ 条目1
+ 条目2
+ 条目3
+ 条目4
    + 缩进条目
    + 缩进条目

---

## 文本换行

**Markdown中在段落前不要用空格（spaces）或制表符（ tabs）缩进段落。**

### 无效换行

在一行结尾没有加空格时，后一行内容会自动追加显示在前一行

```markdown
This is the first line.  
And this is the second line.
```

显示效果

This is the first line.
And this is the second line.

### 段内换行

要在没有段落的情况下换行，使用**两个或多个空格**进行换行，称为 结尾空格（trailing whitespace)

```markdown
This is the first line.  
And this is the second line.
```

显示效果

This is the first line.  
And this is the second line.


### 新段落

两行之间**间隔一行**，即可新增段落

```markdown
This is the first line.

And this is the second line.
```

显示效果

This is the first line.

And this is the second line.

---

## 字体样式

要加粗文本，在短语前后各添加**两个**星号` * `或下划线` _ `  
要斜体文本，在短语前后各添加**一个**星号` * `或下划线`_`  
要同时用粗体和斜体突出显示文本，在短语前后各添加**三个**星号` * `或下划线` _ `  
删除线在PDF中不可用

```markdown
*斜体* 

_斜体_

**粗体**

__粗体__

***粗体+斜体***

___粗体+斜体___


H{sub}`2`O, and 4{sup}`th` of July
```

显示效果

*斜体*

_斜体_

**粗体**

__粗体__

***粗体+斜体***

___粗体+斜体___

H{sub}`2`O, and 4{sup}`th` of July

---

## 单行块引用

要创建块引用，请在段落前添加一个` > `符号。

```markdown
> 这是一个引用块
```

显示效果

> 这是一个引用块

---

## 多行块引用

块引用可以包含多个段落。为段落之间的空白行添加一个 `>`符号。

```markdown
> 呼啸的秋风让人无限忧愁，进也忧愁，退也忧愁。
> 
> 异域戍边的人，哪个不陷入悲愁中？真是愁白了头啊。
> 
> 胡人之处多狂风，树木萧瑟干枯。
```

显示效果

> 呼啸的秋风让人无限忧愁，进也忧愁，退也忧愁。
> 
> 异域戍边的人，哪个不陷入悲愁中？真是愁白了头啊。
> 
> 胡人之处多狂风，树木萧瑟干枯。

---

## 代码块

在代码前和后的行上使用三个反引号` ``` `或三个波浪号` ~~~ ` 
在代码块之前的反引号旁边指定一种语言，即可实现**语法高亮**  

```markdown
    ```python
    import os
    print("Hello World!")
    ```

    ~~~ json
    {
        "firstName": "John",
        "lastName": "Smith",
        "age": 25
    }
    ~~~
```

显示效果

```python
import os
print("Hello World!")
```

~~~json
{
    "firstName": "John",
    "lastName": "Smith",
    "age": 25
}
~~~

---

## 数学公式

math角色和指令分别用于定义内联数学和块数学。  
**注意:** ```和{math}之间不能有空格

```markdown
    ```{math}
    :label: mymath
    (a + b)^2 = a^2 + 2ab + b^2

    (a + b)^2  &=  (a + b)(a + b) \\
            &=  a^2 + 2ab + b^2
    ```
```

显示效果

```{math}
:label: mymath
(a + b)^2 = a^2 + 2ab + b^2

(a + b)^2  &=  (a + b)(a + b) \\
           &=  a^2 + 2ab + b^2
```

---

## 脚注

脚注使用 pandoc 规范。它们的标签以 ^ 开头，然后可以是任何字母数字字符串（无空格），不区分大小写。

```markdown
- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
```

显示效果

- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.  
[^3]: This is a manually-numbered footnote definition.  
---

## 嵌入图像

要添加图像，请使用感叹号 (!), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

```markdown
![philly-magic-garden.jpg](https://www.helloimg.com/i/2025/01/25/67946d6aed4aa.jpg)
```

显示效果

![philly-magic-garden.jpg](https://www.helloimg.com/i/2025/01/25/67946d6aed4aa.jpg)

---

## 链接图片

给图片增加链接，请将图像的Markdown 括在方括号中，然后将链接添加在圆括号中。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片标题")`

```markdown
[![philly-magic-garden.jpg](https://www.helloimg.com/i/2025/01/25/67946d6aed4aa.jpg)](https://markdown.com.cn)
```

显示效果

[![philly-magic-garden.jpg](https://www.helloimg.com/i/2025/01/25/67946d6aed4aa.jpg)](https://markdown.com.cn)

---

## 超链接

超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接标题")`

```markdown
这是一个链接 [Markdown语法](https://markdown.com.cn)

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")
```

显示效果

这是一个链接 [Markdown语法](https://markdown.com.cn)

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")

[^myref]: This is an auto-numbered footnote definition.
    
[^3]: This is a manually-numbered footnote definition.


# 已知问题

**问题1**: make docx生成的word公式显示不正确  
**解决方案**: 公式需要在word中手动写，或者使用截图

**问题2**: Markdown使用两个及以上空格进行段内换行，在生成word中，文本没有正确换行  
**解决方案**: word生成暂不支持段内换行，请在word中使用SHIFT+ENTER进行段内换行

**问题3**: makedown中如果文本是超长的网址链接或者没有空的连续英文，该文本在生成pdf时可能超过右页边距  
**解决方案**: latex普遍问题，无法解决，需要手动进行文本换行

**问题4**: pdf文件没有正确生成或者部分内容缺失  
**解决方案**: 可能是markdown内容不正确引起的，需要检查pdf目录下的log文件是否存在error

**问题5**: word封面中文档状态和版本显示不正确  
**解决方案**: 文档状态和版本需要在word中手动调整

**问题6**: word显示语言为英文时，生成的word正文右上角显示错误  
**解决方案**: 手动调整word右上角的StyleRef为Heading1