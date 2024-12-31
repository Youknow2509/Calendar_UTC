
class url_ds_lhp:
    def __init__(self, **args):
        # set action
        self.action = args.get('action', "DKH_Chung%2FLayKetQuaDangKyLopHocPhan")
        # set strDaoTao_ChuongTrinh_Id 
        self.strDaoTao_ChuongTrinh_Id = args.get('strDaoTao_ChuongTrinh_Id', "")
        # set strDangKy_KeHoachDangKy_Id
        self.strDangKy_KeHoachDangKy_Id = args.get('strDangKy_KeHoachDangKy_Id', "")
        # set strQLSV_NguoiHoc_Id
        self.strQLSV_NguoiHoc_Id = args.get('strQLSV_NguoiHoc_Id', "")
        # set strNguoiThucHien_Id
        self.strNguoiThucHien_Id = args.get('strNguoiThucHien_Id', "")
        # set strDaoTao_ThoiGianDaoTao_Id
        self.strDaoTao_ThoiGianDaoTao_Id = args.get('strDaoTao_ThoiGianDaoTao_Id', "")
        # set strChucNang_Id
        self.strChucNang_Id = args.get('strChucNang_Id', "")
        # set _
        self._ = args.get('_', "1")
        
    def toJson(self):
        # convert to json obj
        return {
            "action": self.action,
            "strDaoTao_ChuongTrinh_Id": self.strDaoTao_ChuongTrinh_Id,
            "strDangKy_KeHoachDangKy_Id": self.strDangKy_KeHoachDangKy_Id,
            "strQLSV_NguoiHoc_Id": self.strQLSV_NguoiHoc_Id,
            "strNguoiThucHien_Id": self.strNguoiThucHien_Id,
            "strDaoTao_ThoiGianDaoTao_Id": self.strDaoTao_ThoiGianDaoTao_Id,
            "strChucNang_Id": self.strChucNang_Id,
            "_": self._
        }
        
    def create_url(self) -> str:
        return f"https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_Chung/LayKetQuaDangKyLopHocPhan?action={self.action}&strDaoTao_ChuongTrinh_Id={self.strDaoTao_ChuongTrinh_Id}&strDangKy_KeHoachDangKy_Id={self.strDangKy_KeHoachDangKy_Id}&strQLSV_NguoiHoc_Id={self.strQLSV_NguoiHoc_Id}&strNguoiThucHien_Id={self.strNguoiThucHien_Id}&strDaoTao_ThoiGianDaoTao_Id={self.strDaoTao_ThoiGianDaoTao_Id}&strChucNang_Id={self.strChucNang_Id}&_={self._}"