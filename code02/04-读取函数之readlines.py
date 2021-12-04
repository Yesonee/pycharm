f = open('test1.txt','r')
#readlines可以按照⾏的⽅式把整个⽂件中的内容进⾏⼀次性读取，并且返回的是⼀个列表，其中每⼀⾏的数据为⼀个元素。
con = f.readlines()

print(con)

f.close()