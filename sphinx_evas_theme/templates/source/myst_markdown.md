# MyST Markdown 语法入门

MyST Markdown MyST MyST（全称 Markedly Structured Text）专为 Sphinx 项目使用而设计的 Markdown 风格。 它是 CommonMark Markdown 和一些额外的语法片段的组合，以支持 Sphinx 的功能，因此您可以用纯 Markdown 编写 Sphinx 文档。

[MyST-Parser官网语法教程](https://myst-parser.readthedocs.io)


## 提示框

警告提示框（Admonition）突出显示与页面叙述稍有不同的特定文本块，例如注释或警告。

``` markdown

:::{tip}
给读者一些有用的提示吧！
:::

:::{note}
这是一个笔记
:::


:::{caution}
这是一个警告
:::

:::{error}
这是一个错误
:::

```


显示效果

:::{tip}
给读者一些有用的提示吧！
:::

:::{note}
这是一个笔记
:::


:::{caution}
这是一个警告
:::

:::{error}
这是一个错误
:::

---------------------

## 标题

为了兼容考虑，用一个空格在 `#` 和标题之间进行分隔。

``` markdown
# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

```

---------------------

## 有序列表
要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 1 起始。
``` markdown
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

---------------------

## 无序列表
要创建无序列表，请在每个列表项前面添加破折号 (-)、星号 (*) 或加号 (+) 。缩进一个或多个列表项可创建嵌套列表。

``` markdown
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

---------------------

## 文本换行

### 无效换行

在一行结尾没有加空格时，后一行内容会自动追加显示在前一行
``` markdown
This is the first line.  
And this is the second line.
```

显示效果

This is the first line.
And this is the second line.

### 正确换行

要在没有段落的情况下换行，请使用 \ 后跟新行。这对应于 HTML 中的 <br> 和 LaTeX 中的 \\ 。
``` markdown
This is the first line. \
And this is the second line.
```

显示效果

This is the first line. \
And this is the second line.

### 新段落

两行之间**间隔一行**，即可新增段落
``` markdown
This is the first line.

And this is the second line.
```

显示效果

This is the first line.

And this is the second line.

---------------------

## 字体样式
要加粗文本，在短语前后各添加**两个**星号`*`或下划线`_`  
要斜体文本，在短语前后各添加**一个**星号`*`或下划线`_`  
要同时用粗体和斜体突出显示文本，在短语前后各添加**三个**星号`*`或下划线`_`  
删除线在PDF中不可用

``` markdown
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

---------------------

## 单行块引用
要创建块引用，请在段落前添加一个`>`符号。

``` markdown
> 这是一个引用块
```

显示效果

> 这是一个引用块

---------------------

## 多行块引用
块引用可以包含多个段落。为段落之间的空白行添加一个`>`符号。

``` markdown

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

---------------------

## 代码块
在代码前和后的行上使用三个反引号```或三个波浪号~~~ 
在代码块之前的反引号旁边指定一种语言，即可实现**语法高亮**  

``` markdown
    ``` python
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

``` python
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

---------------------

## 文件中的代码

可以使用 literalinclude 指令从文件中包含更长的代码：

``` markdown

> ```{literalinclude} quickstart.py
> ```

```

显示效果

```{literalinclude} quickstart.py
```

---------------------

## 数学公式

math角色和指令分别用于定义内联数学和块数学。

``` markdown

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

---------------------


## 脚注
脚注使用 pandoc 规范。它们的标签以 ^ 开头，然后可以是任何字母数字字符串（无空格），不区分大小写。

``` markdown
- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
```


- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.

---------------------

## 嵌入图像
要添加图像，请使用感叹号 (!), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

``` markdown
![这是图片](_static/philly-magic-garden.jpg "Magic Gardens")

    ```{image} _static/philly-magic-garden.jpg
    :alt: philly magic garden
    :class: bg-primary
    :scale: 50 %
    :align: center
    ```

```
显示效果

![这是图片](_static/philly-magic-garden.jpg "Magic Gardens")

```{image} _static/philly-magic-garden.jpg
:alt: philly magic garden
:class: bg-primary
:scale: 50 %
:align: center
```

---------------------

## 链接图片
给图片增加链接，请将图像的Markdown 括在方括号中，然后将链接添加在圆括号中。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片标题")`

``` markdown
[![这是图片](_static/philly-magic-garden.jpg "Magic Gardens")](https://markdown.com.cn)
```

显示效果

[![这是图片](_static/philly-magic-garden.jpg "Magic Gardens")](https://markdown.com.cn)

---------------------

## 超链接
超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接title")`

``` markdown
这是一个链接 [Markdown语法](https://markdown.com.cn)

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")
```

显示效果

这是一个链接 [Markdown语法](https://markdown.com.cn)

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")

---------------------

## 表格

表格必须使用MyST Markdown格式，否则PDF无法显示

list-table 指令用于根据统一的两级项目符号列表中的数据创建表格。 “统一”是指每个子列表（二级列表）必须包含相同数量的列表项。

``` markdown
:::{list-table} Frozen Delights!
:widths: 15 10 30
:header-rows: 1

*   - **Treat**
    - **Quantity**
    - **Description**
*   - Albatross
    - 2.99
    - On a stick!
*   - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be
 crunchy, now would it?
*   - Gannet Ripple
    - 1.99
    - On a stick!
:::
```

显示效果

:::{list-table} Frozen Delights!
:widths: 15 10 30
:header-rows: 1

*   - **Treat**
    - **Quantity**
    - **Description**
*   - Albatross
    - 2.99
    - On a stick!
*   - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be
 crunchy, now would it?
*   - Gannet Ripple
    - 1.99
    - On a stick!
:::
