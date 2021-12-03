''''
打开文件；
把内容写入文件；
关闭文件。
'''
data = 'I will be in a file.\nSo cool!'
data1 = 'I will better'
'''
'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。
之前不加参数时，open的模式默认为'r'，reading，只读模式，文件必须存在，否则引发异常。
还有一种常用模式是'a'，appending。它也是一种写入模式，但你写入的内容不会覆盖之前的内容，而是添加到原有文件内容后面。
'''
# out = open('output.txt', 'a')
# f1=out.write(data)
# out = open('output.txt','a')
# f2=out.write(data1)
# out.close()

f = open('output.txt')
data0 = f.read()
print(data0)
f1 = open('123.txt','w')
f.close()