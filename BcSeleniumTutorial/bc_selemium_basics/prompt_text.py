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

prompt_text = driver.find_element(By.ID,'promptBtn')
prompt_text.click()
time.sleep(2)
enter_text = driver.switch_to.alert
enter_text.send_keys('bharath')
enter_text1 = driver.switch_to.alert
enter_text1.accept()
