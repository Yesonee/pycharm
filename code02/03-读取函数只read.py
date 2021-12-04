f = open('test1.txt', 'r')

# 文件内容如果有换行，底层有\n,会有字节占位，导致read书写参数读取出来的个数和参数值不匹配
# read不写参数表示读取所有
# print(f.read())
print(f.read(2))

f.close()
