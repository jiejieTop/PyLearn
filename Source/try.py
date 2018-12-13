def demo1():
    return int(input("请输入一个整数："))

def demo2():
    num = demo1()
    rst = 100/num

try:
    print(demo2())

except ValueError:
    print("请输入正确的整数")

except Exception as result:
    print("错误类型是 %s" % result)
