'''
Created on 27 Apr 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
chose_file = driver.find_element(By.XPATH, '//*[@id="multipleFilesInput"]')
chose_file.send_keys(r'C:\Users\Bharath.c\Documents\KNN.py')
chose_file.send_keys(r'C:\Users\Bharath.c\Documents\total.docx')
upload_file = driver.find_element(By.XPATH, '//*[@id="multipleFilesForm"]/button')
upload_file.click()