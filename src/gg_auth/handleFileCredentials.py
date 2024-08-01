import os 

PATH_CREDENTIALS = os.environ.get('PATH_CREDENTIALS')

def writeCredentials(content):
    with open(PATH_CREDENTIALS, 'w') as file:
        file.write(content)

def readCredentials(file_name):
    with open(PATH_CREDENTIALS, 'r') as file:
        content = file.read()
        return content

