import pandas as pd
import re
import os

def main():
    """
        Function main from get data from file
    """
    
    print('Handle load data from file')
    PATH_FILE_READ_DATE = 'data/data_17_12_24.xlsx'
    # Load the Excel file
    df = pd.read_excel(PATH_FILE_READ_DATE, sheet_name='data')

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
            'start_time': thoi_gian,
            'end_time': thoi_gian,
            'days': thu,
            'until': 'TODO'
        })
        
    # handle show obj tests
    for item in res:
        print(item)

def format_start_time(thoi_gian, tiet_hoc):
    """
        Format start time
    """
    pass

def format_end_time(thoi_gian, tiet_hoc):
    """
        Format end time
    """
    pass

def format_days(d):
    """
        Format days
    """
    pass    

def format_until(thoi_gian):
    """
        Format until
    """
    pass
    
if __name__ == '__main__':
    main()