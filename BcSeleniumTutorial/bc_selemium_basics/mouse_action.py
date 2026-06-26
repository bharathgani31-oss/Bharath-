'''
Created on 28 Apr 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

''' create action object from ActionChain class'''
action = ActionChains(driver)

'''Double click'''
copy_text_btn = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
#action.double_click(copy_text_btn).perform()
driver.execute_script("var evt = new MouseEvent('dblclick', {bubbles: true, cancelable: true}); arguments[0].dispatchEvent(evt);", copy_text_btn)

'''4 Mouse Hovering'''

point_me_btn = driver.find_element(By.CLASS_NAME, 'dropbtn')
action.move_to_element(point_me_btn).perform()

