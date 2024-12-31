""" Example:
    https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_LichTuanTheoLopHocPhan/LayLichTuanTheoLopHocPhan?action=DKH_LichTuanTheoLopHocPhan%2FLayLichTuanTheoLopHocPhan&type=GET&strNguoiThucHien_Id=d8bcde87f70247b19a1bae88dddd40a0&strQLSV_NguoiHoc_Id=d8bcde87f70247b19a1bae88dddd40a0&strDangKy_LopHocPhan_Id=6FC62C9FE36648B9BBE6CA51252C5BD6&strChucNang_Id=A9CE858670AE453B90BB0A74458EFA34&_=1
"""

class url_tg_lhp:
    def __init__(self, **args):
        self.action = args.get("action", "DKH_LichTuanTheoLopHocPhan%2FLayLichTuanTheoLopHocPhan")
        self.type = args.get("type", "GET")
        self.strNguoiThucHien_Id = args.get("strNguoiThucHien_Id") 
        self.strQLSV_NguoiHoc_Id = args.get("strQLSV_NguoiHoc_Id")
        self.strDangKy_LopHocPhan_Id = args.get("strDangKy_LopHocPhan_Id")
        self.strChucNang_Id = args.get("strChucNang_Id")
        self._ = args.get("_", 1)
        
    def get_url(self):
        # return url
        return f"https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_LichTuanTheoLopHocPhan/LayLichTuanTheoLopHocPhan?action={self.action}&type={self.type}&strNguoiThucHien_Id={self.strNguoiThucHien_Id}&strQLSV_NguoiHoc_Id={self.strQLSV_NguoiHoc_Id}&strDangKy_LopHocPhan_Id={self.strDangKy_LopHocPhan_Id}&strChucNang_Id={self.strChucNang_Id}&_={self._}"