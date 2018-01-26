# -*- coding: utf-8 -*-
from Module import chonLuatVaApDung, locLuat

def suyDienTien(giaThiet, ketLuan, GT):
    gtluatdadung = []
    klluatdadung = []
    gtlocduoc, kllocduoc = locLuat(giaThiet, ketLuan, GT)
    while len(gtlocduoc) != 0:
        GT,b,c = chonLuatVaApDung(gtlocduoc, kllocduoc, GT)
        gtluatdadung.append(b)
        klluatdadung.append(c)
        gtlocduoc, kllocduoc = locLuat(giaThiet, ketLuan, GT)
    return (GT, gtluatdadung, klluatdadung)