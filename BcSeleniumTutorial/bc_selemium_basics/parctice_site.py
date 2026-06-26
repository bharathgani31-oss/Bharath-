'''
Created on 1 May 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
action = ActionChains(driver)
go_too = driver.find_element(By.LINK_TEXT, 'Practice Site')
go_too.click()
action.scroll_by_amount(0,1300).perform()
book_clk = driver.find_element(By.XPATH,'//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[2]')
book_clk.click()
html_book = driver.find_element(By.XPATH,'//*[@id="text-22-sub_row_1-0-2-1-0"]/div/ul/li/a[2]')
html_book.click()
#wait = WebDriverWait(driver, 4)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text-22-sub_row_1-0-2-2-0"]/div/ul/li/a[2]')))
#element.click()
java_script = driver.find_element(By.XPATH,'//*[@id="text-22-sub_row_1-0-2-2-0"]/div/ul/li/a[2]')
java_script.click()
#log_in = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a')
#action.move_to_element(log_in).perform()
at_site = driver.find_element(By.LINK_TEXT,'AT Site')
at_site.click()
#ckl_cart = driver.find_element(By.XPATH,'//*[@id="wpmenucartli"]/a/span[1]')
#ckl_cart.click()