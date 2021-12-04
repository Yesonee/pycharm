# coding=utf-8
#1.无参数
fn1 = lambda: 100
print (fn1())

#有参数
fn2 = lambda a,b,c=100:a+b+c
print (fn2(10,20))

#一个参数
fn3 = lambda a:a
print (fn3('hello world'))

#默认参数/缺省参数
fn4 =lambda  d,e,f=100: d+e+f
print  (fn4(10,20))
print  (fn4(10,20,100))#不是默认数据就使用真实值

