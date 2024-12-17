from google_auth_oauthlib.flow import Flow
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import urllib.parse as urlparse
import os
# Import module
# from .handleFileCredentials import writeCredentials, readCredentials

PATH_CREDENTIALS = os.environ.get('PATH_CREDENTIALS', 'src/gg_auth/credentials.json')

def writeCredentials(content):
    with open(PATH_CREDENTIALS, 'w') as file:
        file.write(content)


# Global variables
SCOPES = []
PATH_CREDENTIALS = None
PATH_CLIENT_SECRETS = None
REDIRECT_URI = None
AUTHORIZATION_CODE = None
SERVER = None
SERVER_THREAD = None
STOP_SERVER = threading.Event()  # Event to signal server shutdown

def get_var_env():
    global SCOPES
    global PATH_CREDENTIALS
    global PATH_CLIENT_SECRETS
    global REDIRECT_URI
    
    SCOPES = ['https://www.googleapis.com/auth/calendar', 
              'https://www.googleapis.com/auth/calendar.events', 
              'https://www.googleapis.com/auth/calendar.readonly',
              'https://www.googleapis.com/auth/spreadsheets'
              ]
    PATH_CREDENTIALS = os.getenv('PATH_CREDENTIALS', 'src/gg_auth/credentials.json')
    PATH_CLIENT_SECRETS = os.getenv('PATH_CLIENT_SECRETS', 'src/gg_auth/client_secrets.json')
    REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:3300/oauth2callback')
    # show value globally
    print('SCOPES: ', SCOPES)
    print('PATH_CREDENTIALS: ', PATH_CREDENTIALS)
    print('PATH_CLIENT_SECRETS: ', PATH_CLIENT_SECRETS)
    print('REDIRECT_URI: ', REDIRECT_URI)

class OAuth2Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global AUTHORIZATION_CODE
        if self.path.startswith('/oauth2callback'):
            query = urlparse.urlparse(self.path).query
            params = urlparse.parse_qs(query)
            AUTHORIZATION_CODE = params.get('code', [None])[0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Authorization code received. You can close this window.')
            # Signal the server to stop
            STOP_SERVER.set()

def start_server():
    global SERVER
    server_address = ('', 3300)
    SERVER = HTTPServer(server_address, OAuth2Handler)
    
    # Loop until STOP_SERVER is set
    while not STOP_SERVER.is_set():
        SERVER.handle_request()

    SERVER.server_close()

def create_credentials():
    get_var_env()
    
    # Start the local web server to handle redirect URI
    global SERVER_THREAD
    SERVER_THREAD = threading.Thread(target=start_server)
    SERVER_THREAD.start()

    # Create the OAuth 2.0 Flow object
    flow = Flow.from_client_secrets_file(
        PATH_CLIENT_SECRETS,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    
    # Generate the authorization URL
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'  # Include granted scopes if needed
    )
    
    print(authorization_url)
    # print('Please go to this URL: {}\n'.format(authorization_url))

    # Wait for the user to authenticate and provide the authorization code
    while AUTHORIZATION_CODE is None:
        pass
    
    # Fetch the access token
    flow.fetch_token(code=AUTHORIZATION_CODE)

    # Create an authorized API client
    credentials = flow.credentials
    
    # Write credentials to file
    writeCredentials(credentials.to_json())
    
    print('Credentials created successfully!')

    # Ensure the server thread has stopped
    STOP_SERVER.set()
    if SERVER_THREAD:
        SERVER_THREAD.join()

if __name__ == "__main__":
    create_credentials()
