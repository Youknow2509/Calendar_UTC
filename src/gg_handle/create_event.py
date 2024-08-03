
from gg_auth import google_auth
from datetime import datetime, timedelta
from gg_handle.utils.time_format import time_format

def create_event(**kwargs):
    """
        Create an event basic:
        Parameters:
            title: Title of the event
            location: Location of the event
            description: Description of the event
            start_time: Start time of the event (ISO 8601) - '%d-%m-%Y %H:%M:%S' Ex: '03-08-2024 11:29:00'
            end_time: End time of the event (ISO 8601) - '%d-%m-%Y %H:%M:%S' Ex: '03-08-2024 12:29:00'
    """
    # Calendar ID of the primary calendar
    CALENDAR_ID = 'primary'
    
    TIME_ZONE = 'Asia/Ho_Chi_Minh'
    
    title = kwargs.get('title', 'Title none')
    location = kwargs.get('location', 'Location none')
    description = kwargs.get('description', 'Description none')
    start_time = kwargs.get('start_time', datetime.utcnow().isoformat() + 'Z')
    end_time = kwargs.get('end_time', (datetime.utcnow() + timedelta(hours=1)).isoformat() + 'Z')
        
    # Format time 
    start_time = time_format(start_time)
    end_time = time_format(end_time)
    
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
    }

    # Call the Calendar API
    event_result = google_auth().events().insert(
        calendarId=CALENDAR_ID,
        body=event
    ).execute()

    print(f'Event created: {event_result.get("htmlLink")}')
    print(f'''Event: Title: {title}, 
            Description: {description}, 
            Location: {location}, 
            Start Time: {start_time}, 
            End Time: {end_time}\n''')