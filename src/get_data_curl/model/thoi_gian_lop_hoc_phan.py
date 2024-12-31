""" Example
    "NGAYTAO": "20241231090753",
    "NGUOITAO_ID": "d8bcde87f70247b19a1bae88dddd40a0",
    "NGAYCAPNHATCUOI": "20241231090753",
    "NGUOICAPNHATCUOI_ID": "d8bcde87f70247b19a1bae88dddd40a0",
    "QLSV_NGUOIHOC_ID": "d8bcde87f70247b19a1bae88dddd40a0",
    "DANGKY_LOPHOCPHAN_ID": "6FC62C9FE36648B9BBE6CA51252C5BD6",
    "DANGKY_LOPHOCPHAN_TEN": null,
    "GIANGVIEN_ID": null,
    "NGAYBATDAU": "30/12/2024",
    "NGAYKETTHUC": "05/01/2025",
    "THU": "5",
    "THUHOC": "5 - 02/01/2025",
    "SOTIET": 3.0,
    "TIETBATDAU": 7.0,
    "TIETKETTHUC": 9.0,
    "PHONGHOC_ID": "7cc93082a21a41a2b4e51d96341e5d34",
    "PHONGHOC_TEN": "301-A3B",
    "THUOCTINHLOP_ID": "0486dbab65bf4884807e12cecd735b41",
    "THUOCTINH_TEN": null,
    "GIANGVIEN": null,
    "BUOIHOC": null,
    "NGAYHOC": "02/01/2025",
    "GIOBATDAU": 13.0,
    "PHUTBATDAU": 0.0,
    "GIOKETTHUC": 15.0,
    "PHUTKETTHUC": 25.0
"""

class thoi_gian_lop_hoc_phan:
    def __init__(self, **args):
        self.NGAYTAO = args.get("NGAYTAO") 
        self.NGUOITAO_ID = args.get("NGUOITAO_ID") 
        self.NGAYCAPNHATCUOI = args.get("NGAYCAPNHATCUOI") 
        self.NGUOICAPNHATCUOI_ID = args.get("NGUOICAPNHATCUOI_ID") 
        self.QLSV_NGUOIHOC_ID = args.get("QLSV_NGUOIHOC_ID") 
        self.DANGKY_LOPHOCPHAN_ID = args.get("DANGKY_LOPHOCPHAN_ID") 
        self.DANGKY_LOPHOCPHAN_TEN = args.get("DANGKY_LOPHOCPHAN_TEN") 
        self.GIANGVIEN_ID = args.get("GIANGVIEN_ID") 
        self.NGAYBATDAU = args.get("NGAYBATDAU") 
        self.NGAYKETTHUC = args.get("NGAYKETTHUC") 
        self.THU = args.get("THU") 
        self.THUHOC = args.get("THUHOC") 
        self.SOTIET = args.get("SOTIET") 
        self.TIETBATDAU = args.get("TIETBATDAU") 
        self.TIETKETTHUC = args.get("TIETKETTHUC") 
        self.PHONGHOC_ID = args.get("PHONGHOC_ID") 
        self.PHONGHOC_TEN = args.get("PHONGHOC_TEN") 
        self.THUOCTINHLOP_ID = args.get("THUOCTINHLOP_ID") 
        self.THUOCTINH_TEN = args.get("THUOCTINH_TEN") 
        self.GIANGVIEN = args.get("GIANGVIEN") 
        self.BUOIHOC = args.get("BUOIHOC") 
        self.NGAYHOC = args.get("NGAYHOC") 
        self.GIOBATDAU = args.get("GIOBATDAU") 
        self.PHUTBATDAU = args.get("PHUTBATDAU") 
        self.GIOKETTHUC = args.get("GIOKETTHUC") 
        self.PHUTKETTHUC = args.get("PHUTKETTHUC") 