'''
Created on 11 May 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
# 2
driver.get("https://testautomationpractice.blogspot.com/")
#3
'''
date_picker = driver.find_element(By.XPATH, '//*[@id="start-date"]')
date_picker.send_keys('11-05-2026')

date_pic = driver.find_element(By.XPATH,'//*[@id="end-date"]')
date_pic.send_keys('12-05-2026')
'''
date = input("Enter the date:")
element = driver.find_element(By.ID, 'datepicker')
element.send_keys(date)