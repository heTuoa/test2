def test01():
    a = 2
    test02(a)
    print(a)

def test02(x):
    x = x * 2 + 3
    if x < 10:
        test02(x)
    x = x * 2 + 3
    print()
    print(x)
a = 1
b = 2
c = 3
def test03(x, y):
    x = x*2
    y = y+2
    global c
    c = x+y

def test04():
    test03(a, a+b)
    print(a,b,c)

if __name__ == '__main__':
    test04()
    #哈哈哈哈
    #测试下pycharm的git



