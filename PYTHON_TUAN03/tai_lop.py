TEP = "PYTHON_TUAN03/data/StudentsPerformance.csv"


# ===================================================== DA VIET SAN
def doc_du_lieu(duong_dan):
    ds = []
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()                       # bo dong tieu de
        for dong in tep:
            gt, nhom, hv, an, on, t, d, v = dong.strip().split(",")
            ds.append({"gioi_tinh": gt, "nhom": nhom, "hoc_van": hv,
                       "an_trua": an, "on_thi": on,
                       "toan": int(t), "doc": int(d), "viet": int(v)})
    return ds


# ===================================================== A2 - re nhanh
def can_ho_tro(hs):
    kho_khan = hs["an_trua"] == "free/reduced" and hs["on_thi"] == "none"
    co_mon_yeu = hs["toan"] < 40 or hs["doc"] < 40 or hs["viet"] < 40
    return kho_khan or co_mon_yeu      

def xep_loai(diem):
    if diem >= 90:
        return "A"
    elif diem >= 80:
        return "B"
    elif diem >= 70:
        return "C"
    elif diem >= 50:
        return "D"
    else:
        return "F"


def bac_hoc_van(muc):
    match muc:
        case "some high school" | "high school":
            return 1
        case "some college" | "associate's degree":
            return 2
        case "bachelor's degree":
            return 3
        case "master's degree":
            return 4
        case _:
            return None
        
# ===================================================== A3 - list, tuple, dict, set
def mau_phuong_thuc(ds_hs):
    diem_toan = []

    for hs in ds_hs:
        diem_toan.append(hs["toan"]) 

    print(len(diem_toan), diem_toan.count(100), diem_toan.index(100)+1)
    diem_toan.sort()

    print(diem_toan[:5], diem_toan[-3:])

    nu, dat_toan = set(), set()

    for index, hs in enumerate(ds_hs, start=1):
        if hs["gioi_tinh"] == "female":
            nu.add(index)
        if hs["toan"] >= 50:
            dat_toan.add(index)

    print(len(nu & dat_toan), len(nu - dat_toan), len(nu | dat_toan))

    dem = {}
    for hs in ds_hs:
        khoa = (hs["gioi_tinh"], hs["an_trua"])
        dem[khoa] = dem.get(khoa, 0) + 1

    for khoa, n in sorted(dem.items()):
        print(khoa, n)

    toan_theo_nhom = {}
    for hs in ds_hs:
        toan_theo_nhom.setdefault(hs["nhom"], []).append(hs["toan"])

    nhom_a = toan_theo_nhom["group A"]
    print(sorted(toan_theo_nhom), len(nhom_a), max(nhom_a))


def top_k(ds_hs, mon, k):
    ds_mon = [i[mon] for i in ds_hs]
    ds_mon.sort()
    return sorted(ds_mon, reverse=True)[:k]


def gioi_ca_ba(ds_hs, nguong):
    math, read, write = set(), set(), set()

    for index, hs in enumerate(ds_hs, start=1):
        if hs["toan"] >= nguong:
            math.add(index)
        if hs["doc"] >= nguong:
            read.add(index)
        if hs["viet"] >= nguong:
            write.add(index)

    all = math & read & write
    onlyMath = math - read - write
    return (all, onlyMath)


def gom_theo(ds_hs, cot):
    ret = {}
    for index, hs in enumerate(ds_hs, start=1):
        ret.setdefault(hs[cot], []).append(index)

    return ret


# ===================================================== A4 - nam mau lap
def tom_tat_mon(ds_hs, mon):
    dat, tong = 0, 0
    for hs in ds_hs:
        tong += hs[mon]
        dat += (hs[mon] >= 50)

    return (dat, round(tong/len(ds_hs),2))


def cao_nhat(ds_hs, mon):
    ds = [(index, hs[mon]) for index, hs in enumerate(ds_hs, start=1)]

    return sorted(ds, key=lambda x: x[1], reverse= True)[0]

def tb_theo_nhom(ds_hs, cot, mon):
    ds = {}
    for hs in ds_hs:
        ds.setdefault(hs[cot], []).append(hs[mon])

    return {group: round(sum(arr)/len(arr), 2)  for group, arr in ds.items()}


# ===================================================== A5 - while, break
def vi_tri_dau_tien(ds_hs, dieu_kien):
    for index, hs in enumerate(ds_hs, start=1):
        if can_ho_tro(hs) == dieu_kien:
            return index
    
    return None

def diem_cong_can_thiet(ds_hs, mon, ti_le):
    ds = [hs[mon] for hs in ds_hs]
    n = len(ds)

    need = sorted(ds)[n - round(ti_le * n)]
    return 0 if need >= 50 else 50 - need

if __name__ == "__main__":
    ds = doc_du_lieu(TEP)
    print("So hoc sinh:", len(ds))
    
    print("--- A2")
    print(can_ho_tro(ds[3]), can_ho_tro(ds[0]))
    print([xep_loai(d) for d in (95, 90, 85, 70, 50, 49, 0)])
    print([bac_hoc_van(m) for m in ("high school", "master's degree", "college")])
    
    print("--- A3 mau")
    mau_phuong_thuc(ds)
    
    print("--- A3")
    print(top_k(ds, "toan", 10), top_k(ds, "doc", 0))
    ca_ba, chi_toan = gioi_ca_ba(ds, 90)
    print(len(ca_ba), sorted(ca_ba)[:5], len(chi_toan))
    nhom = gom_theo(ds, "on_thi")
    print(sorted(nhom), len(nhom.get("completed", [])), nhom.get("completed", [])[:5])
    
    print("--- A4")
    print(tom_tat_mon(ds, "toan"))
    for mon in ("toan", "doc", "viet"):
        print(mon, cao_nhat(ds, mon))
    print(tb_theo_nhom(ds, "on_thi", "toan"))
    print(tb_theo_nhom(ds, "hoc_van", "viet"))
    
    print("--- A5")
    print(vi_tri_dau_tien(ds, True), vi_tri_dau_tien(ds, False))
    print(diem_cong_can_thiet(ds, "toan", 0.95))
