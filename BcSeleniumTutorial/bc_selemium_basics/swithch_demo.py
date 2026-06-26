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
enter_clk = driver.find_element(By.PARTIAL_LINK_TEXT, 'Iframe with in an Iframe')
enter_clk.click()

nested_frame = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(nested_frame)

iframe_demo = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(iframe_demo)

input_single_frame = driver.find_element(By.TAG_NAME, 'input')
input_single_frame.send_keys("Bharath")
