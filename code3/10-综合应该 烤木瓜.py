#1、定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        #被烤的时间
        self.cook.time = 0
        #地瓜的状态
        self.cook_state = '生的'
        #调料列表
        self.condiments = []

#2、创建
    #添加time形参 自己传入
    def cook(self,time):
        """烤地瓜的方法"""
        #1、先计算地瓜整体烤过的时间
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            #生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            #半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.condiments < 8:
            #熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            #烤糊了
            self.cook_state = '焦了'

    def  _str_(self):
            return f'这个地瓜被烤过的时间{self.cook_time}，状态是{self.cook_state}'

#2、创建对象并调用对应的实列方法

digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
print(digua1)