"""

"""

class header:
    def __init__(self, **args):
        # Set accept
        self.accept = args.get('accept', "application/json, text/javascript, */*; q=0.01")
        # Set accept-language
        self.accept_language = args.get('accept_language', "en-US,en;q=0.9")
        # Set authorization
        self.authorization = args.get('authorization', "Bearer ...")
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
    