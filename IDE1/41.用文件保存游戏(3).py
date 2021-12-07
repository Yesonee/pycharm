'''
你的小游戏现在已经可以保存成绩了，但只有一组成绩，不管谁来玩，都会算在里面。所以今天我还要加上一个更多的功能：存储多组成绩。玩家需要做的就是，在游戏开始前，输入自己的名字。而我会根据这个名字记录他的成绩。这个功能所用到的内容我们几乎都说过，现在要把它们结合起来
'''
from  random import randint

name = input('请输入你的名字： ') #输入玩家名字

f = open('game2.txt',encoding='UTF-8')
lines = f.readlines()
f.close()
scores = {} #初始化一个空字典
for l in lines:
  s = l.split() #把每一行的数据拆分成list
  scores[s[0]] = s[1:] #第一项作为key，剩下的作为value
  score = scores.get(name) #找到当前玩家的数据
if score is None: #如果没找到
 score = [0,0,0]

game_times = int(score[0])  #总游戏次数
min_times = int(score[1])   #最快猜出的轮数
total_times = int(score[2]) #记录总轮数
if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0
#加上显示玩家的名字
print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' %(
    name,game_times,min_times,avg_times
))

num = randint(1,100)
times = 0 #记录本次游戏轮数
print('Guess what I think')
bingo = False
while bingo == False:
    times += 1 #轮数＋1
    answer = int(input())
    if answer < num:
        print('too small')
    if answer > num:
        print('too big')
    if answer == num:
        print('BINgo')
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times  += 1

#把成绩更新到对应的玩家数据中
#加str转成字符串，为后面的格式化做准备
scores[name] = [str(game_times),str(min_times),str(total_times)]
result = '' #初始化一个空字符串，用来存储数据
for n in scores:
    #把数据按照“name game_times min_times total_times”格式化
    #结尾要加上\n换行
    line = n + '' + ''.join(scores[n]) + '\n'
    result += line #添加到result中

f = open ('game2.txt','w',encoding='gbk')
f.write(result)
f.close()
