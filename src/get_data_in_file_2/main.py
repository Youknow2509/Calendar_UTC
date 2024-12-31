import pandas as pd
import re
import os

def main():
    """
        Function main from get data from file
    """
    
    # print('Handle load data from file')
    PATH_FILE_READ_DATE = 'data/data_17_12_24.xlsx'
    # Load the Excel file
    df = pd.read_excel(PATH_FILE_READ_DATE, sheet_name='data2')

    """
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
    
    number_rows = df.shape[0]
    for i in range(number_rows): 
        lop_hoc_phan = df.iloc[i, 0]
        thu = df.iloc[i, 1]
        tiet_hoc = df.iloc[i, 2]
        phong_hoc = df.iloc[i, 3]
        thoi_gian = df.iloc[i, 4]
        
        # show console to debug
        # print(lop_hoc_phan, ', thu: ', thu, ', tiet_hoc: ', tiet_hoc, ', phong_hoc: ', phong_hoc, ', thoi_gian: ', thoi_gian)

        res.append({
            'title': lop_hoc_phan,
            'description': phong_hoc,
            'start_time': format_start_time(thoi_gian, tiet_hoc),
            'end_time': format_end_time(thoi_gian, tiet_hoc),
            'days': [format_days(thu)],
            'until': format_until(thoi_gian, tiet_hoc) + ' ' + "00:00:00"
        })
        
    # handle show obj tests
    # print("[")
    # for item in res:
    #     print(item)
    #     print(', \n')
    # print("]\n")
    
    return res

def format_start_time(thoi_gian, tiet_hoc):
    """
        Format start time
        Ex: '30/12-19/01/2025 1->3' to "30-12-2024 07:00:00"
    """
    fm = help_format_thoi_gian_tiet_hoc(thoi_gian, tiet_hoc)

    tg_bd = fm.get('ngay_bat_dau', 'Err get thoi gian bat dau')
    nam = fm.get('nam', 'Err get nam')
    tiet_bd = fm.get('tiet_bat_dau', 'Err get tiet bat dau')
    
    #  check thoi gian la thang 12 thi nam - 1
    if tg_bd.split('/')[1] == '12':
        nam = str(int(nam) - 1)
    
    res = tg_bd.replace('/', '-') + '-' + nam + ' ' + help_change_tiet_hoc_to_thoi_gian(tiet_bd)[0]
    
    return res

def format_end_time(thoi_gian, tiet_hoc):
    """
        Format end time
    """
    fm = help_format_thoi_gian_tiet_hoc(thoi_gian, tiet_hoc)

    tg_kt = fm.get('ngay_bat_dau', 'Err get thoi gian ket thuc')
    nam = fm.get('nam', 'Err get nam')
    tiet_kt = fm.get('tiet_ket_thuc', 'Err get tiet ket thuc')
    
    #  check thoi gian la thang 12 thi nam - 1
    if tg_kt.split('/')[1] == '12':
        nam = str(int(nam) - 1)
        
    res = tg_kt.replace('/', '-') + '-' + nam + ' ' + help_change_tiet_hoc_to_thoi_gian(tiet_kt)[1]
    
    return res

def format_days(d):
    """
        Format days
    """
    return help_format_thu(d)  

def format_until(thoi_gian, tiet_hoc):
    """
        Format until
    """
    fm = help_format_thoi_gian_tiet_hoc(thoi_gian, tiet_hoc)

    tg_kt = fm.get('ngay_ket_thuc', 'Err get thoi gian ket thuc')
    nam = fm.get('nam', 'Err get nam')
    
    res = tg_kt.replace('/', '-') + '-' + nam
    
    return res

def help_format_thu(thu):
    """
        Format days
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
    return day_mapping[str(thu)]

def help_format_thoi_gian_tiet_hoc(thoi_gian, tiet_hoc):
    match = re.match(r"(\d{2}/\d{2})-(\d{2}/\d{2})/(\d{4})\s+(\d+)->(\d+)", str(str(thoi_gian) + " " + str(tiet_hoc)))
    if not match:
        raise ValueError("Invalid format. Expected format: 'dd/mm-dd/mm/yyyy x->y'")

    start_date_raw, end_date_raw, year_date_raw, start_period, end_period = match.groups()
    
    # show test results
    # print("Testing regex: start_date_raw: ", start_date_raw, ", end_date_raw: ", end_date_raw, ", year_date_raw: ", year_date_raw , ", start_period: ", start_period, ", end_period: ", end_period)
    
    return {
        'ngay_bat_dau': start_date_raw,
        'ngay_ket_thuc': end_date_raw,
        'nam': year_date_raw,
        'tiet_bat_dau': start_period,
        'tiet_ket_thuc': end_period
    }

def help_convert_tiet_hoc(tiet_hoc):
    """
        Chuyen doi tiet hoc thanh thoi gian: (gio vao, gio ket thuc)
    """
    dt = tiet_hoc.split('->')
    thoi_gian_bat_dau = help_change_tiet_hoc_to_thoi_gian(dt[0].trim())[0]
    thoi_gian_ket_thuc = help_change_tiet_hoc_to_thoi_gian(dt[1].trim())[1]
    
    return [thoi_gian_bat_dau, thoi_gian_ket_thuc]

def help_change_tiet_hoc_to_thoi_gian(tiet):
    tiet_dict = {
        '1': ['07:00:00', '07:45:00'],
        '2': ['07:50:00', '08:35:00'],
        '3': ['08:40:00', '09:25:00'],
        '4': ['09:35:00', '10:20:00'],
        '5': ['10:25:00', '11:10:00'],
        '6': ['11:15:00', '12:00:00'],
        '7': ['13:00:00', '13:45:00'],
        '8': ['13:50:00', '14:35:00'],
        '9': ['14:40:00', '15:25:00'],
        '10': ['15:35:00', '16:20:00'],
        '11': ['16:25:00', '17:10:00'],
        '12': ['17:15:00', '18:00:00'],
        '13': ['18:15:00', '19:00:00'],
        '14': ['19:05:00', '19:50:00'],
        '15': ['19:55:00', '20:40:00'],
        '16': ['20:45:00', '21:30:00'],
    }
    return tiet_dict.get(tiet, ['Err', 'Err'])
    
if __name__ == '__main__':
    main()