"""Bai thuc hanh 1 - phan tu viet tai lop (muc A5).

Ba ham duoi day dang viet do hoac bo trong. Sua lai tung ham,
moi lan sua xong thi chay:   python tai_lop.py
roi doi chieu voi hop Moc kiem trong de.
"""

BAN_GHI = [
    ("Nguyen Van An", "24TTH", 8.5),
    ("Tran Thi Binh", "24TTH", 4.0),
    ("Le Van Chi", "25KDL", 9.0),
    ("Pham Thu Dung", "25KDL", 6.5),
    ("Hoang Minh Giang", "24TTH", 5.0),
    ("Vo Thi Ha", "25KDL", 3.5),
    ("Do Quoc Khanh", "24TTH", 7.5),
    ("Bui Lan Anh", "25KDL", 10.0),
]


def xep_loai(diem, nguong_dat=5.0):
    if diem >= 9.5:
        return "Xuat sac"
    elif diem >= 8.0:
        return "Gioi"
    elif diem >= nguong_dat:
        return "Dat"
    else:
        return "Chua dat"

def dem_theo_loai(ban_ghi, nguong_dat=5.0):
    dem = {}
    for x in ban_ghi:
        y = xep_loai(x[-1]) 
        dem[xep_loai(x[-1], nguong_dat)] = dem.get(xep_loai(x[-1], nguong_dat), 0) + 1
    
    print(dem)

def nguoi_cao_nhat(ban_ghi):
    if not ban_ghi:        
        return None

    top = max(ban_ghi, key = lambda x: x[-1])
    return top[:1] + top[2:]


if __name__ == "__main__":
    for ten, lop, diem in BAN_GHI:
        print(f"{ten:<18} {diem:>5}   {xep_loai(diem)}")
    print()
    print(dem_theo_loai(BAN_GHI))
    print(nguoi_cao_nhat(BAN_GHI))
    print(nguoi_cao_nhat([]))
    print(nguoi_cao_nhat([("Mot", "L1", 9.0), ("Hai", "L2", 9.0)]))
    print(dem_theo_loai(BAN_GHI, 7.0))