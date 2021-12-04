"""
测试目标
1、访问模式对文件的影响
2、访问模式对write（）的影响
3、访问模式是否可以忽略
"""

#r:如果文件不存在，报错：
#f = open（test1.txt",'r'）
f = open('test1.txt', 'r')
f.close()