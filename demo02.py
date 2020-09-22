# a=1
# b=2
# if a>b:
#     print("a大")    
# else:
#     print("b大")

# age=int(input("请输入你的年龄："))

# if age>60:
#     print("退休！")
# elif age>30:
#     print("累吧")
# elif age>20:
#     print("找工作")
# else:
#     print("读书")

# a=input("请输入：")
# if a in "0123456789":
#     a=int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()
# if a>5:
#     print("大")
# else:
#     print("小")

# a=100
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# a=1
# while a<10:
#     print("嘻嘻嘻嘻",a) 
#     a=a+1

# a=["阿斯蒂芬","玩儿","很关键","从v","UI哦"]
# for i in a:
#     print(i)

# b=list(range(0,100,4))#4是步长
# print(b)

# for i in range(10):
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end=" ")
#     print()#每次print都会自动换行

# a=["阿斯蒂芬","玩儿","很关键","从v","UI哦"]
# for i in a:
    # print(i)

# while 2:
#     for i in range(1,31):
#         print("红灯还有",31-i,"秒结束")
#     for j in range(1,36): 
#         print("绿灯还有",36-j,"秒结束")
#     for k in range(1,4):
#         print("黄灯还有",4-k,"秒结束")

# light={"红灯":30,"绿灯":35,"黄灯":3}
# for i in light:
#     for j in range(light[i]):#range默认从0开始
#         print(i,"倒计时还有",light[i]-j,"秒")

# username=input("请输入账号：")
# password=input("请输入密码：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "erwqazxcvtyughjbnmopl":
#         if len(password)>=8 and len(password)<=12:
#             print("注册成功！",{username:password})
#         else:
#             print("密码必须8-12位！")
#     else:
#         print("账号的首字母必须小写字母开头！")
# else:
#     print("账号的长度不符合规范，请输入5-8位的账号！")

# for i in range(10):
#     if i==4:
#         continue
#     print(i)
    
def checkname(username):
    """
    账号5-8位，首字母小写
    """
    if len(username)>=5 and len(username)<=8:
        if username[0] in "erwqafdszxcvtyughjbnmopl":
            return True
        else:
            return("账号的首字母必须小写字母开头！")
    else:
        return("账号的长度不符合规范，请输入5-8位的账号！")

username=input("")
password=input("")
if checkname(username)==True:
    if len(password)
# def jiafa(a,b):
#     if type(a) is int and type(b) is int:
#         return(a+b)
#     else:
#         return("不对")

# # a=[]
# # print(a.append("哈哈"))
# print(jiafa(1,1))


