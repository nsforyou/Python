# 课程名称:Python基础课程
# 创建日期:2022/9/18 3:35
# 作   者: 十八般武艺
# 版   本: Python 3.10.7

"""
授课内容:
  安装pandas教程分享
  https://jingyan.baidu.com/article/ceb9fb100ba416ccad2ba089.html#:~:text=%E9%A6%96%E5%85%88%E5%8F%B3%E9%94%AE%E7%82%B9%E5%87%BB%E6%A1%8C%E9%9D%A2%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%BC%80%E5%A7%8B%E5%9B%BE%E6%A0%87%EF%BC%8C%E7%84%B6%E5%90%8E%E9%80%89%E6%8B%A9%E8%BF%90%E8%A1%8C%E3%80%82%20%E5%9C%A8%E5%BC%B9%E5%87%BA%E7%9A%84%E7%AA%97%E5%8F%A3%E4%B8%AD%E8%BE%93%E5%85%A5cmd%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E7%A1%AE%E5%AE%9A%E3%80%82,%E8%BE%93%E5%85%A5%EF%BC%9Apip%20install%20pandas%EF%BC%8C%E6%8C%89%E4%B8%8B%E5%9B%9E%E8%BD%A6%E9%94%AE%EF%BC%8C%E4%BC%9A%E8%87%AA%E5%8A%A8%E5%BC%80%E5%A7%8B%E5%AE%89%E8%A3%85%E3%80%82
"""
import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)