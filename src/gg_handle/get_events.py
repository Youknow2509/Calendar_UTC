
from gg_auth import google_auth
from datetime import datetime, timezone

CALENDAR_ID = 'primary'

def get_all_events():
    """
        Get_All_Events function
    """
    # Get the current time in ISO format with UTC timezone
    now = datetime.utcnow().isoformat() + 'Z'
    
    # Call the Calendar API
    events_result = google_auth().events().list(
        calendarId=CALENDAR_ID,
        timeMin=now,  # Start from the current time
        maxResults=100, 
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No title')
        print(f"{start} - {summary}")
