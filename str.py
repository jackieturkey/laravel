#定制类
#__str__
# class Human(object):
#     def __init__(self,gender):
#         self.gender = gender
#     def __str__(self):
#         return 'Human object(gender: %s)' % self.gender

# print (Human('male'))

#斐波那契数列
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1    #初始化两个计算器  a,b

    def __iter__(self):
        return self    #实例本身就是迭代本身，所以返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b #计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a #返回下一个值



