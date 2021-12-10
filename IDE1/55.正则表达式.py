# print('\bhi')
# print(r'\bhi')
# print(r'\\bhi')
# print ("\\bhi")
import re


def regexFlag():
    '''
    演示re模块常量的使用
    :return:
    '''
    # 1 re
    test = 'Yeson大帅比b'
    pattern = r'Yeson大帅比B'
    print('默认模式', re.findall(pattern, test))
    print('忽略大小写 模式', re.findall(pattern, test, re.IGNORECASE))
