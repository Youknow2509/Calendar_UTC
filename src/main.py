# from get_data import get_data
from gg_handle import *
# from get_data_in_file import get_data
# from get_data_in_file_2 import get_data
from get_data_curl import get_data

# todo delete
import re


def main():
    """
        Main function
    """
    get_data()
    # get_all_events()
    # create_event(title='Test create event with api')
    
    # create_event_adv(title='Hệ quản trị cơ sở dữ liệu Oracle-1-1-24(QT01)', 
    #                     days=['WE'],
    #                     start_time='12-08-2024 15:35:00',
    #                     end_time='12-08-2024 18:00:00',
    #                     until='22-09-2024 00:00:00',
    #                     description='503-A8 Giảng đường A8')

    # delete_all_events()
    
    # handle_file_create_calendar()
 
def handle_file_create_calendar():
    """
        Handle file create calendar
    """
    datas = get_data()
    
    for data in datas:
        # data: {'title': string, 'description': string, 'start_time': string, 'end_time': string, days: string, until: string}
        title = data['title']
        description = data['description']
        start_time = data['start_time']
        end_time = data['end_time']
        days = data['days']
        until = data['until']
        
        # print('title: ', title, ', description: ', description, ', start_time: ', start_time, ', end_time: ', end_time, ', days: ', days, ', until: ', until)
        # print('----------------------------------------------------------------------------------------------------------------')
        
        create_event_adv(title=title, description=description, start_time=start_time, end_time=end_time, days=days, until=until)
    
if __name__ == "__main__":
    main()
    
