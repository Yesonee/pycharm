# 需求：洗衣机 功能：能洗衣服
# 1、定义洗衣机类
"""
class 类名（）：
    代码
"""
class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)

# 2、创建对象
# 对象名 = 类名（）
haier = Washer()
# 3、验证成果
# 打印haier对象
print(haier)
# 使用wash功能 -- 是列对象
haier.wash()

#由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象
