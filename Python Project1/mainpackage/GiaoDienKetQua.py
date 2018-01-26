# -*- coding: utf-8 -*-
import functools
from Tkinter import *
from PIL import ImageTk, Image
from Module import chuyenTuKiHieuVeTnGoi

def duaRaGiaoDienKetQua(danhSachDienThoaiPhuHop,gtluatdadung,klluatdadung, dauVao):
    text=''
    def OnDouble(self):
        selection = ListTen.curselection()
        value = ListTen.get(selection[0])
        a = (str)(selection)
        b = ''
        for i in range(1, len(a)-2):
            b +=a[i]
        c = int(b)

        text = """
Tên: %s
ID: %d
Hãng: %s
Giá thành: %d đồng
RAM: %2.3f G
CPU: %.2f GHz
Bộ nhớ trong: %d G
Pin: %d mPA
Màu sắc: %r
                                        """ % (
            danhSachDienThoaiPhuHop[c][2], danhSachDienThoaiPhuHop[c][0], danhSachDienThoaiPhuHop[c][1],
            int(danhSachDienThoaiPhuHop[c][3]), float(danhSachDienThoaiPhuHop[c][7]),
            float(danhSachDienThoaiPhuHop[c][6]), int(danhSachDienThoaiPhuHop[c][8]),
            int(danhSachDienThoaiPhuHop[c][9]), str(danhSachDienThoaiPhuHop[c][4]))

        label2.configure(text = text)

    DSTenDT = []
    for i in range(len(danhSachDienThoaiPhuHop)):
        DSTenDT.append(danhSachDienThoaiPhuHop[i][2])
    giaoDienKQ = Tk()
    giaoDienKQ.title("Danh sách điện thoại phù hợp")

    """listBox danh sách điện thoại trong labal1 """
    label1 = Label(giaoDienKQ, relief=RIDGE, width=45, bg='blue')
    label11 = Label(label1, text = 'danh sách điện thoại phù hợp', bg='yellow', height  = 2)
    label11.config(font=("Courier", 12))
    label11.pack(fill = X)
    scrollbar = Scrollbar(label1, width=10)
    scrollbar.pack(side=LEFT, fill=Y)

    """ listBox chứa tên các điện thoại được thuật toán trả về"""
    ListTen = Listbox(label1, yscrollcommand=scrollbar.set, width=45, bg='white', height = 5)
    for line in DSTenDT:
        ListTen.insert(END, str(line))
    ListTen.bind("<Double-Button-1>", OnDouble)
    ListTen.pack(side=LEFT,fill = Y)
    scrollbar.config(command=ListTen.yview)
    label1.pack(side=LEFT, fill=Y)

    quatrinhsuydien = ''
    for i in range(len(gtluatdadung)):
        l=len(gtluatdadung[i])
        for j in range(l):
            quatrinhsuydien+=chuyenTuKiHieuVeTnGoi(gtluatdadung[i][j])
            if j< l-1:
                quatrinhsuydien+=" AND "
            else:
                quatrinhsuydien+=" ==> "+chuyenTuKiHieuVeTnGoi(klluatdadung[i])+'\n'
    """label3 chứa quá trình suy diễn, và hướng dẫn"""
    label3 = Label(giaoDienKQ, relief=RIDGE, width=110, bg='white')
    l31 = Label(label3, text = 'Quá trình suy diễn tiến', bg='magenta', height  = 2)
    l31.config(font=("Courier", 12))
    l31.pack(fill = X)
    l32= Text(label3, height=40)

    l32.insert(END, quatrinhsuydien)
    l32.pack(fill=X)
    vao = "Đầu vào:\n" + chuyenTuKiHieuVeTnGoi(dauVao[0]) +", "+ chuyenTuKiHieuVeTnGoi(
        dauVao[1])  +", "+ chuyenTuKiHieuVeTnGoi(dauVao[2]) +", "+ chuyenTuKiHieuVeTnGoi(dauVao[3])

    dauvao=Label(giaoDienKQ,text = vao, bg='red', height=5)
    # dauvao.insert(INSERT, vao)
    dauvao.config(font=("Courier", 13))
    dauvao.pack(side=BOTTOM, fill=X)
    label3.pack(side=RIGHT, fill=Y)

    """thông tin điện thoại trong label2"""
    text = """
Tên:%s
ID:%d
Hãng:%s
Giá thành:%d đồng
RAM: %2.3f G
CPU: %.2f GHz
Bộ nhớ trong: %d G
Pin: %d mPA
Màu sắc: %r
            """ % (danhSachDienThoaiPhuHop[0][2], danhSachDienThoaiPhuHop[0][0], danhSachDienThoaiPhuHop[0][1],
                   int(danhSachDienThoaiPhuHop[0][3]), float(danhSachDienThoaiPhuHop[0][7]),
                   float(danhSachDienThoaiPhuHop[0][6]), int(danhSachDienThoaiPhuHop[0][8]),
                   int(danhSachDienThoaiPhuHop[0][9]), str(danhSachDienThoaiPhuHop[0][4]))

    label2 = Message(giaoDienKQ,text=text, relief=RIDGE,bg='white')
    label2.config(font=("Courier", 12))
    a = Label(label2, text = "Thông số điện thoại", width=45, bg = "cyan",relief=RIDGE, height = 2)
    a.config(font=("Courier", 12))
    a.pack()
    label2.pack(side=LEFT, fill=Y)

    giaoDienKQ.attributes('-topmost', 1)

    giaoDienKQ.mainloop()