import os 

PATH_CREDENTIALS = os.environ.get('PATH_CREDENTIALS', 'src/gg_auth/credentials.json')

def writeCredentials(content):
    with open(PATH_CREDENTIALS, 'w') as file:
        file.write(content)

def readCredentials():
    with open(PATH_CREDENTIALS, 'r') as file:
        content = file.read()
        return content

