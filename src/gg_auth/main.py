from .create_credentials import readCredentials
from .create_credentials import create_credentials
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

import json

from googleapiclient.errors import HttpError
from datetime import datetime, timezone


#  Var global variables
creds = None

def get_credentials():
    """
    Get the credentials from the user
    """
    global creds
    creds = readCredentials()
    if not creds:
        create_credentials()
        creds = readCredentials()
    
    creds = Credentials(**json.loads(creds))
    creds.refresh(Request())
        
def main():
    """
    Main function for the gg_auth package
    """
    get_credentials()
    
    try:
        service = build("calendar", "v3", credentials=creds)

        # Get the current time in ISO 8601 format
        now = datetime.now(timezone.utc).isoformat()
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
    main()
