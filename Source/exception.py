def input_passwold():

    #提示输入密码
    pwd = input("请输入密码：")

    #判断密码的长度
    if len(pwd) >= 8:
        return pwd

    #print("主动抛出异常")
    #创建异常对象
    ex = Exception("密码长度不够")

    raise ex

try:
    print(input_passwold())

except Exception as result:
    print(result)