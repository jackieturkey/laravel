#python  中的类
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score


bart = Student('Jackie',100)
# print(bart.name)
# print(bart.score)
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数

#python 中的封装

def print_score(std):
    print('%s : %s' %( std.name,std.score) )

print_score(bart)



