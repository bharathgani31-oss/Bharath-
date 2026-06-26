'''
Created on 30 Apr 2026

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
driver.get("https://demo.automationtesting.in/Frames.html")
switch_to = driver.find_element(By.LINK_TEXT, 'SwitchTo')
switch_to.click()
alearts_move = driver.find_element(By.LINK_TEXT,'Alerts')
alearts_move.click()
click_aleart_one = driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')
click_aleart_one.click()
time.sleep(2)
aleart_popup = driver._switch_to.alert
aleart_popup.accept()
aleart_with_ok_cancel = driver.find_element(By.LINK_TEXT,'Alert with OK & Cancel')
aleart_with_ok_cancel.click()
time.sleep(2)
on_click = driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
on_click.click()
aleartt_popup = driver._switch_to.alert
aleartt_popup.dismiss()
aleart_textbox = driver.find_element(By.LINK_TEXT,'Alert with Textbox')
aleart_textbox.click() 
text_box_clk = driver.find_element(By.XPATH,'//*[@id="Textbox"]/button')
text_box_clk.click()
enter_text = driver.switch_to.alert
enter_text.send_keys('bharath')
enter_text1 = driver.switch_to.alert
enter_text1.accept()
