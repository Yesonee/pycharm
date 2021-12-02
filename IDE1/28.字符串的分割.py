sentence = 'I am an English sentence'

#split() 会把字符串按照其中的空格进行分割，分割后的每一段都是一个新的字符串，最终返回这些字符串组成一个list。于是得到
a = sentence.split()
print(a)

# print(sentence.split(sentence))

section = 'Hi. I am the one. Bye.'
b = section.split('.')
print(b)

c = 'aaa'.split('a')
print(c)