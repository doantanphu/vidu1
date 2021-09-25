tongtien= int(input("số tiền đã có:"))
songuoidonggop=0
while tongtien <= 100000:
    donggop = int(input("mời bạn đóng góp tiền uống cf: "))
    tongtien +=donggop
    songuoidonggop+=1
else:
    print("đủ tiền rồi quyên góp gì nữa?")
print("đã quyên góp đươc {} từ{} người!".format(tongtien, songuoidonggop))