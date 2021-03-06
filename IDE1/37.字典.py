'''
字典这种数据结构有点像我们平常用的通讯录，有一个名字和这个名字对应的信息。在字典中，名字叫做“键”，对应的内容信息叫做“值”。字典就是一个键/值对的集合。
它的基本格式是（key是键，value是值）：
'''

#d = {key1 : value1, key2 : value2}
'''
键/值对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号中。
1.键必须是唯一的；
2.键只能是简单对象，比如字符串、整数、浮点数、bool值。
list就不能作为键，但是可以作为值。
'''

score ={
    '晓峰': 95,
    '段誉': 97,
    '虚竹': 89
}
#print (score['段誉'])
#注意，如果你的键是字符串，通过键访问的时候就需要加引号，如果是数字作为键则不用

for name in score:
   print (score[name])

score.get('波波')
score['波波'] = 91
score['慕容复'] = 88

for name in score:
    print(name,score[name])