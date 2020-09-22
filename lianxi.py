highgrade={}
lowgrade={}
studentlist=["阿斯蒂芬","玩儿","很关键","从v","UI哦"]
for i in studentlist:
    grade=int(input("请输入"+i+"的成绩："))
    if grade>=60:
        highgrade[i]=grade
    else:
        lowgrade[i]=grade
print("大于60的：",highgrade)
print("小于60的：",lowgrade)