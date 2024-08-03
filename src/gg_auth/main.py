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
    service = build("calendar", "v3", credentials=creds)
    
    return service

if __name__ == '__main__':
    main()
