for x in range(5):
    print(x)
else:
    print("Vòng lặp kết thúc tại x = {}".format(x))


danhsachsinhvien = ["phu","linh","minh","dat","phat"]
for sinhvien in danhsachsinhvien:
    print(sinhvien)

for char in danhsachsinhvien[0]:
    print(char)

tong = 0
for i in range(11):
    tong = tong + i

print(f"Tổng từ 0-10 là: {tong}")