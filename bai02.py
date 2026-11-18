
diem_mon_hoc = {
    "Toan": 8.5,
    "Tin": 9.0,
    "Anh": 7.5,
    "Ly": 6.0,
    "Hoa": 8.0
}
# 1. Hien thi ten va diem tung mon
print("1. Danh sach diem tung mon:")
for mon, diem in diem_mon_hoc.items():
    print(f" - {mon}: {diem}")
# 2. Tinh diem trung binh
diem_tb = sum(diem_mon_hoc.values()) / len(diem_mon_hoc)
print(f"\n2. Diem trung binh cac mon: {diem_tb:.2f}")
# 3. Tim mon co diem cao nhat va thap nhat
mon_cao_nhat = max(diem_mon_hoc, key=diem_mon_hoc.get)
mon_thap_nhat = min(diem_mon_hoc, key=diem_mon_hoc.get)
print(f"\n3. Mon co diem cao nhat: {mon_cao_nhat} ({diem_mon_hoc[mon_cao_nhat]})")
print(f"   Mon co diem thap nhat: {mon_thap_nhat} ({diem_mon_hoc[mon_thap_nhat]})")
# 4. Dem so mon co diem tu 8 tro len
so_mon_tren_8 = 0
for diem in diem_mon_hoc.values():
    if diem >= 8.0:
        so_mon_tren_8 += 1
print(f"\n4. So mon co diem tu 8 tro len: {so_mon_tren_8}")
# 5. Hien thi cac mon co diem duoi 7
print("\n5. Cac mon co diem duoi 7:")
for mon, diem in diem_mon_hoc.items():
    if diem < 7.0:
        print(f" - {mon}: {diem}")