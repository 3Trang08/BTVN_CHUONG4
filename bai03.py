
fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "mango", "orange"]
# 1. Su dung Dictionary de dem so lan xuat hien cua tung loai qua
dem_qua = {}
for fruit in fruits:
    if fruit in dem_qua:
        dem_qua[fruit] += 1
    else:
        dem_qua[fruit] = 1
# 2. Hien thi ket qua thong ke
print("2. Ket qua thong ke so lan xuat hien:")
for fruit, so_lan in dem_qua.items():
    print(f" - {fruit}: {so_lan} lan")
# 3. Tim loai qua xuat hien nhieu nhat
max_lan = max(dem_qua.values())
print("\n3. Loai qua xuat hien nhieu nhat:")
for fruit, so_lan in dem_qua.items():
    if so_lan == max_lan:
        print(f" - {fruit} ({so_lan} lan)")