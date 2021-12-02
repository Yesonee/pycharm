'''
今天要说的方法是join。它和昨天说的split正好相反：split是把一个字符串分割成很多字符串组成的list，而join则是把一个list中的所有字符串连接成一个字符串。
join的格式有些奇怪，它不是list的方法，而是字符串的方法。首先你需要有一个字符串作为list中所有元素的连接符，然后再调用这个连接符的join方法，join的参数是被连接的list：
'''
s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print (fruit)