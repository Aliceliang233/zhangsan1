"""
print("你好")
print("呱呱"*100)
"""

# a=float(input("请输入："))
# b=float(input("请输入："))
# print("内容：",a+b)

# print(type(9.8))
# print(type(()))
# print(type({}))
# print(type([]))

# a=input("请输入：")
# b=input("请输入：")
# print(len(a)+len(b))

# a=[1,2,3,4,"guagua","切切",True,False]
# a.remove(1)
# print(a)
# a.append("jiujiu")
# print(a)

# a.insert(5,"first")
# print(a)
# b=a.pop(5)
# print(a)
# print(b)

# xx=["你很拽哦","不拽"]
# a.extend(xx)
# print(a)
# print(a+xx)
# a.clear()
#print(a)
# print(a[-2])
# print(a[:4])
# print(a[4:])

# print(a.index("guagua"))
# print(a.count("guagua"))

# b=(a,"sdf","wer")
# print(b[0][3])

# a={"name":"张三",0:"哈哈","age":25}
# print(a["name"])
# a["high"]="188cm"
# print(a)
# a["name"]="李四"
# print(a)

name=input("输入姓名：")
age=input("输入年龄：")
sex=input("输入性别：")
userinfo={}
userinfo.update(name=name,sex=sex,age=age)
print(userinfo)
