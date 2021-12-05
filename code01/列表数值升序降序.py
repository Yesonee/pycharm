# coding=utf-8
students =[
    {'name':'TOM','age':20},
    {'name':'ROSE','age':21},
    {'name':'Jack','age':22},
]

#sort（key=lambda...,reverse=bool数据）
#1.name key对应值进行升序排序
students.sort(key=lambda x:x['name'])
print (students)
#2.name key对应值进行降序排序
students.sort(key=lambda x:x['name'],reverse=True)
print (students)
#3.age key对应值进行升序排序
students.sort(key=lambda x:x['age'])
print (students)