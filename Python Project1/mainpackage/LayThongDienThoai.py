# -*- coding: utf-8 -*-
import MySQLdb

def layListThongSo():
    db = MySQLdb.connect('localhost', 'root', 'tttttttt', 'project')
    cursor = db.cursor()
    try:
        cursor.execute("select * from danh_sach;")
        danhSach = cursor.fetchall()
    except:
        print "không thấy CSDL"
    ts = []
    for n in danhSach:
        ts.append(n[10])
    thongSo = []
    for i in ts:
        dau, cuoi = 0, 0
        x = []

        for j in range(1, len(i)):
            if i[j] == 'R' or j == len(i):
                cuoi = j - 1
                str = ''
                for k in range(dau, cuoi + 1):
                    str += i[k]
                x.append(str)
                dau = j
            elif j + 1 == len(i):
                cuoi = j + 1
                str = ''
                for k in range(dau, cuoi):
                    str += i[k]
                x.append(str)
            else:
                continue
        thongSo.append(x)
    return (danhSach, thongSo)
def XacDinhDienThoaiPhuHop(danhSach, listThongSo, GT):
    dienThoaiPhuHop = []
    for i in range(len(listThongSo)):
        if all([x in GT for x in listThongSo[i]]):
            dienThoaiPhuHop.append(danhSach[i])
    return dienThoaiPhuHop