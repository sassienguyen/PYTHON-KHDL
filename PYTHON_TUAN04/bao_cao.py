import xu_ly_hs as proc

TEP = "./StudentsPerformance.csv"
MON = ("toan", "doc", "viet")
NGUONG_DAT = 50

def pLine(group, size, avgDS, std, rate):
    print(f"{group:<20}{size:>10}{avgDS:>10.2f}{std:>10.2f}{rate:>10.1%}")

if __name__ == "__main__":
    ds = proc.doc_du_lieu(TEP)

    cot = "hoc_van"
    mon = "toan"

    print(f"{'Nhom':<20}{'So HS':>10}{'TB':>10}{'DLC':>10}{'Dat':>10}")

    _, _, tb, dlc, tl = proc.thong_ke_mon(ds, mon)
    pLine("Tat ca", len(ds), tb, dlc, tl)
    
    ds_nu = proc.loc_hoc_sinh(ds, gioi_tinh="female")
    _, _, tb_nu, dlc_nu, tl_nu = proc.thong_ke_mon(ds_nu, mon)

    pLine("Nu", len(ds_nu), tb_nu, dlc_nu, tl_nu)
    
    ds_nam = proc.loc_hoc_sinh(ds, gioi_tinh="male")
    _, _, tb_nam, dlc_nam, tl_nam = proc.thong_ke_mon(ds_nam, mon)

    pLine("Nam", len(ds_nam), tb_nam, dlc_nam, tl_nam)
    
    print()

    table = sorted(proc.bang_theo_nhom(ds, cot, mon))
    for group, size, avgDS, std, rate in table:
        pLine(group, size, avgDS, std, rate)