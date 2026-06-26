'''
Created on 26 Apr 2026

@author: Bharath.c
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

enter_btn_lst = driver.find_element(By.ID, 'country')
enter_btn_lst.click()

country_name = driver.find_element(By.XPATH, '//*[@id="country"]/option[10]')
country_name.click()



color_name = driver.find_element(By.XPATH, '//*[@id="colors"]/option[2]')
color_name.click()


