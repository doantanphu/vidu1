danhsachsinhvien = []
dsdiemsv = []
while (0 < 1):
    nhap = int(input("Nhập menu: \
        0: Thoát khỏi chương trình\
        1: nhập thông tin sinh viên\
        2: sắp xếp theo điểm\
        3: tìm kiếm sinh viên\
        4: hiển thị bảng điểm sinh viên"))

if(nhap == 0):
    breakpoint
if(nhap == 1):
    tensv = input("nhập tên sinh viên:")
    danhsachsinhvien.append(tensv)
    diemsv = input("nhập điểm sv: ")
    dsdiemsv.append(diemsv)
if(nhap == 2):
    dsdiemsv.sort()