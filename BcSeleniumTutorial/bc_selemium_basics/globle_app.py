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
driver.get("https://www.globalapptesting.com/best-practices-automated-testing")
current_page_title = driver.title
print("current_page_title")
enter_name_app = driver.find_element(By.ID, 'firstname-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_name_app.send_keys("bhuvan")
enter_subname_app = driver.find_element(By.ID, 'lastname-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_subname_app.send_keys("Arun")
enter_email_app = driver.find_element(By.ID, 'email-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_email_app.send_keys("abc@gmail.com")
enter_number_app = driver.find_element(By.ID, 'phone-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_number_app.send_keys("1234567890")
enter_country_app = driver.find_element(By.ID, 'country-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_country_app.send_keys("India")
enter_company_app = driver.find_element(By.ID, 'company-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_company_app.send_keys("Google")
enter_title_app = driver.find_element(By.ID, 'message_title-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_title_app.send_keys("Automation testing")
enter_message_app = driver.find_element(By.ID, 'message-cdaaa073-c3ec-4935-a3de-6947ff09b400_1450')
enter_message_app.send_keys("Because i am passate about my job of what i do")