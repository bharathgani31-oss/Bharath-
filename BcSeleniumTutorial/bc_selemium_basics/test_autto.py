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
driver.get("https://practicetestautomation.com/practice-test-login/")
current_page_title = driver.title
enter_user_test = driver.find_element(By.ID, 'username')
enter_user_test.send_keys("student")
enter_password_text = driver.find_element(By.ID, 'password')
enter_password_text.send_keys("Password123")
enter_submit_cli = driver.find_element(By.ID, 'submit')
enter_submit_cli.click()
enter_logout_clk = driver.find_element(By.LINK_TEXT, 'Log out')
enter_logout_clk.click()