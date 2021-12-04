f = open('text.txt','r')
##一次性读取一次内容
##readline()⼀次读取⼀⾏内容
con = f.readline()
print(con)

con = f.readline()
print(con)

con = f.readline()
print(con)

f.close()