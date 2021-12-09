'''
仍然是从A地到B地，这次除了有汽车，我们还有了一辆自行车！
自行车和汽车有着相同的属性：速度（speed）。还有一个相同的方法（drive），来输出行驶/骑行一段距离所花的时间。但这次我们要给汽车增加一个属性：每公里油耗（fuel）。而在汽车行驶一段距离的方法中，除了要输出所花的时间外，还要输出所需的油量。
面向过程的方法，你可能需要写两个函数，然后把数据作为参数传递进去，在调用的时候要搞清应该使用哪个函数和哪些数据。有了面向对象，你可以把相关的数据和方法封装在一起，并且可以把不同类中的相同功能整合起来。这就需要用到面向对象中的另一个重要概念：继承。
我们要使用的方法是，创建一个叫做Vehicle的类，表示某种车，它包含了汽车和自行车所共有的东西：速度，行驶的方法。然后让Car类和Bike类都继承这个Vehicle类，即作为它的子类。在每个子类中，可以分别添加各自独有的属性。
'''
#Vehicle类被称为基本类或超类，Car类和Bike类被成为导出类或子类
class Vehicle:
    def __init__(self,speend):
        self.speed = speend

    def drive(self,distance):
        print('need %f hour(s)' % (distance/self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle.__init__(self,speed)
        self.fuel  = fuel

    def drive(self,distance):
        Vehicle.drive(self,distance)
        print('need %f fuels' % (distance * self.fuel))

b = Bike(15.0)
c = Car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)