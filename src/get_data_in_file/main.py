from .load_file import load_file
from .utils.date_format import date_format
from .utils.tiett_to_time import format_tiet
from .utils.day_to_string import day_to_string

def main():
    """
        Function main from get data from file
    """
    datas = load_file()
    
    res = [] # list of obj, a element type {'title': string, 'description': string, 'start_time': string, 'end_time': string, days: string, until: string}
    
    for data in datas:
        # data: {'Lhp': string, 'Data': list}
        title = data['Lhp']
        d = data['Data']
        for e in d:
            # e: {'date_ranges':  [('07/10/2024', '17/11/2024')], 'schedule': ('6', '10,11,12', '503-A8 Giảng đường A8')}
            date_ranges = e['date_ranges']
            schedule = e['schedule']
            if len(schedule) == 3:
                st, et = format_tiet(schedule[1])
                days = day_to_string(schedule[0])
                description=schedule[2]
                until = date_format(date_ranges[0][1]) + ' 00:00:00'
                start_time = date_format(date_ranges[0][0]) + ' ' + st
                end_time = date_format(date_ranges[0][0]) + ' ' + et
                r = {
                    'title': title,
                    'description': description,
                    'start_time': start_time,
                    'end_time': end_time,
                    'days': [days],
                    'until': until
                }
                res.append(r)
    
    # print('[')  
    # for r in res:
    #     print(r)
    #     print(',')
    # print(']')  
    return res   
    
if __name__ == '__main__':
    main()