'''
Created on 8 May 2026

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

shadow_host_ele = driver.find_element(By.ID, 'shadow_host')

shadow_root_auto = shadow_host_ele.shadow_root

nest_host = shadow_root_auto.find_element(By.CSS_SELECTOR,'#nested_shadow_host')

nest_ele = nest_host.shadow_root

# mobile_clk = shadow_root_auto.find_element(By.CSS_SELECTOR,'#shadow_content > span')
# print(mobile_clk.text)

laptop_clk = nest_ele.find_element(By.CSS_SELECTOR, '#nested_shadow_content > div')
print(laptop_clk.text)


chose_fil = shadow_root_auto.find_element(By.CSS_SELECTOR,'input[type=file]:nth-child(9)')
chose_fil.send_keys(r'C:\Users\Bharath.c\Documents\KNN.py')

# sr_input_txt = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
# sr_input_txt.send_keys('bharath')
#
# sr_chk_bx = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=checkbox]:nth-child(7)')
# sr_chk_bx.click()
#
# blog_clk = driver.find_element(By.LINK_TEXT,'Blog')
# blog_clk.click()

# sr_input_txt = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
# sr_input_txt.send_keys('bharath')
#
# sr_chk_bx = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=checkbox]:nth-child(7)')
# sr_chk_bx.click()

# youtube_clk = driver.find_element(By.LINK_TEXT, 'Youtube')
# youtube_clk.click()//youtube does not need shadow root code it will run without anything
