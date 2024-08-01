from selenium.webdriver.common.by import By

def ReadTableData(driver, time):
    """
        Reads the table data from the website
    """
    form = driver.find_element(By.ID, "gridRegistered")

    # Tìm tất cả các phần tử với lớp 'cssRangeItem3' trong phần tử 'form'
    trs = form.find_elements(By.CLASS_NAME, "cssRangeItem3")

    # In ra số lượng phần tử tìm được 
    print(f'Tìm thấy {len(trs)} lớp học phần !!!')
    
    # Lặp qua từng phần tử và in ra thông tin
    for idx, tr in enumerate(trs):
        # Get id
        lhp_id = f"gridRegistered_lblCourseClass_{idx}"
        hp_id = f"gridRegistered_lblCourseCode_{idx}"
        tg_id = f"gridRegistered_lblLongTime_{idx}"
        dch_id = f"gridRegistered_lblLocation_{idx}"
        tc_id = f"gridRegistered_lblCourseCredit_{idx}"
        
        lhp = tr.find_elements(By.ID, lhp_id)
        hp = tr.find_elements(By.ID, hp_id)
        tg = tr.find_elements(By.ID, tg_id)
        dch = tr.find_elements(By.ID, dch_id)
        tc = tr.find_elements(By.ID, tc_id)
        
        print(f"Lớp học phần: {lhp[0].text}")
        print(f"- Mã học phần: {hp[0].text}")
        print(f"- Thời gian: {tg[0].text}")
        print(f"- Địa chỉ: {dch[0].text}")
        print(f"- Tín chỉ: {tc[0].text}")
        print("\n")
    
   
        