# -*- coding: utf-8 -*-
from random import randint

def locLuat(giaThiet, ketLuan, GT):
    gtlocduoc = []
    klLocDuoc = []
    for i in range(len(giaThiet)):
        if all([x in GT for x in [ketLuan[i]]]) == False and all([x in GT for x in giaThiet[i]]) == True:
            gtlocduoc.append(giaThiet[i])
            klLocDuoc.append(ketLuan[i])
    return (gtlocduoc, klLocDuoc)

def chonLuatVaApDung(gtlocduoc, kllocduoc, GT):
    a = randint(1, len(kllocduoc))
    GT.append(kllocduoc[a-1])
    b = gtlocduoc[a-1]
    c = kllocduoc[a-1]
    return (GT,b,c)

def showThuocTinhNguoiDung(thuocTinhNguoiDung):
    print "\nTHÔNG TIN NHẬP VÀO: "
    print "giới tính:",
    if thuocTinhNguoiDung[0] == 'R1':
        print "Nam."
    else:
        print "Nữ."
    print "độ tuổi:",
    if thuocTinhNguoiDung[1] == 'R3':
        print "< 18 tuổi."
    elif thuocTinhNguoiDung[1] == 'R4':
        print "18-35 tuổi."
    elif thuocTinhNguoiDung[1] == 'R5':
        print "35-45 tuổi."
    else:
        print ">45 tuổi"
    print "Nghề nghiệp:",
    if thuocTinhNguoiDung[2] == 'R7':
        print "Học sinh, sinh viên."
    elif thuocTinhNguoiDung[2] == 'R8':
        print "Viên chức nhà nước, công nhân viên sở."
    elif thuocTinhNguoiDung[2] == 'R9':
        print "Lao động bình dân tự do"
    else:
        print "Nhà đầu tư, chủ doanh nghiệp"
    print "Sở thích:",
    if thuocTinhNguoiDung[3] == 'R11':
        print "Công Nghệ."
    elif thuocTinhNguoiDung[3] == 'R12':
        print "Giải trí."
    elif thuocTinhNguoiDung[3] == 'R13':
        print "Tin tức."
    else:
        print "Làm đẹp."
    print '\n'

def chuyenTuKiHieuVeTnGoi(a):
    b=''
    if a == 'R1': return 'Giới tính: Nam'
    elif a == 'R2': return 'Giới tính: Nữ'
    elif a == 'R3': return 'Độ tuổi: <18'
    elif a == 'R4': return 'Độ tuổi: 18 đến 34'
    elif a == 'R5': return 'Độ tuổi: 35 đến 44'
    elif a == 'R6': return 'Độ tuổi: >34'
    elif a == 'R7': return 'Nghề nghiệp: Học sinh, Sinh viên'
    elif a == 'R8': return 'Nghề nghiệp: Viên chức nhà nước, công nhân viên sở'
    elif a == 'R9': return 'Nghề nghiệp: Lao động bình dân tự do'
    elif a == 'R10': return 'Nghề nghiệp: Nhà đầu tư, chủ doanh nghiệp'
    elif a == 'R11': return 'Sở thích: Công nghệ'
    elif a == 'R12': return 'Sở thích: Giải trí'
    elif a == 'R13': return 'Sở thích: Tin tức'
    elif a == 'R14': return 'Sở thích: Làm đẹp'
    elif a == 'R15': return 'Giá: <=2 triệu'
    elif a == 'R16': return 'Giá: 2 đến 5 triệu'
    elif a == 'R17': return 'Giá: 5 đến 10 triệu'
    elif a == 'R18': return 'Giá: >10 triệu'
    elif a == 'R19': return 'Hãng: Apple'
    elif a == 'R20': return 'Hãng: LG'
    elif a == 'R21': return 'Hãng: Nokia'
    elif a == 'R22': return 'Hãng: Samsung'
    elif a == 'R23': return 'Hãng: Sony'
    elif a == 'R24': return 'Màu: Đen'
    elif a == 'R25': return 'Màu: Trắng'
    elif a == 'R26': return 'Màu: Hồng'
    elif a == 'R27': return 'Màu: Xám bạc'
    elif a == 'R28': return 'Màu: Vàng'
    elif a == 'R29': return 'Camera: <=8 MP'
    elif a == 'R30': return 'Camera: 8 đến 13 MP'
    elif a == 'R31': return 'Camera: >13 MP'
    elif a == 'R35': return 'RAM: < 1G'
    elif a == 'R36': return 'RAM: 1-2 G'
    elif a == 'R37': return 'RAM: >2G'
    elif a == 'R38': return 'Bộ nhớ trong: <=8'
    elif a == 'R39': return 'Bộ nhớ trong: 16'
    elif a == 'R40': return 'Bộ nhớ trong: 32'
    elif a == 'R41': return 'Bộ nhớ trong: 64'
    elif a == 'R42': return 'Bộ nhớ trong: >=128'
    elif a == 'R43': return 'Bộ nhớ trong: <1800'
    elif a == 'R44': return 'Bộ nhớ trong: 1800-3000'
    elif a == 'R45': return 'Bộ nhớ trong: >3000'
    else:
        return "Null"


