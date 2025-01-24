import requests
import time
import json
from ..model.url_tg_lhp import url_tg_lhp
def get_list_thoi_gian_lop_hoc_phan(header, ds_lhp):
    """
        Get thoi gian lop hoc phan
    """
    
    list_thoi_gian_lop_hoc_phan = []
    
    for lhp in ds_lhp:
        # Get thoi gian lop hoc phan
        try:
            params = {
                "action": "DKH_LichTuanTheoLopHocPhan/LayLichTuanTheoLopHocPhan",
                "type": "GET",
                "strNguoiThucHien_Id": lhp.toJson().get("NGUOITAO_ID", None),
                "strQLSV_NguoiHoc_Id": lhp.toJson().get("QLSV_NGUOIHOC_ID", None),
                "strDangKy_LopHocPhan_Id": lhp.toJson().get("DANGKY_LOPHOCPHAN_ID", None),
                "strChucNang_Id": "A9CE858670AE453B90BB0A74458EFA34",
                "_": "1"
            }
            
            header_obj = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-language": "en-US,en;q=0.9",
                "Authorization": header.toJson().get("authorization", None),
                "Cookie": header.toJson().get("cookie", None),
                "Priority": "u=1, i",
                "Referer": "https://qldt.utc.edu.vn/congthongtin/Index.aspx",
                "Sec-ch-ua-mobile": "?0",
                "Sec-ch-ua-platform": "macOS",
                "Sec-fetch-dest": "empty",
                "Sec-fetch-mode": "cors",
                "Sec-fetch-site": "same-origin",
                "Sec-gpc": "1",
                "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            }
                        
            response = requests.get('https://qldt.utc.edu.vn/dangkyhocapi/api/DKH_LichTuanTheoLopHocPhan/LayLichTuanTheoLopHocPhan', headers=header_obj, params=params)
            
            if response.status_code != 200:
                print("Error: ", response.status_code)
                return None
            
            response_json = json.loads(response.text)
            # print(response_json)
            
            # Get data
            data = response_json.get("Data", None)
            # print(data)
            res = {
                "DANGKY_LOPHOCPHAN_TEN": lhp.toJson().get("DANGKY_LOPHOCPHAN_TEN", None),
                "Data": data
            }
            # Add to list
            list_thoi_gian_lop_hoc_phan.append(res)
            # print(res)
            
            time.sleep(0.8) 
                    
        except Exception as e:
            print("Error: ", e)
            return None
    
    return list_thoi_gian_lop_hoc_phan