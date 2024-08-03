from gg_auth import google_auth

def delete_all_events():
    """
        Delete all events in the primary calendar
    """
    
    service = google_auth()
    
    # Define the calendar ID (e.g., primary for the main calendar)
    calendar_id = 'primary'

    # List events
    events_result = service.events().list(calendarId=calendar_id).execute()
    events = events_result.get('items', [])

    # Delete all events
    for event in events:
        event_id = event['id']
        service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        print(f"Deleted event: {event_id}")