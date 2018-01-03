#装饰器(decorator)
# def now():
#     print('2017-10-01')

# f = now
# f()

#装饰器
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func._name_)
        return func(*args,**kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
call now()