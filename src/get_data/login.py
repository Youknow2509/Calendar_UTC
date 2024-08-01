from selenium.webdriver.common.by import By

def Login(driver, time, username, password):
    """
        Login to the website: https://qldt.utc.edu.vn/
    """
    
    driver.get('https://qldt.utc.edu.vn/')
    
    # Wait for the page to load
    time.sleep(1)
    
    # Off focus 
    element = driver.find_element(By.ID, "pnlLogin") 
    element.click()
    time.sleep(0.5)
    
    # Handle JS login
    driver.execute_script("""
        document.getElementById('txtPassword').value = CryptoJS.MD5(arguments[1]).toString();
        document.getElementById('txtUserName').value = arguments[0];
        document.getElementById('btnSubmit').click();
    """, username, password)
    print("Login username: ", username, " correct !!!")
    
    time.sleep(1)
    
    # Xử lý cảnh báo
    alert = driver.switch_to.alert
    alert.accept()  # Hoặc alert.dismiss() để hủy bỏ
    driver.implicitly_wait(5)
