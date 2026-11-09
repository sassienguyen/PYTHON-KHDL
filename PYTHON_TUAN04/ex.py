# Các hàm xử lý dữ liệu - Phần B (Bài thực hành 4)
# Tên tệp: ex.py (tương đương <MSSV>_lab04.py)

MON = ("toan", "doc", "viet")

def doc_du_lieu(duong_dan):
    """Đọc tệp CSV thành danh sách các dict học sinh."""
    ds = []
    try:
        with open(duong_dan, encoding="utf-8") as tep:
            tep.readline()
            for dong in tep:
                gt, nhom, hv, an, on, t, d, v = dong.strip().split(",")
                ds.append({"gioi_tinh": gt, "nhom": nhom, "hoc_van": hv,
                           "an_trua": an, "on_thi": on,
                           "toan": int(t), "doc": int(d), "viet": int(v)})
    except FileNotFoundError:
        pass
    return ds

def trung_vi(ds):
    """Tính trung vị của danh sách số, không làm thay đổi danh sách gốc."""
    if not ds:
        return None
    ds_sap = sorted(ds)
    n = len(ds_sap)
    giua = n // 2
    if n % 2 == 0:
        return (ds_sap[giua - 1] + ds_sap[giua]) / 2
    return ds_sap[giua]

def tom_tat(ds):
    """Trả về (số phần tử, min, trung vị, trung bình, max) của một danh sách."""
    if not ds:
        return (0, None, None, None, None)
    return (len(ds), min(ds), trung_vi(ds), round(sum(ds) / len(ds), 2), max(ds))

def loc(ds_hs, *, mon="toan", tu=0, den=100, **dieu_kien):
    """Lọc danh sách học sinh theo điểm số và các điều kiện cột linh hoạt."""
    ket_qua = []
    for hs in ds_hs:
        if tu <= hs[mon] <= den and all(hs[k] == v for k, v in dieu_kien.items()):
            ket_qua.append(hs)
    return ket_qua

def gom_canh_bao(ds_hs, *, nguong=40, ket_qua=None):
    """Thêm (số thứ tự, tên môn) cho các môn có điểm dưới ngưỡng."""
    if ket_qua is None:
        ket_qua = []
    for i, hs in enumerate(ds_hs, start=1):
        for m in MON:
            if hs[m] < nguong:
                ket_qua.append((i, m))
    return ket_qua

def gom_nhom(ds_hs, cot):
    """Hàm phụ: Nhóm học sinh theo một cột, trả về dict."""
    nhom = {}
    for hs in ds_hs:
        nhom.setdefault(hs[cot], []).append(hs)
    return nhom

def bang_so_sanh(ds_hs, cot, *, mon="toan"):
    """Trả về danh sách các dòng so sánh điểm môn học giữa các nhóm."""
    nhom_dict = gom_nhom(ds_hs, cot)
    bang = [f"{'Nhom':<22}{'So HS':>6}{'TB':>8}{'Trung vi':>10}"]
    
    for ten_nhom in sorted(nhom_dict.keys()):
        ds_diem = [hs[mon] for hs in nhom_dict[ten_nhom]]
        sl, _, tv, tb, _ = tom_tat(ds_diem)
        bang.append(f"{ten_nhom:<22}{sl:>6}{tb:>8.2f}{tv:>10.1f}")
        
    return bang

def xep_hang(ds_hs, mon, *, k=None):
    """Xếp hạng học sinh theo điểm môn học (giảm dần)."""
    # Sắp xếp theo tuple (-điểm, số thứ tự) để điểm giảm dần, STT tăng dần
    mang = [(i, hs[mon]) for i, hs in enumerate(ds_hs, start=1)]
    mang.sort(key=lambda x: (-x[1], x[0]))
    return mang if k is None else mang[:k]

def bang_hai_chieu(ds_hs, cot_dong, cot_cot, *, mon="toan"):
    """Bảng điểm trung bình theo sự kết hợp của 2 cột."""
    gom = {}
    for hs in ds_hs:
        khoa = (hs[cot_dong], hs[cot_cot])
        gom.setdefault(khoa, []).append(hs[mon])
        
    return {k: round(sum(v) / len(v), 2) for k, v in gom.items()}

if __name__ == "__main__":
    # Phần tự thử nghiệm
    ds = doc_du_lieu("StudentsPerformance.csv")
    if ds:
        print("=== THỬ NGHIỆM PHẦN B ===")
        print(f"Tổng số HS: {len(ds)}\n")
        
        print("1. Tom tat danh sach diem toan cua 5 hs dau:")
        diem_5_hs = [hs["toan"] for hs in ds[:5]]
        print(diem_5_hs, "=>", tom_tat(diem_5_hs), "\n")
        
        print("2. Loc hs Nu (female), diem toan 95-100:")
        ds_loc = loc(ds, mon="toan", tu=95, den=100, gioi_tinh="female")
        print(f"Số lượng: {len(ds_loc)} hs\n")
        
        print("3. Canh bao diem < 40 cua 20 hs dau:")
        print(gom_canh_bao(ds[:20], nguong=40), "\n")
        
        print("4. Bang so sanh theo on thi:")
        for line in bang_so_sanh(ds, "on_thi", mon="toan"):
            print(line)
        print()
        
        print("5. Top 4 xep hang mon toan:")
        print(xep_hang(ds, "toan", k=4), "\n")
        
        print("6. Bang 2 chieu (gioi_tinh, on_thi) mon toan:")
        b2 = bang_hai_chieu(ds, "gioi_tinh", "on_thi")
        for k, v in b2.items():
            print(f"{k}: {v}")
