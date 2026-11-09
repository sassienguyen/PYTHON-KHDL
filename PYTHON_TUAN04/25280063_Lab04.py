TEP = "./StudentsPerformance.csv"
MON = ("toan", "doc", "viet")
NGUONG_DAT = 50

# ===================================================== BTTL
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

def gom_nhom(ds_hs, cot):
    groupBy = {}
    for hs in ds_hs:
        groupBy.setdefault(hs[cot], []).append(hs)

    return groupBy

# ===================================================== BTTL

def trung_vi(ds):
    if not ds:
        return None

    n = len(ds)
    arr = sorted(ds)
    if n&1:
        return arr[(n+1)//2 - 1]
    else:
        return round((arr[n//2 - 1]+arr[n//2])/2,2)

def tom_tat(ds):
    if not ds:
        return (0, None, None, None, None)
    
    return (
            len(ds), 
            min(ds), 
            trung_vi(ds), 
            round(sum(ds)/ len(ds), 2),
            max(ds)
            )

def loc(ds_hs, *, mon="toan", tu=0,den=100, **dieu_kien):
    ket_qua = []

    for hs in ds_hs:
        if hs[mon] < tu and hs[mon] > den:
            continue
    
        passed = True
        for cond, val in dieu_kien.items():
            if hs[cond] != val:
                passed = False
                break
        if passed:
            ket_qua.append(hs)
    
    return ket_qua

def gom_canh_bao(ds_hs, *,nguong=40, ket_qua=None):

    if ket_qua is None:
        ket_qua = []

    ket_qua = []

    for index, hs in enumerate(ds_hs, start=1):
        for mon in MON:
            if hs[mon] < nguong:
                ket_qua.append((index, hs))
    
    return ket_qua

def bang_so_sanh(ds_hs, cot, *,mon="toan"):
    ket_qua = []
    ket_qua.append(f"{'Nhom':<22}{'So HS':>6}{'TB':>8}{'Trung vi':>10}")

    groupBy = gom_nhom(ds_hs, cot)
    for group, group_ds in groupBy.items():
        scores = lay_cot(group_ds, mon)
        total, _, avgDS, medDS, _ = tom_tat(scores)
        ket_qua.append(f"{group:<22}{total:>6}{avgDS:>8}{medDS:>10}")

    return ket_qua

def xep_hang(ds_hs, mon, *, k=None):
    rank = []
    focusedDs = [(index, hs[mon]) for index, hs in enumerate(ds_hs)]
    ds = sorted(focusedDs, key = lambda x: (x[1], x[0]) ,reverse=True)

    return ds if k is None else ds[:k]
    
def bang_hai_chieu(ds_hs, cot_dong, cot_cot, *, mon="toan"):
    group = {}
    for hs in ds_hs:
        pair = (hs[cot_dong], hs[cot_cot])
        group.setdefault(pair, []).append(hs[mon])
        
    return {pair: round(sum(arr) / len(arr), 2) for pair, arr in group.items()}

if __name__ == "__main__":
    ds = doc_du_lieu(TEP)
    
    print("\nTEST")

    for i in loc(ds[:67], mon="toan", tu=50, den=100, gioi_tinh = "female"):
        print(i)

    print("\nTEST")

    for i in gom_canh_bao(ds[:90], nguong=40):
        print(i)
    
    print("\nTEST")

    for i in bang_so_sanh(ds[:90], "nhom"):
        print(i)

    print("\nTEST")
    print(xep_hang(ds, "toan", k=4))

    print("\nTEST")
    for pair, avg in bang_hai_chieu(ds, "gioi_tinh", "on_thi").items():
        print(f"{pair}: {avg}")
