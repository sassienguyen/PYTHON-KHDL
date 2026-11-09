"""Bai thuc hanh 2 - phan tu viet tai lop (muc A2, A3, A4).

Moi lan sua xong mot ham thi chay:   python tai_lop.py
roi doi chieu voi hop Moc kiem trong de.
"""

DONG_THO = [
    "  nguyen van an ; 24TTH ; 8.5 ",
    "TRAN THI BINH;24TTH;4",
    "le  van   chi ; 25KDL ; 9.25",
    "pham thu dung;25KDL;",
    "  hoang minh giang;24TTH; 7,5",
]


# ===================================================== A2 - nam ham nho

def tach_truong(dong):
    splitValue = dong.split(";")
    return [" ".join(i.split()) for i in splitValue]

def chuan_hoa_ten(ten):
    ten = " ".join(ten.split())
    ten = ten.title()
    return ten

def doc_diem(chuoi):
    chuoi = chuoi.replace(",", ".")
    return float(chuoi) if chuoi != "" else None


def dinh_dang_dong(ten, lop, diem):
    return f"{chuan_hoa_ten(ten):<20}" + f"{lop:<7}" + (f"{"--":>6}" if diem is None else f"{diem:>6.2f}")



def chuan_hoa_bang(bang):

    cleanedBang = [[chuan_hoa_ten(" ".join(i[0].split())), i[1], i[2]] for i in bang]
    return cleanedBang

# ===================================================== A3 - ghep lai

def bao_cao(cac_dong):
    """Tra ve list cac dong cua bang diem, theo dung thu tu dau vao.
    Dong cuoi:  f"{'Trung binh':<27}{tb:>6.2f}"  voi tb la trung binh
    cua nhung nguoi CO diem. Khong duoc sua danh sach cac_dong."""
    # return []         # <-- CAN VIET LAI THAN HAM
    dropSpace = [tach_truong(i) for i in cac_dong]
    processedData = [[chuan_hoa_ten(i[0]), i[1], doc_diem(i[2])] for i in dropSpace]
    formattedData = [dinh_dang_dong(i[0], i[1], i[2]) for i in processedData]

    tb = 0.0
    n = 0
    for _, _, i in processedData:
        if i is None:
            continue
        else:
            tb += i
            n += 1

    tb = tb/n

    formattedData.append(f"{'Trung binh':<27}{tb:>6.2f}")
    return formattedData

# ===================================================== A4 - yeu cau them

def cao_thap_nhat(cac_dong):
    dropSpace = [tach_truong(i) for i in cac_dong]
    processedData = [[chuan_hoa_ten(i[0]), i[1], doc_diem(i[2])] for i in dropSpace]

    dropNA = []
    for i in processedData:
        if i[2] is None:
            continue
        else:   
            dropNA.append(i)
    
    if not dropNA:
        return None
    dropNA.sort(key=lambda x: x[2])

    return (dropNA[-1][0], dropNA[0][0])


if __name__ == "__main__":
    print("--- A2")
    print(tach_truong(DONG_THO[0]))
    print(chuan_hoa_ten("  le  van   CHI "))
    print(doc_diem("8.5"), doc_diem("4"), doc_diem("7,5"), doc_diem(""))
    print("|" + dinh_dang_dong("Le Van Chi", "25KDL", 9.25) + "|")
    print("|" + dinh_dang_dong("Pham Thu Dung", "25KDL", None) + "|")
    bang = [["  le van CHI", "25KDL", 9.25], ["an", "24TTH", 8.5]]
    bang_moi = chuan_hoa_bang(bang)
    print(bang_moi)
    print(bang)
    print("--- A3")
    for dong in bao_cao(DONG_THO):
        print(dong)
    print(DONG_THO[0])
    print("--- A4")
    print(cao_thap_nhat(DONG_THO))
    print(cao_thap_nhat(["an;L1;", "binh;L1;"]))
