#迭代


#传两个参数来实现键值对的迭代
# for i,value in enumerate(['a','b','c']):
#     print(i,value)

#判断是否是可迭代对象（方法是通过collections模块的Iterable类型判断）
from collections import Iterable
isinstance('abc',Iterable) #字符串是否可以迭代
