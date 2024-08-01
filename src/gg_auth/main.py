from .create_credentials import readCredentials
from .create_credentials import create_credentials
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json


def main():
    """
    Main function for the gg_auth package
    """
    credentials = readCredentials()
    if credentials is None:
        create_credentials()
        credentials = readCredentials()
    
    credentials_data = json.loads(credentials)
    credentials = Credentials(**credentials_data)

    service = build('calendar', 'v3', credentials=credentials)

    print(service)
if __name__ == '__main__':
    main()
