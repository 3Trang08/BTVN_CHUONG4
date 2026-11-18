# Nhap so luong sinh vien n (dieu kien n > 0)
n = int(input("Nhap so luong sinh vien n: "))
while n <= 0:
    n = int(input("So luong sinh vien phai lon hon 0. Nhap lai n: "))
# 1. Luu cac diem vao List
diem_sv = []
for i in range(n):
    diem = float(input(f"Nhap diem sinh vien thu {i + 1} (tu 0 den 10): "))
    while diem < 0 or diem > 10:
        diem = float(input("Diem khong hop le! Nhap lai (tu 0 den 10): "))
    diem_sv.append(diem)
print("KET QUA THONG KE")
print("Danh sach diem:", diem_sv)
# 2. Tinh tong va diem trung binh
tong_diem = sum(diem_sv)
diem_tb = tong_diem / n
print("Tong diem:", tong_diem)
print(f"Diem trung binh: {diem_tb:.2f}")
# 3. Tim diem cao nhat, thap nhat
print("Diem cao nhat:", max(diem_sv))
print("Diem thap nhat:", min(diem_sv))
# 4. Dem so sinh vien dat (diem >= 5)
so_sv_dat = 0
for d in diem_sv:
    if d >= 5:
        so_sv_dat += 1
print("So sinh vien dat:", so_sv_dat)
# 5. Dem so sinh vien khong dat
so_sv_khong_dat = n - so_sv_dat
print("So sinh vien khong dat:", so_sv_khong_dat)