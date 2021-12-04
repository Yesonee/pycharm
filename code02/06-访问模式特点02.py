"""
测试目标
1、r+ 和 w+ a+ 区别
2、文件指针对数据抓取的影响
"""
# r+： r没有文件则报错；文件指针在开头，所以被读取出来
#f = open('text.txt', 'r')
# f = open ('test1.txt','r+')

# w+:没有该文件会新建文件；w的特点：文件指针在开头，用新内容覆盖原内容
#f = open('text.txt', 'w')
#f = open('text.txt', 'w+')

# a+：没有该文件会新建文件；文件指针在结尾，无法读取数据（文件指针后面无数据）
#f = open('text123.txt', 'a')
f = open('text456.txt', 'a+')

con = f.read()
print(con)

f.close()
