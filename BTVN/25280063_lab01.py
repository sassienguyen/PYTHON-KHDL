DU_LIEU = [
    "# ngay;nhiet_do;luong_mua\n",
    "2026-09-01;31.5;0.0\n",
    "2026-09-02;32.0;5.5\n",
    "2026-09-03;30.5;22.0\n",
    "2026-09-04;33.5;0.0\n",
    "2026-09-05;34.0;0.0\n",
    "2026-09-06;32.5;0.0\n",
    "2026-09-07;31.0;1.5\n",
    "\n",
    "2026-09-08;29.5;35.0\n",
    "2026-09-09;30.0;0.0\n",
    "2026-09-10;33.0;0.0\n",
    "2026-09-11; 34.0 ;0.0\n",
    "2026-09-12;33.5;0.0\n",
    "2026-09-13;31.5;8.0\n",
    "2026-09-14;32.0;0.0\n",
]

def doc_du_lieu(cac_dong):
    res = []
    for dong in cac_dong:
        dong = dong.strip()
        if not dong or dong.startswith("#"):
            continue
        ngay, nhiet_do, luong_mua = dong.split(";")
        res.append((ngay.strip(), float(nhiet_do), float(luong_mua)))
    return res

def phan_loai(nhiet_do, luong_mua):
    if luong_mua >= 20:
        return "Mua to"
    elif luong_mua > 0:
        return "Mua"
    elif nhiet_do >= 33:
        return "Nang nong"
    else:
        return "Binh thuong"

def dem_theo_loai(cac_ngay):
    dem = {}
    for _, nhiet_do, luong_mua in cac_ngay:
        loai = phan_loai(nhiet_do, luong_mua)
        dem[loai] = dem.get(loai, 0) + 1
    return dem

def ngay_nong_nhat(cac_ngay):
    if not cac_ngay:
        return None
    top = max(cac_ngay, key=lambda x: x[1])
    return (top[0], top[1])

def nhiet_do_trung_binh(cac_ngay):
    if not cac_ngay:
        return None
    tong = sum(x[1] for x in cac_ngay)
    return round(tong / len(cac_ngay), 2)

def dot_kho_dai_nhat(cac_ngay):
    if not cac_ngay:
        return None
    
    max_len, cur_len = 0, 0
    ngay_bat_dau = ngay_bat_dau_cur = None
    
    for ngay, _, luong_mua in cac_ngay:
        if luong_mua == 0:
            if cur_len == 0:
                ngay_bat_dau_cur = ngay
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                ngay_bat_dau = ngay_bat_dau_cur
        else:
            cur_len = 0
            
    return (ngay_bat_dau, max_len) if max_len > 0 else None

def bien_dong_lon_nhat(cac_ngay):
    if not cac_ngay or len(cac_ngay) < 2:
        return None
    
    # Tính độ chênh lệch giữa ngày hiện tại và ngày trước đó
    chenh_lech = [
        (cac_ngay[i][0], abs(cac_ngay[i][1] - cac_ngay[i-1][1])) 
        for i in range(1, len(cac_ngay))
    ]
    return max(chenh_lech, key=lambda x: x[1])

if __name__ == "__main__":
    data = doc_du_lieu(DU_LIEU)
    print("Dữ liệu:", data)
    print("Đếm theo loại:", dem_theo_loai(data))
    print("Ngày nóng nhất:", ngay_nong_nhat(data))
    print("Nhiệt độ trung bình:", nhiet_do_trung_binh(data))
    print("Đợt khô dài nhất:", dot_kho_dai_nhat(data))
    print("Biến động lớn nhất:", bien_dong_lon_nhat(data))
