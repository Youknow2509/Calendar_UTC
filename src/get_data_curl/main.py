import time
from .utils.get_list_danh_sach_lop_hoc_phan import get_list_danh_sach_lop_hoc_phan
from .utils.get_list_thoi_gian_lop_hoc_phan import get_list_thoi_gian_lop_hoc_phan
from .utils.get_header import get_header
from .utils.format_date import format_date

def main():
    """
        Main function get data
        
        Output:
            res is list obj
            {
                'title': title,
                'description': description,
                'start_time': start_time,
                'end_time': end_time,
                'days': [days],
                'until': until
            }
    """
    
    res = []
    
    # Get header information
    header = get_header()
    # print(header.toJson())
    
    # Get list danh sach lop hoc phan
    list_lop_hoc_phan = get_list_danh_sach_lop_hoc_phan()
    # print(list_lop_hoc_phan)
    
    # Get list thoi gian lop hoc phan
    list_thoi_gian_lop_hoc_phan = get_list_thoi_gian_lop_hoc_phan(header, list_lop_hoc_phan)
    # print(list_thoi_gian_lop_hoc_phan)
    
    for tg_lhp in list_thoi_gian_lop_hoc_phan:
        title = tg_lhp['DANGKY_LOPHOCPHAN_TEN']
        data = tg_lhp['Data']
        if len(data) != 0:
            for item in data:
                description = item['PHONGHOC_TEN']
                start_time = format_date(item['NGAYHOC'], item['GIOBATDAU'], item['PHUTBATDAU'])
                end_time = format_date(item['NGAYHOC'], item['GIOKETTHUC'], item['PHUTKETTHUC'])
                days = day_to_string(item['THU'])
                until = format_date(item['NGAYKETTHUC'], item['GIOKETTHUC'], item['PHUTKETTHUC'])
                
                res.append({
                    'title': title,
                    'description': description,
                    'start_time': start_time,
                    'end_time': end_time,
                    'days': [days],
                    'until': until
                })
                
                # print({
                #     'title': title,
                #     'description': description,
                #     'start_time': start_time,
                #     'end_time': end_time,
                #     'days': [days],
                #     'until': until
                # })
    
    return res
                
                
def day_to_string(data: str) -> str:
    """
    Convert the day to string
    """
    day_mapping = {
        '2': 'MO',
        '3': 'TU',
        '4': 'WE',
        '5': 'TH',
        '6': 'FR',
        '7': 'SA',
        '8': 'SU'
    }
    
    return day_mapping[data]
                
        