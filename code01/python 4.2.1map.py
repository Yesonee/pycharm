# coding=utf-8
#1。准备列表数据
list1 =[1,2,3,4,5,]
#2。准备2次方计算的函数
def funs(x):
    return x ** 2

#3。调用map
result = map(funs,list1)

#4。验收成功
#输出内存地址
print (result)
#输出结果
print (list(result))