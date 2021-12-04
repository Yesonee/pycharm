"""
多继承：一个子类同时继承了多个父类
故事推进：daqiu是个爱学习的孩子，想学习更多的煎饼果子技术，于是，在百度搜索到黑马，报班学习煎饼果子技术
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongf}制作煎饼果子')

#2、定义徒弟类，继承师傅类 和 学校类
class Prentice(Master, School):
    pass

#3、用徒弟类创建对象，调用实列属性和方法
# 注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
