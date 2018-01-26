# -*- coding: utf-8 -*-

from Tkinter import *

from GiaoDienKetQua import *
from LayTapLuat import layTapLuat
from LayThongDienThoai import layListThongSo, XacDinhDienThoaiPhuHop

from SuyDienTien import suyDienTien


def GiaoDienHoiThongTinNguoiDung():
    def Thoat():
        giaoDienHoiThongTin.quit()
    def KetQua():
        dauVao = []
        """đưa các giá trị mà người dùng chọn quy về tập ví dụ: [ R1, R3, R7, R11 ]"""
        if varCombo1.get() == 'Male':
            dauVao.append('R1')
        else:
            dauVao.append('R2')
        if varCombo2.get() == 'Less than 18':
            dauVao.append('R3')
        elif varCombo2.get() == 'From 18 to 34':
            dauVao.append('R4')
        elif varCombo2.get() == 'Frame 35 to 44':
            dauVao.append('R5')
        else:
            dauVao.append('R6')
        if varCombo3.get() == 'Student':
            dauVao.append('R7')
        elif varCombo3.get() == 'Teacher, personnel, officer':
            dauVao.append('R8')
        elif varCombo3.get() == 'Worker, Employee, taff':
            dauVao.append('R9')
        else:
            dauVao.append('R10')
        if varCombo4.get() == 'Technology':
            dauVao.append('R11')
        elif varCombo4.get() == 'Relax':
            dauVao.append('R12')
        elif varCombo4.get() == 'News':
            dauVao.append('R13')
        else:
            dauVao.append('R14')
        """thực hiện kết nối CSDL rồi"""
        giaThiet, ketLuan = layTapLuat()
        GT = dauVao

        """áp dụng Suy diễn tiến với tập giả thiết ban đầu và tập luật lấy từ CSDL"""
        GT,gtluatdadung,klluatdadung = suyDienTien(giaThiet, ketLuan, GT)
        danhSach, listThongSo = layListThongSo()
        danhSachDienThoaiPhuHop = XacDinhDienThoaiPhuHop(danhSach, listThongSo, GT)
        """đưa ra giao diện kết quả"""

        duaRaGiaoDienKetQua(danhSachDienThoaiPhuHop,gtluatdadung,klluatdadung, dauVao)

    giaoDienHoiThongTin = Tk()
    giaoDienHoiThongTin.title("Giao diện hỏi thông tin người dùng")
    huongdan = Label(giaoDienHoiThongTin, text = "Ấn vào các ô bên phải \n\
    và lựa chọn các thông tin phù hợp  ", bg = 'red', borderwidth=10 )
    huongdan.config(font=("Courier", 12))
    huongdan.pack(side = 'top')
    # hỏi Giới tính
    panelCombo1 = Frame(giaoDienHoiThongTin, relief=RIDGE, borderwidth=1)
    l = Label(panelCombo1, text = 'Giới tính:')
    l.pack(side='left', padx=12, pady=8)
    panelCombo1.pack(side='top', fill='x', padx=12, pady=8)
    varCombo1 = StringVar()
    varCombo1.set('Male')
    cboCombo1 = OptionMenu(panelCombo1, varCombo1, 'Male','Female')
    cboCombo1.config(width=30)
    cboCombo1.pack(side='right', anchor='w', padx=12, pady=8)

    # Hỏi Tuổi
    panelCombo2 = Frame(giaoDienHoiThongTin, relief=RIDGE, borderwidth=1)
    l = Label(panelCombo2, text='Độ tuổi:')
    l.pack(side='left', padx=12, pady=8)
    panelCombo2.pack(side='top', fill='x', padx=12, pady=8)
    varCombo2 = StringVar()
    varCombo2.set('Less than 18')
    cboCombo2 = OptionMenu(panelCombo2, varCombo2, 'Less than 18', 'From 18 to 34', 'Frame 35 to 44', 'more than 44')
    cboCombo2.config(width=30)
    cboCombo2.pack(side='right', anchor='w', padx=12, pady=8)

    # Hỏi NGhề nghiệp
    panelCombo3 = Frame(giaoDienHoiThongTin, relief=RIDGE, borderwidth=1)
    l = Label(panelCombo3, text='Nghề nghiệp: ')
    l.pack(side='left', padx=12, pady=8)
    panelCombo3.pack(side='top', fill='x', padx=12, pady=8)
    varCombo3 = StringVar()
    varCombo3.set('Student')
    cboCombo3 = OptionMenu(panelCombo3, varCombo3, 'Student', 'Teacher, personnel, officer', 'Worker, Employee, taff', 'Investor')
    cboCombo3.config(width=30)
    cboCombo3.pack(side='right', anchor='w', padx=12, pady=8, )

    # Hỏi Sở thích
    panelCombo4 = Frame(giaoDienHoiThongTin, relief=RIDGE, borderwidth=1)
    l = Label(panelCombo4, text='Sở thích: ')
    l.pack(side='left', padx=12, pady=8)
    panelCombo4.pack(side='top', fill='x', padx=12, pady=8)
    varCombo4 = StringVar()
    varCombo4.set('Technology')
    cboCombo4 = OptionMenu(panelCombo4,varCombo4, 'Technology', 'Relax', 'News', 'nice, beauti')
    cboCombo4.config(width=30)
    cboCombo4.pack(side='right', anchor='w', padx=12, pady=8)
    # đề đưa giao diện nên đầu

    # quy định kích thước, vị trí  hiển thị ban đầu

    # nút ấn xem kết quả và nút thoát
    Nut = Frame(giaoDienHoiThongTin, relief=SUNKEN, borderwidth=1)
    closeButton = Button(Nut, text="   Close   ", bg='red', command=Thoat)
    closeButton.pack(side=RIGHT, padx=5, pady=5)

    okButton = Button(Nut, text="   OK   ", bg='blue', command=KetQua)
    okButton.pack(side=RIGHT, padx=5, pady=5)
    Nut.pack(side=RIGHT, anchor='n', padx=25, pady=25)

    giaoDienHoiThongTin.geometry("400x400+50+50")
    giaoDienHoiThongTin.mainloop()

GiaoDienHoiThongTinNguoiDung()
