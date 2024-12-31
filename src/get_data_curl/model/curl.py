
class request:
    def __init__(self, header, **args):
        # Set url
        self.url = args.get('url', "https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_Chung/LayKetQuaDangKyLopHocPhan?action=DKH_Chung%2FLayKetQuaDangKyLopHocPhan&strDaoTao_ChuongTrinh_Id=&strDangKy_KeHoachDangKy_Id=F6C1A50758B34DBA9EC0115D6F99FF50&strQLSV_NguoiHoc_Id=d8bcde87f70247b19a1bae88dddd40a0&strNguoiThucHien_Id=d8bcde87f70247b19a1bae88dddd40a0&strDaoTao_ThoiGianDaoTao_Id=d6d1f36311ae468f858b25a401dbfba1&strChucNang_Id=A9CE858670AE453B90BB0A74458EFA34&_=1735610415876")
        self.header = header
        
    def toJson(self):
        # convert to json obj
        return {
            "url": self.url,
            "accept": self.header.accept,
            "accept_language": self.header.accept_language,
            "authorization": self.header.authorization,
            "cookie": self.header.cookie,
            "priority": self.header.priority,
            "referer": self.header.referer,
            "sec-ch-ua": self.header.sec_ch_ua,
            "sec-ch-ua-mobile": self.header.sec_ch_ua_mobile,
            "sec-ch-ua-platform": self.header.sec_ch_ua_platform,
            "sec-fetch-dest": self.header.sec_fetch_dest,
            "sec-fetch-mode": self.header.sec_fetch_mode,
            "sec-fetch-site": self.header.sec_fetch_site,
            "sec-gpc": self.header.sec_gpc,
            "user-agent": self.header.user_agent
        }