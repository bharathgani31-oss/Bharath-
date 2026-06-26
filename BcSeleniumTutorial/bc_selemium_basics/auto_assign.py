'''
Created on 26 Apr 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")

'''Switch to i frame'''
driver._switch_to.frame('SingleFrame')

input_single_frame = driver.find_element(By.TAG_NAME, 'input')
input_single_frame.send_keys("bharath")
#enter_new_dis = driver.find_element(By.XPATH,'/html/body/section/div/div/div/input')
#enter_new_dis.send_keys("Bharath")

