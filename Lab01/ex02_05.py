So_GL = float(input("nhập GL: "))
Luong = float(input("nhập lương: "))
GL_tieu_chuan = 44
GL_vuot_tieu_chuan = max(0, So_GL - GL_tieu_chuan)
TL = GL_tieu_chuan * Luong + GL_vuot_tieu_chuan * GL_tieu_chuan * 1.5
print(f"tổng tiền : {TL}")