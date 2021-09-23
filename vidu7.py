import random
#a = ramdom.randint(0,2)
print("mời bạn đoán:")
a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
if a>b and b>c:
    print("a là số lớn nhất: " +str(a))
elif b>c and b>a:
    print("b là số lớn nhất: " +str(b))
else:
     print("c là số lớn nhất: " +str(c))
