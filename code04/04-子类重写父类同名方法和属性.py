"""
故事：daqoi掌握了师父和培训的技术后，自己潜心钻研出自己的独门配方的一套全新的煎饼果子
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

#2、定义徒弟类，继承师傅类 和 学校类,添加和父类同名的属性和方法
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    pass

#3、用徒弟类创建对象，调用实列属性和方法
# 注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

#结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法。