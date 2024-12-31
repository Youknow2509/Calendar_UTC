
class request:
    def __init__(self, **args):
        # Set url
        self.url = args.get('url', "https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_Chung/LayKetQuaDangKyLopHocPhan?action=DKH_Chung%2FLayKetQuaDangKyLopHocPhan&strDaoTao_ChuongTrinh_Id=&strDangKy_KeHoachDangKy_Id=F6C1A50758B34DBA9EC0115D6F99FF50&strQLSV_NguoiHoc_Id=d8bcde87f70247b19a1bae88dddd40a0&strNguoiThucHien_Id=d8bcde87f70247b19a1bae88dddd40a0&strDaoTao_ThoiGianDaoTao_Id=d6d1f36311ae468f858b25a401dbfba1&strChucNang_Id=A9CE858670AE453B90BB0A74458EFA34&_=1735610415876")
        # Set accept
        self.accept = args.get('accept', "application/json, text/javascript, */*; q=0.01")
        # Set accept-language
        self.accept_language = args.get('accept_language', "en-US,en;q=0.9")
        # Set authorization
        self.authorization = args.get('authorization', "Bearer @@@@;")
        # Set cookie
        self.cookie = args.get('cookie', "__AntiXsrfToken=@@@@; .Auth=@@@@")
        # Set priority
        self.priority = args.get('priority', "u=1, i")
        # Set referer
        self.referer = args.get('referer', "https://qldt.utc.edu.vn/congthongtin/Index.aspx")
        # Set sec-ch-ua
        self.sec_ch_ua = args.get('sec-ch-ua', '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"')
        # Set sec-ch-ua-mobile
        self.sec_ch_ua_mobile = args.get('sec-ch-ua-mobile', "?0")
        # Set sec-ch-ua-platform
        self.sec_ch_ua_platform = args.get('sec-ch-ua-platform', "macOS")
        # Set sec-fetch-dest
        self.sec_fetch_dest = args.get('sec-fetch-dest', "empty")
        # Set sec-fetch-mode
        self.sec_fetch_mode = args.get('sec-fetch-mode', "cors")
        # Set sec-fetch-site
        self.sec_fetch_site = args.get('sec-fetch-site', "same-origin")
        # Set sec-gpc
        self.sec_gpc = args.get('sec-gpc', "1")
        # Set user-agent
        self.user_agent = args.get('user-agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

    def toJson(self):
        # convert to json obj
        return {
            "url": self.url,
            "accept": self.accept,
            "accept_language": self.accept_language,
            "authorization": self.authorization,
            "cookie": self.cookie,
            "priority": self.priority,
            "referer": self.referer,
            "sec-ch-ua": self.sec_ch_ua,
            "sec-ch-ua-mobile": self.sec_ch_ua_mobile,
            "sec-ch-ua-platform": self.sec_ch_ua_platform,
            "sec-fetch-dest": self.sec_fetch_dest,
            "sec-fetch-mode": self.sec_fetch_mode,
            "sec-fetch-site": self.sec_fetch_site,
            "sec-gpc": self.sec_gpc,
            "user-agent": self.user_agent
        }