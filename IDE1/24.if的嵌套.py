#==和 for 循环一样，if 也可以嵌套使用，即在一个 if/elif/else 的内部，再使用 if。这有点类似于电路的串联==#
'''
if 条件1:
   if 条件2:
       语句1
   else:
       语句2
else:
   if 条件2:
       语句3
   else:
       语句4
=======================
条件1为True，条件2为True时，

执行语句1；

条件1为True，条件2为False时，

执行语句2；

条件1为False，条件2为True时，

执行语句3；

条件1为False，条件2为False时，

执行语句4。
'''





"""
假设需要这样一个程序：
我们先向程序输入一个值x，再输入一个值y。(x,y)表示一个点的坐标。程序要告诉我们这个点处在坐标系的哪一个象限。
x>=0，y>=0，则输出1；
x<0，y>=0，则输出2；
x<0，y<0，则输出3；
x>=0，y<0，则输出4。
"""
if y >= 0:
    if x >= 0:
        print(1)
    else:
        print(2)
else:
    if x < 0:
        print(3)
    else:
        print(4)
