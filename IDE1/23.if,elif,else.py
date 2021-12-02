# a = int(input())
# if a == 1:
#     print('right')
# else:
#     print('wrong')

'''
if, elif, else 可组成一个整体的条件语句。

if 是必须有的；
elif 可以没有，也可以有很多个，每个elif条件不满足时会进入下一个elif判断；一旦满足，执行完就结束整个条件语句；
else 可以没有，如果有的话只能有一个，必须在条件语句的最后。
'''
# print('Pelase input number')
# a = int(input())
# if a == 1:
#     print('none')
# elif a == 2:
#     print('two')
# elif a == 3:
#     print('three')
# else:
#     print('too many')

#==我们昨天刚改写的小游戏中的函数 isEqual，用了三个条件判断，我们可以再改写成一个包含 if...elif...else 的结构：==#

def isEqual(num1,num2):
    if num1<num2:
        print('too small')
        return False;
    elif num1>num2:
        print('too big')
        return  False;
    else:
        print('bingo')
        return True

    from random import randint
    num = randint(1, 100)
    print('Guess what I think?')
    bingo = False
    while bingo == False:
        answer = int(input())
        bingo = isEqual(answer, num)