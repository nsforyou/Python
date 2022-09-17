# 课程名称:Python基础课程
# 创建日期:2022/9/18 0:23
# 作   者: 十八般武艺
# 版   本: Python 3.10.7

"""
授课内容:
    Python关键字
        import keyword
        print(keyword.kwlist)
    缩进
        按tab键实现4个空格的缩进,补齐方式
        按下shift+tab实现反向缩进
    多行语句
"""
print("我们看看Python都有哪些关键字:")
import keyword
print(keyword.kwlist)
print("我们看看怎么缩进")
if 2>1:
    print("2>1")
print("看看如何换行")
a = 1
b = 2
c = 3
ddd = a+\
      b+\
      c
print(ddd)
# 括号内随意换行,并不会报错