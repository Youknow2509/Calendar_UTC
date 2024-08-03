

from gg_auth import google_auth
from datetime import datetime, timedelta
from gg_handle.utils.time_format import time_format
from gg_handle.utils.time_format import time_format_until
from gg_handle.utils.day_format import day_format
from gg_handle.utils.fix_day_start import fix_day_start

def create_event_adv(**kwargs):
    """
        Create an event basic:
        Parameters:
            title: Title of the event
            location: Location of the event
            description: Description of the event
            start_time: Start time of the event (ISO 8601) - '%d-%m-%Y %H:%M:%S' Ex: '03-08-2024 11:29:00'
            end_time: End time of the event (ISO 8601) - '%d-%m-%Y %H:%M:%S' Ex: '03-08-2024 12:29:00'
            days: Days of the week to repeat the event - MO, WE, etc
            until: End time of the event (ISO 8601) - '%d-%m-%Y %H:%M:%S' Ex: '03-08-2024 12:29:00'
    """
    # Calendar ID of the primary calendar
    CALENDAR_ID = 'primary'
    
    TIME_ZONE = 'Asia/Ho_Chi_Minh'
    
    title = kwargs.get('title', 'Title none')
    location = kwargs.get('location', 'Location none')
    description = kwargs.get('description', 'Description none')
    start_time = kwargs.get('start_time', datetime.utcnow().isoformat() + 'Z')
    end_time = kwargs.get('end_time', (datetime.utcnow() + timedelta(hours=1)).isoformat() + 'Z')
    days = kwargs.get('days', ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])
    until = kwargs.get('until', (datetime.utcnow() + timedelta(weeks=2)).isoformat() + 'Z')
    
    # Format time 
    start_time = time_format(start_time)
    end_time = time_format(end_time)
    until = time_format_until(until)    
    
    # Calculate the duration of the event
    start_dt = datetime.fromisoformat(start_time)
    end_dt = datetime.fromisoformat(end_time)
    duration = end_dt - start_dt
    
    # print("duration: ", duration)
    
    # Format days    
    days = day_format(days)
    
    # Fix day near the specified 
    start_time = fix_day_start(start_time, days)
    start_dt = datetime.fromisoformat(start_time)
    end_time = (start_dt + duration).isoformat()
    
    # print('Start time: ', start_time)
    # print('End time: ', end_time)
    
    # Define event details
    event = {
        # Tiêu đề sự kiện
        'summary': title, 
        # Địa điểm sự kiện
        'location': location,
        # Mô tả sự kiện
        'description': description,
        # Thời gian bắt đầu sự kiện
        'start': {
            'dateTime': start_time,
            'timeZone': TIME_ZONE,
        },
        # Thời gian kết thúc sự kiện
        'end': {
            'dateTime': end_time, 
            'timeZone': TIME_ZONE,
        },
        # Lập đi lập lại sự kiện với một tuần xuất - vào thứ, kết thúc đến một thời điểm 
        'recurrence': [
            # Ex: 'RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR;UNTIL=20240803T235959Z',
            f'RRULE:FREQ=WEEKLY;BYDAY={days};UNTIL={until}'
        ],
    }

    print('Event: \n', event)
    
    # Call the Calendar API
    event_result = google_auth().events().insert(
        calendarId=CALENDAR_ID,
        body=event
    ).execute()

    print(f'Event created: {event_result.get("htmlLink")}')
    