# -*- coding: utf-8 -*-

import MySQLdb
# kết nối database dể lấy tập luật
def layTapLuat():
    db = MySQLdb.connect('localhost', 'root', 'tttttttt', 'project')
    cursor = db.cursor()
    try:
        cursor.execute("select * from luat_dung;")
        tapLuat = cursor.fetchall()
    except:
        print "không thấy CSDL"
    ketLuan = []
    for i in tapLuat:
        ketLuan.append(i[2])
    giaThiet = []
    for n in tapLuat:
        giaThiet.append(n[1])
    GT = []
    for i in giaThiet:
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
        GT.append(x)
    return (GT, ketLuan)
