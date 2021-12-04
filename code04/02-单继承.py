"""
故事：一个煎饼果子的老师傅，在煎饼果子届爬滚很多年，研发一套精湛的煎饼果子技术。师傅要把这套技术传授给他唯一徒弟
分析：徒弟是不是要继承师父的所有技术？
"""

#1、师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#2、定义徒弟类、继承师父类
class Prentice(Master):
    pass

#3、用徒弟类创建对象，调用实列属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()