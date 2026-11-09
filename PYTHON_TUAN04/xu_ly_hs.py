"""Cac ham xu ly du lieu diem thi - Bai thuc hanh 4.

Moi muc gom: MA MAU (go lai tu de, chay thu) va cac ham CAN VIET.
Moi lan sua xong mot ham thi chay:   python xu_ly_hs.py
"""

TEP = "./StudentsPerformance.csv"
MON = ("toan", "doc", "viet")
NGUONG_DAT = 50


# ===================================================== DA VIET SAN
def doc_du_lieu(duong_dan):
    """Doc tep CSV thanh list cac dict, moi dict la mot hoc sinh."""
    ds = []
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()
        for dong in tep:
            gt, nhom, hv, an, on, t, d, v = dong.strip().split(",")
            ds.append({"gioi_tinh": gt, "nhom": nhom, "hoc_van": hv,
                       "an_trua": an, "on_thi": on,
                       "toan": int(t), "doc": int(d), "viet": int(v)})
    return ds


# ===================================================== A2
def lay_cot(ds_hs, mon):
    cot = []
    for hs in ds_hs:
        cot.append(hs[mon])

    return cot


def thong_ke(ds: list) -> tuple:
    return min(ds), max(ds), round(sum(ds)/ len(ds), 2)

def do_lech_chuan(ds):

    avg = sum(ds)/len(ds)
    diff = [(x - avg)**2 for x in ds]

    return round((sum(diff)/len(diff))**0.5, 2)

def ti_le_dat(ds, nguong=NGUONG_DAT):
    passed = [x for x in ds if x >= nguong]
    
    return round(len(passed)/ len(ds), 3)

def thong_ke_mon(ds_hs, mon):
    ds_mon = [hs[mon] for hs in ds_hs]
    minDS, maxDS, avgDS = thong_ke(ds_mon)
    return  minDS, maxDS, avgDS, do_lech_chuan(ds_mon), ti_le_dat(ds_mon)
    

# ===================================================== A3
def loc_hoc_sinh(ds_hs, *, gioi_tinh=None, on_thi=None):
    ket_qua = []
    for hs in ds_hs:
        if gioi_tinh is not None and hs["gioi_tinh"] != gioi_tinh:
            continue
        if on_thi is not None and hs["on_thi"] != on_thi:
            continue
        ket_qua.append(hs)

    return ket_qua

def diem_tb_hs(hs, *cac_mon):
    """Trung binh cac mon duoc chi ra cua mot hoc sinh, lam tron 2;
    khong chi ra mon nao thi lay ca ba mon."""

    ds_mon = cac_mon if len(cac_mon) > 0 else MON
    ds_diem = [hs[mon] for mon in ds_mon]

    return round(sum(ds_diem)/len(ds_diem),2)

def danh_sach_yeu(ds_hs, nguong=40, ket_qua=None):
    ket_qua = []

    for index, hs in enumerate(ds_hs, start=1):
        passed = True
        for mon in MON:
            if hs[mon] < nguong:
                passed = False
        if not passed:
            ket_qua.append(index)

    return ket_qua


# ===================================================== A4

def hoc_sinh_co_100_toan(ds_hs):
    return [hs for hs in ds_hs if hs.get("toan") == 100]


def dat_ca_ba(hs):
    return all([hs["toan"] >= NGUONG_DAT,
                hs["doc"] >= NGUONG_DAT, hs["viet"] >= NGUONG_DAT])


def co_diem_100(hs):
    return any([hs["toan"] == 100, hs["doc"] == 100, hs["viet"] == 100])

def top_diem(ds_hs, mon, k=5):
    ds_diem = lay_cot(ds_hs, mon)
    return sorted(ds_diem, reverse=True)[:k]

# ===================================================== A5
def gom_nhom(ds_hs, cot):
    groupBy = {}
    for hs in ds_hs:
        groupBy.setdefault(hs[cot], []).append(hs)

    return groupBy

def bang_theo_nhom(ds_hs, cot, mon):
    groupBy = gom_nhom(ds_hs, cot)
    table = []

    for group, ds in groupBy.items():
        _, _, avgDS, std, rate = thong_ke_mon(ds, mon)
        table.append((group, len(ds), avgDS, std, rate))

    return table

if __name__ == "__main__":
    ds = doc_du_lieu(TEP)
    print("--- A2")
    print(thong_ke([8.5, 4.0, 6.5, 9.0]), do_lech_chuan([8.5, 4.0, 6.5, 9.0]))
    print(ti_le_dat([45, 50, 72, 30]), ti_le_dat([45, 50, 72, 30], nguong=40))
    for mon in MON:
        print(mon, thong_ke_mon(ds, mon))
    print("--- A3")
    print(len(loc_hoc_sinh(ds, gioi_tinh="female")),
          len(loc_hoc_sinh(ds, gioi_tinh="male", on_thi="completed")),
          len(loc_hoc_sinh(ds)))
    print(diem_tb_hs(ds[0]), diem_tb_hs(ds[0], "toan"), diem_tb_hs(ds[0], "doc", "viet"))
    print(len(danh_sach_yeu(ds)), len(danh_sach_yeu(ds)), danh_sach_yeu(ds, 20))
    print("--- A4")
    dem_ca_ba, dem_100 = 0, 0
    for hs in ds:
        dem_ca_ba += dat_ca_ba(hs)
        dem_100 += co_diem_100(hs)
    print(dem_ca_ba, dem_100)
    print(top_diem(ds, "toan", k=9), top_diem(ds, "viet", k=3))
    
    print("Students with math score 100:", len(hoc_sinh_co_100_toan(ds)))

    print("--- A5")
    for dong in bang_theo_nhom(ds, "an_trua", "toan"):
        print(dong)


