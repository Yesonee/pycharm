"""
房子类
1、实列属性
    房子地理位置
    房子占地面积
    房子剩余空间
    房子内家具列表
2、实列方法
    容纳家具
显示房屋信息
"""


class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子地理位置{self.address},房屋面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        # 如果 家具占地面积 <= 房子剩余面积：可以搬入（家具列表添加家具名字数据并房子剩余面积更新）
        # 否则：提示用户家具太大，剩余面积不足，无法容纳
        #
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            # 能容纳追加家具名字
            self.free_area -= item.area
            # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积
        else:
            print('用户家具太大，剩余面积不足，无法容纳')


# 双人床
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 16)

# 房子1：北京，1000
jia1 = Home('北京', 1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)
print(jia1)
