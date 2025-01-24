from ..model.lop_hoc_phan import lop_hoc_phan

import os
import json

def get_list_danh_sach_lop_hoc_phan():
    """
        Get danh sach lop hoc phan
    """
    name_file = "ds_lhp.json"
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', name_file))

    # print("file path: ", file_path)
    
    # Open the JSON file and read its contents
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            list_lop_hoc_phan = []
            for lop_hoc_phan_json in data:
                # print(lop_hoc_phan_json)
                lhp_obj = lop_hoc_phan(**lop_hoc_phan_json)
                # print(lhp_obj)
                list_lop_hoc_phan.append(lhp_obj)
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return list_lop_hoc_phan