"""Một vòng Python: đọc tệp điểm, tính toán, in báo cáo.

Chương trình này đi qua đủ năm nhóm kiến thức, ở mức làm quen:
    Nhóm 1. Biến, kiểu dữ liệu, toán tử
    Nhóm 2. Rẽ nhánh và vòng lặp: if/else, for, while
    Nhóm 3. Cấu trúc dữ liệu: list, tuple, dict, set
    Nhóm 4. Hàm: định nghĩa, tham số, return, phạm vi biến
    Nhóm 5. Nhập/xuất: input(), print(), đọc tệp văn bản
Hôm nay chỉ cần chạy được, và nhận ra từng nhóm nằm ở đâu.
Các bài 3 đến 7 sẽ quay lại từng nhóm, kỹ hơn.

CÁCH CHẠY
    1. VS Code: File > Open Folder, chọn thư mục mot_vong_python.
    2. Terminal > New Terminal, rồi gõ:  python mot_vong_python.py
    3. Chương trình hỏi ngưỡng điểm đạt: nhấn Enter để dùng 5.0.
Tệp diem.txt phải nằm cùng thư mục với tệp này.
"""


# ==================================================================
# Nhóm 4 - HÀM: đặt tên cho một việc để dùng lại nhiều lần
# ==================================================================

def xep_loai(diem, nguong_dat):
    """Trả về xếp loại của một điểm."""
    if diem >= 8.0:
        ket_qua = "Gioi"
    elif diem >= nguong_dat:
        ket_qua = "Dat"
    else:
        ket_qua = "Chua dat"
    return ket_qua      # ket_qua chỉ tồn tại trong hàm


def trung_binh(cac_so):
    """Trả về trung bình cộng của một danh sách số."""
    tong = 0.0
    for so in cac_so:
        tong = tong + so
    return tong / len(cac_so)


# ==================================================================
# Nhóm 5 - NHẬP: hỏi người dùng một con số
# ==================================================================

# input() luôn trả về chuỗi (str), kể cả khi gõ số
tra_loi = input("Nhap nguong diem dat (Enter = 5.0): ")
if tra_loi == "":
    nguong_dat = 5.0
else:
    nguong_dat = float(tra_loi)     # đổi chuỗi thành số thực


# ==================================================================
# Nhóm 5 - ĐỌC TỆP   +   Nhóm 3 - LIST và TUPLE
# ==================================================================

ban_ghi = []                        # list rỗng, sẽ chứa các tuple
with open("diem.txt", encoding="utf-8") as tep:
    for dong in tep:                # mỗi vòng đọc một dòng
        ten, lop, diem_chu = dong.strip().split(";")
        # mỗi sinh viên là một tuple gồm 3 phần tử
        ban_ghi.append((ten, lop, float(diem_chu)))


# ==================================================================
# Nhóm 1 - BIẾN, KIỂU, TOÁN TỬ   +   Nhóm 3 - SET và DICT
# ==================================================================

so_sinh_vien = len(ban_ghi)         # int
cac_diem = []                       # list các số thực
cac_lop = set()                     # set: tự bỏ phần tử trùng
diem_theo_lop = {}                  # dict: lớp -> list điểm

for ten, lop, diem in ban_ghi:
    cac_diem.append(diem)
    cac_lop.add(lop)
    if lop not in diem_theo_lop:
        diem_theo_lop[lop] = []
    diem_theo_lop[lop].append(diem)

so_dat = 0
for diem in cac_diem:
    dat = diem >= nguong_dat        # bool: True hoặc False
    if dat:
        so_dat = so_dat + 1
ti_le_dat = so_dat / so_sinh_vien * 100


# ==================================================================
# Nhóm 5 - XUẤT: in báo cáo
# ==================================================================

print()
print("===== BAO CAO DIEM =====")
print("So sinh vien :", so_sinh_vien)
print("Cac lop      :", sorted(cac_lop))
print("Nguong dat   :", nguong_dat)
# :.2f nghĩa là lấy 2 chữ số sau dấu thập phân
print(f"Trung binh   : {trung_binh(cac_diem):.2f}")
print(f"Ti le dat    : {ti_le_dat:.1f}%")
print()

for ten, lop, diem in ban_ghi:
    loai = xep_loai(diem, nguong_dat)
    # :<18 là canh trái trong 18 ô, :>5 là canh phải trong 5 ô
    print(f"{ten:<18} {lop:<6} {diem:>5}   {loai}")
print()

for lop in sorted(diem_theo_lop):
    print("Lop", lop, "- trung binh", trung_binh(diem_theo_lop[lop]))


# ==================================================================
# Nhóm 2 - WHILE: lặp khi chưa biết trước phải lặp bao nhiêu lần
# ==================================================================

diem_thap_nhat = min(cac_diem)
so_lan = 0
while diem_thap_nhat < nguong_dat:
    diem_thap_nhat = diem_thap_nhat + 0.5
    so_lan = so_lan + 1
print()
print("Diem thap nhat can cong 0.5 diem", so_lan, "lan thi dat.")
