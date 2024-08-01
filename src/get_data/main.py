import os
import time
# import seleium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# import module
from .login import Login
from .readTable import ReadTableData

def main():
    """
        Main function Get Date
    """

    # Get Var from environment
    username = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    
    # Setup the ChromeDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Login to the website
    Login(driver, time, username, password)
    # Get the data
    ReadTableData(driver, time)
    
    # Close the browser
    driver.quit()
    
if __name__ == '__main__':
    main()