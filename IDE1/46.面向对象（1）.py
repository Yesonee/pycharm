# s = 'hao are you'
#
# l = s.split()
#
# dir(s)

##问题：假设我们有一辆汽车，我们知道它的速度(60km/h)，以及A、B两地的距离(100km)。要算出开着这辆车从A地到B地花费的时间
#面向过程
speed = 60.0
distance = 100.0
time =distance/speed
print(time)

#面向对象
class Car:
    speed = 0
    def drive(self,distance):
        time = distance / self.speed
        print(time)

car = Car()
car.speed = 60
car.drive(100)

#但是，如果我们让题目再稍稍复杂一点。假设我们又有了一辆更好的跑车，它的速度是150km/h，
# 然后我们除了想从A到B，还要从B到C（距离200km）。要求分别知道这两种车在这两段路上需要多少时间
#面向过程
# speed1 = 60.0
# distance1 = 100.0
# speed2 =150.0
# distance2 = 200.0
#
# time1 =distance1/speed1
# time2 =distance2/speed1
#
# print(time1)
# print(time2)

#面向对象方法
class Car:
    speed = 0
    def drive(self,distance):
        time = distance / self.speed
        print(time)

car1 = Car()
car1.speed = 60
car1.drive(100)
car1.drive(200)

car2 = Car()
car1.speed = 150
car1.drive(100)
car1.drive(200)

