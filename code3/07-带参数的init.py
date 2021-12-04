# 思考：一个类可以创建多个对象，传参数可以不同的对象设置不同的初始化属性
# 1、定义类：带参数的init 宽度和高度： 实列方法：调用实列属性
class Washer():
    def __init__(self, width, height):
    #实列属性
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度实{self.width},洗衣机的高度是{self.height}')


# 2、创建对象，创建多个对象且属性值不同：调用实列方法
haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(40, 50)
haier2.print_info()
