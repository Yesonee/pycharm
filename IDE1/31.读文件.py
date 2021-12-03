#打开一个文件的命令
f = open('123.txt')
#变量f保存了这个文件，还需要去读取它的内容。你可以通过read()函数把文件内所有内容读进一个字符串中。
data0 = f.read()
data1 = f.readline(1)
data2 = f.readlines()
#输出
print(data0)
print(data1)
print(data2)
f.close()
