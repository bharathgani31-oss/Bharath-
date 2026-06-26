'''
Created on 5 May 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
# 2
driver.get("https://testautomationpractice.blogspot.com/")
action = ActionChains(driver)
action.scroll_by_amount(0,3000).perform()
text_wrt = driver.find_element(By.XPATH, '//*[@id="shadow_host"]//input[1]')
text_wrt.send_keys('bharath')