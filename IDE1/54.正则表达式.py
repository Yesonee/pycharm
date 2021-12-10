import  re
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r'hi',text)
# if m:
#     print(m)
# else:
#     print('not match')


s = re.findall(r'l.*e',text)
print(s)
d = re.findall(r'.*',text)
print(d)