import requests
import time

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
                "strNguoiThucHien_Id": "d8bcde87f70247b19a1bae88dddd40a0",
                "strQLSV_NguoiHoc_Id": "d8bcde87f70247b19a1bae88dddd40a0",
                "strDangKy_LopHocPhan_Id": "6FC62C9FE36648B9BBE6CA51252C5BD6",
                "strChucNang_Id": "A9CE858670AE453B90BB0A74458EFA34",
                "_": "1"
            }
            response = requests.get('https://api.github.com/user', headers=header, params=params)
            if response.status_code == 200:
                print("Success")
            else:
                print("Failed")
        except:
            print("Error: ")
            return None
    
    return list_thoi_gian_lop_hoc_phan