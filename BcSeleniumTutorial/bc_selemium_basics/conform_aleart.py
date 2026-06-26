'''
Created on 25 Apr 2026

@author: Bharath.c
'''
import time
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

conf_button = driver.find_element(By.ID, 'confirmBtn')
conf_button.click()
time.sleep(3)
aleart_popup = driver._switch_to.alert
aleart_popup.dismiss()
