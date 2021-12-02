#1、遍历
word = 'helloworld'
for c in word:
    print(c)
#2、索引访问
print(word[0])
print(word[-2])

#3、切片
#通过两个参数，截取一段子串，具体规则和list相同
print(word[5:7])
print(word[:-5])
print(word[:])

#4、连接字符
#join方法也可以对字符串使用，作用就是用连接符把字符串中的每个字符重新连接成一个新字符串
news = ','.join(word)