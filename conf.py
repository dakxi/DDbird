
# Sphinx 文档生成器的配置文件。
#
# 此文件仅包含最常用选项的选择。对于一个完整的
# 列表见文档：
# https://www.sphinx-doc.org/en/master/usage/configuration.html

进口 推荐
来自 推荐。转换 导入 AutoStructify

# -- 路径设置 ---------------------------------- -----------------

# 如果扩展（或用 autodoc 记录的模块）在另一个目录中，
# 在此处将这些目录添加到 sys.path。如果目录是相对于
# 文档根目录，使用 os.path.abspath 使其成为绝对路径，如此处所示。
#
# 导入我们
# 导入系统
# sys.path.insert(0, os.path.abspath('.'))

# -- 项目信息 --------------------------------------------------------- --------

# 源文件名的后缀。
# 您可以指定多个后缀作为字符串列表：
source_suffix   = [ '.rst' , '.md' ]

项目 =  '使用手册'
版权  =   '2022，DarkseaDogbird'
作者 =  '多克悉多布'
master_doc  =  '索引'

版本 =  '1.0.0'
# 完整版，包括 alpha/beta/rc 标签
发布 =  '1.0.0-rc'


# -- 通用配置 --------------------------------------------------------- ------

# 在此处添加任何 Sphinx 扩展模块名称，作为字符串。他们可以
# Sphinx 附带的扩展（名为“sphinx.ext.*”）或您的自定义
＃ 那些。
扩展 = [
    “推荐”
]

# 在此处添加任何包含模板的路径，相对于该目录。
模板路径 = [ '_模板' ]

# Sphinx 自动生成的内容的语言。参考文档
# 获取支持的语言列表。
#
# 如果您通过 gettext 目录进行内容翻译，也会使用此选项。
# 通常你从命令行为这些情况设置“语言”。
language = 'zh'

# 模式列表，相对于源目录，匹配文件和
# 查找源文件时要忽略的目录。
# 此模式也会影响 html_static_path 和 html_extra_path。
排除模式 = []


# -- HTML 输出选项 ------------------------------------------- ------

# 用于 HTML 和 HTML 帮助页面的主题。请参阅文档
# 内置主题列表。
#
html_theme   =   'sphinx_rtd_theme'

# 在此处添加任何包含自定义静态文件（如样式表）的路径，
# 相对于这个目录。它们在内置静态文件之后被复制，
# 所以名为“default.css”的文件将覆盖内置的“default.css”。
html_static_path   = [ '_static' ]

乳胶元素 = {
# 纸张尺寸（'letterpaper' 或 'a4paper'）。
#'papersize': '信纸',
 
# 字体大小（'10pt'、'11pt' 或 '12pt'）。
#'pointsize': '10pt',
 
# LaTeX 序言的附加内容。
#'序言': '',
'序言'：r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
}

默认 设置（应用程序）：
    应用程序。add_config_value ( 'recommonmark_config' , {
            'url_resolver'：lambda   url：github_doc_root   +   url，
            'auto_toc_tree_section' : '内容' ,
            }，真）
    应用程序。add_transform ( AutoStructify )
