class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print(f'{self}对象已经被删除')
haier1 = Washer(10.20)

del haier1