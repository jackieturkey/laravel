#使用@property内置装饰器把一个方法变成属性调用

class Student(object):

    @property
    def score (self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100 :
            raise ValueError('score must be in 0-100 ')
        
        self._score = value