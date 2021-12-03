f = open('scores.txt',encoding='utf-8')
#取得文件中的数据。因为每一行都是一条学生成绩的记录，所以用readlines
lines =f.readlines()
f.close()
#print(lines)
#对每一条数据进行处理。按照空格，把姓名、每次的成绩分割开
results = []

for line in lines:
    #print (line)
    data = line.split()
    #print (data)

'''
4.整个程序最核心的部分到了。如何把一个学生的几次成绩合并，并保存起来呢？
我的做法是：对于每一条数据，都新建一个字符串，把学生的名字和算好的总成绩保存进去。
最后再把这些字符串一起保存到文件中：
'''
"""
注意：
对于每一行分割的数据，data[0]是姓名，data[1:]是所有成绩组成的列表。
每次循环中，sum都要先清零。
score是一个字符串，为了做计算，需要转成整数值int。
result中，我加了一个制表符\t和换行符\n，让输出的结果更好看些。
"""
    sum = 0
    #score_list = data[1:] # 学生各门课的成绩列表
    for score in data[1:]:
        point = int (score)
        sum +=  int (score)
    result = '%s\t: %d\n' %(data[0],sum) # 名字和总分
    #print(result)

    results.append(result)

#print(results)
output = open('result.txt','w',encoding='UTF-8')
output.writelines(results)
output.close()