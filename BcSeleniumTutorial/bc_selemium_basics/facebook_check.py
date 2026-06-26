'''
Created on 3 May 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

wait = WebDriverWait(driver, 10)

# Open signup
create_account = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(@data-testid,'open-registration-form-button')]")
))
create_account.click()

# Fill form
first_name = wait.until(EC.visibility_of_element_located((By.NAME, "firstname")))
first_name.send_keys("Bharath")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Chandrashekara")

mail_id = driver.find_element(By.NAME, "reg_email__")
mail_id.send_keys("bharathgani31@gmail.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("your_password_here")

# Submit
submit_clk = driver.find_element(By.NAME, "websubmit")
submit_clk.click()