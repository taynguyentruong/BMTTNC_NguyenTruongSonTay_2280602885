def chia_het_5(so_nhi_phan):
    so_thap_phan =int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("nhập chuổi số nhị phân: ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_5 = [so for so in so_nhi_phan_list if chia_het_5(so)]
if len(so_chia_het_5) > 0:
    ket_qua = ','.join(so_chia_het_5)
    print("các số nhị P chia hết cho 5 la:", ket_qua)
else:
    print("không có số nào")