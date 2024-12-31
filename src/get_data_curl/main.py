from .utils.get_list_danh_sach_lop_hoc_phan import get_list_danh_sach_lop_hoc_phan
from .utils.get_list_thoi_gian_lop_hoc_phan import get_list_thoi_gian_lop_hoc_phan
from .utils.get_header import get_header


def main():
    """
        Main function get data
    """
    
    # Get header information
    header = get_header()
    # print(header.toJson())
    
    # Get list danh sach lop hoc phan
    list_lop_hoc_phan = get_list_danh_sach_lop_hoc_phan()
    
    # Get list thoi gian lop hoc phan
    list_thoi_gian_lop_hoc_phan = get_list_thoi_gian_lop_hoc_phan(header, list_lop_hoc_phan)
    