f = open('game.txt')
score = f.read().split()
#为便于理解，把数据读进来后，分别存在3个变量中
game_times = int(score[0])  #总游戏次数
min_times = int(score[1])   #最快猜出的轮数
total_times = int(score[2]) #记录总轮数

#平均轮数根据总轮数和游戏次数相除得到
if game_times > 0:
   avg_times = total_times / game_times
else:
   avg_times = 0
    print('你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (game_times, min_times, avg_times))

num = randint (1,100)
    print('Guess what I think?')
bingo = False
while bingo == False:
    answer = int(input())
    if answer < num:
        print('too small')
    if answer > num:
        print('too big')
    if answer == num:
        print('BINgo')
        bingo = True
