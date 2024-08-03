import pandas as pd
import re
import os

def load_file() -> list:
    """
        Function laod data from file.xlsx
    """
    PATH_FILE_READ_DATE = os.environ.get('PATH_FILE_READ_DATE', 'data/data.xlsx')
    
    # Load the Excel file
    df = pd.read_excel(PATH_FILE_READ_DATE, sheet_name='data')

    res = []
    
    number_rows = df.shape[0]
    for i in range(number_rows): 
        data = parse_schedule(df.iloc[i, 1])
        r = {'Lhp': df.iloc[i, 0] ,'Data': data}
        res.append(r)
        
    return res
        
def parse_schedule(datas: str) -> list:
    """
        Split the schedule into date ranges and schedules
    """
    res = []
    
    datas = datas.split('Từ')[1:]
    
    # Regex patterns to extract the necessary parts
    date_range_pattern = re.compile(r" (\d{2}/\d{2}/\d{4}) đến (\d{2}/\d{2}/\d{4}):")
    schedule_pattern = re.compile(r"Thứ (\d) tiết ([\d,]+) tại (.+)")
    
    for data in datas:
        # Splitting the input by date ranges
        date_ranges = date_range_pattern.findall(data)
        schedules = schedule_pattern.findall(data)
        
        size_date_ranges = len(date_ranges)
        size_schedules = len(schedules)
        if size_date_ranges > 0 and size_schedules > 0:
            for schedule in schedules:
                res.append({
                    'date_ranges': date_ranges,
                    'schedule': schedule
                })
        elif size_schedules == 0:
            res.append({
                'date_ranges': date_ranges,
                'schedule': []
            })
        
    
    return res
    
