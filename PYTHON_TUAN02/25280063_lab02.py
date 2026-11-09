DON_HANG = [
    "# ma_don;khach;mat_hang;so_luong;don_gia",
    "D01    ; nguyen van an ;Ca phe sua    ;2;25,000",
    "D02;TRAN THI BINH;Tra dao;1;30,000",
    "D03; nguyen van an;Banh mi;3;15,000",
    "D04;le van chi;Ca phe sua;;25,000",
    "D05;tran thi binh;Sinh to bo;2.0;",
    "",
    "D06;Le Van Chi;Tra dao; 4 ;30000",
    "D07;tran thi BINH;Ca phe sua;1;25,000",
]

DATA_1 = [
    "# ma_don;khach_hang;san_pham;so_luong;don_gia",
    "  ORD-001  ;  Nguyen Hoang Long  ;  Tai nghe Bluetooth  ; 2 ; 450,000 ",
    "ORD-002;NGUYEN HOANG LONG;Chuot khong dau;1; 250000 ",
    "ORD-003;Pham Minh Tuan;  Ban phim co ; ; 1,200,000",
    "ORD-004;;  Tai nghe Bluetooth  ;1;450,000",
    "ORD-005;pham minh tuan;Lot chuot RGB;3.0;150,000",
    "ORD-006;  Nguyen Hoang Long ;Chuot khong dau; -2 ; 250,000",
    "ORD-007;VO THI MAI;  ;1; 80,000",
    "",
    "ORD-008;Vo Thi Mai;Op dien thoai;5;0",
]

DATA_2 = [
    "# id;khach_hang;mat_hang;so_luong;don_gia",
    "G01;  tran van B ;Sua tuoi Vinamilk (Loc 4); 2 ; 32,000",
    "G02;Tran Van B; Mi Hao Hao (Thung) ;1.5; 110,000",
    "G03; HOANG THI C ;Trung ga (Hopt 10);;28,000",
    "G04;hoang thi c;Sua tuoi Vinamilk (Loc 4);3; 32.000",
    "G05;  ; Mi Hao Hao (Thung) ; 2 ; 110,000",
    "G06;Tran Van B;  ; ; ",
]

def chuan_hoa_ten(name):
    return " ".join(name.split()).title()

def doc_so_luong(chuoi):
    return 0 if not chuoi.split() else int(float(chuoi.replace(",", ".")))


def doc_don_gia(chuoi):
    return None if not chuoi.split() else float(chuoi.replace(",", ""))

def doc_don_hang(dong):
    splitValue = dong.split(";")
    if not splitValue[0]:
        return None
    elif splitValue[0][0] == '#':
        return None

    return {
            'ma_don': " ".join(splitValue[0].split()),
            'khach': chuan_hoa_ten(splitValue[1]),
            'mat_hang': " ".join(splitValue[2].split()),
            'so_luong': doc_so_luong(splitValue[3]),
            'don_gia': doc_don_gia(splitValue[4])
        }

def ap_dung_giam_gia(cac_don, phan_tram):
    processData = [doc_don_hang(i) for i in cac_don if doc_don_hang(i) is not None]

    for i in processData:
        if i['don_gia'] is not None:
            i['don_gia'] = i['don_gia'] * (100 - phan_tram)/100

    return processData

def tong_theo_khach(cac_dong):
    total = {}
    processData = [doc_don_hang(i) for i in cac_dong if doc_don_hang(i) is not None]
    
    for i in processData:
        if i['don_gia'] is not None:
            value = i['so_luong'] * i['don_gia']
            total[i['khach']] = total.get(i['khach'], 0) + value
            
    return total

def hoa_don(cac_dong, ten_khach):
    name = chuan_hoa_ten(ten_khach)
    processData = [doc_don_hang(i) for i in cac_dong if doc_don_hang(i) is not None]
    
    bill = [f"HOA DON - {name}"]
    total = 0
    
    for i in processData:
        if i['khach'] != name:
            continue
            
        detail = f"{i['ma_don']:<5}{i['mat_hang']:<18}{i['so_luong']:>3} x "
        if i['don_gia'] is None:
            bill.append(detail + f"{'chua co gia':>23}")
        else:
            value = i['so_luong'] * i['don_gia']
            total += value
            bill.append(detail + f"{i['don_gia']:>10,.0f} = {value:>10,.0f}")
            
    bill.append(f"{'TONG CONG':<42}{total:>10,.0f}")
    return bill

if __name__ == "__main__":
    print("TEST01")
    print(chuan_hoa_ten("ngEyen VAN niek"))


    print("\nTEST02")    
    data = DATA_2
    for i in data:
        print(doc_don_hang(i))

    print(DON_HANG[1])

    print("\nTEST03")
    sale = ap_dung_giam_gia(data, 50)
    for i  in sale:
        print(i)

    print("\nTEST04")
    print(tong_theo_khach(data))

    print("\nTEST05")
    bill = hoa_don(data, "le van chi")
    for i in bill:
        print(i)
