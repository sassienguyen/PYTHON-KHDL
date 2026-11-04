def chuan_hoa_gioi_tinh(s):
    s = s.strip().lower()
    match s:
        case "female" | "f" | "nu":
            return "female"
        case "male" | "m" | "nam":
            return "male"
        case _:
            return None
        
def doc_diem(s):
    try:
        ret = int(float(s))
        if ret < 0 or ret > 100:
            return None
        return ret
    except ValueError:
        return None
    
def doc_ban_ghi(dong):
    try:
        gt, nhom, hv, an, on, t, d, v = dong.split(',')
        gt = chuan_hoa_gioi_tinh(gt)

        if gt is None:
            return None

        return {"gioi_tinh": gt, 
                "nhom": nhom,
                "hoc_van": hv,
                "an_trua": an,
                "on_thi": on,
                "toan": doc_diem(t),
                "doc": doc_diem(d),
                "viet": doc_diem(v)}
    except ValueError:
        return None

def doc_tat_ca(cac_dong):
    try:
        key = "gender,race/ethnicity,parental level of education,lunch,test preparation course,math score,reading score,writing score"
        ds = []
        skip = 0
        
        for i in cac_dong:
            clean = i.strip()
            if clean == key or clean == "":
                # skip += 1
                continue
            
            current = doc_ban_ghi(clean)
            if current is None:
                skip += 1
                continue
            else:
                ds.append(current)

        return (ds,skip)
    except ValueError:
        return None
    
def tb_theo_nhom(ds_hs, cot, mon):
    ds = {}
    for hs in ds_hs:
        if hs[mon] is None:
            continue
        ds.setdefault(hs[cot], []).append(hs[mon])

    return {group: round(sum(arr)/len(arr), 2) for group, arr in ds.items()}

def bo_trung_lap(ds_hs):
    skip = 0
    ds = []

    ds_set = set()
    for i in ds_hs:
        tmp = tuple(i.items())
        if tmp in ds_set:
            skip += 1
            continue
        ds_set.add(tmp)
        ds.append(i)

    return (ds, skip)

def bieu_do_diem(ds_hs, mon, do_rong):
    if 100 % do_rong != 0:
        return []
    
    group = {}
    graphDetail = []
    step = do_rong
    nMax = 0

    for hs in ds_hs:
        score = hs[mon]
        if score is None:
            continue

        if score == 100:
            score = 99
        
        whichTier = (score//step)*step

        group[whichTier] = group.get(whichTier, 0) + 1

    if not group:
        return None
    
    nMax = max(group.values())

    for L in range(0, 100, step):
        n = group[L]
        so_dau = (n*40)//nMax
        R = 100 if L == 100 - step else L + step - 1
        graphDetail.append(f"{L:>3}-{R:>3} | {'#' * so_dau} {n}")

    return graphDetail



if __name__ == "__main__":
    PATH = './data/hoc_sinh_ban.csv'

    with open(PATH, encoding="utf-8") as tep:
            cac_dong = tep.readlines()

    print("\nTEST01")
    ds, so_loi = doc_tat_ca(cac_dong)
    print(len(ds), so_loi)


    print("\nTEST02")
    print(tb_theo_nhom(ds, "gioi_tinh", "toan"))

    print("\nTEST03")
    noDuplicates, skip = bo_trung_lap(ds)
    print(len(noDuplicates), skip)
    print(tb_theo_nhom(ds, "gioi_tinh", "toan"))
    print(tb_theo_nhom(noDuplicates, "gioi_tinh", "toan"))

    print("\nTEST04")
    
    for i in bieu_do_diem(noDuplicates, "toan", 10):
        print(i)