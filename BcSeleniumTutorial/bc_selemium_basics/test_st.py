'''
Created on 23 Apr 2026

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
current_page_title = driver.title
print("current_page_title:", current_page_title)

enter_name_name = driver.find_element(By.ID, 'name')
enter_name_name.send_keys("Bharath")
enter_name_email = driver.find_element(By.ID, 'email')
enter_name_email.send_keys("bharathgani31@gmail.com")
enter_name_phone = driver.find_element(By.ID, 'phone')
enter_name_phone.send_keys("8792477769")
enter_name_textarea = driver.find_element(By.ID, 'textarea')
enter_name_textarea.send_keys("# 123 india")
wiki_name_radio = driver.find_element(By.ID, 'male')
wiki_name_radio.click()
wiki_week_check = driver.find_element(By.ID, 'thursday')
wiki_week_check.click()
wiki_week_check1 = driver.find_element(By.ID, 'monday')
wiki_week_check1.click()
wiki_week_check2 = driver.find_element(By.ID, 'tuesday')
wiki_week_check2.click()
wiki_week_check3 = driver.find_element(By.ID, 'wednesday')
wiki_week_check3.click()
wiki_week_check4 = driver.find_element(By.ID, 'friday')
wiki_week_check4.click()
wiki_week_check5 = driver.find_element(By.ID, 'saturday')
wiki_week_check5.click()
wiki_week_check6 = driver.find_element(By.ID, 'sunday')
wiki_week_check6.click()
enter_name_datepicker = driver.find_element(By.ID, 'datepicker')
enter_name_datepicker.send_keys("03/23/2026")
enter_text_form = driver.find_element(By.ID, 'input1')
enter_text_form.send_keys("Hello")
enter_text_form1 = driver.find_element(By.ID, 'input2')
enter_text_form1.send_keys("My name is bharath")
enter_text_form2 = driver.find_element(By.ID, 'input3')
enter_text_form2.send_keys("Bhuvan")