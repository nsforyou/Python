# 课程名称:Python基础课程
# 创建日期:2022/9/18 1:42
# 作   者: 十八般武艺
# 版   本: Python 3.10.7

"""
授课内容:
    切片:[开始:结尾]取左不取右
    [:]->> 切片获取的是整个字符串
    切片:[开始:结尾:步长]取左不取右
"""
name = "陈浩南帅气够狠还讲义气"
# 切片
print(name[0:3])
print(name[1:3])
print(name[:])
print(name[-3:])
print(name[0:6])
print(name[0:6:2])
print(name[:])
print(name[::3])
print(name[::-1])

