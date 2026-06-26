'''
Created on 25 Apr 2026

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
driver.get("https://testautomationpractice.blogspot.com/")



current_page_title = driver.title
print("current_page_title:", current_page_title)
total_windows = driver.window_handles 
print(total_windows)
enter_new_dis = driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button')
enter_new_dis.click()
enter_pop_clk = driver.find_element(By.ID, 'PopUp')
enter_pop_clk.click()

enter_name_wiki = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
enter_name_wiki.send_keys("selenium")
wiki_search_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
wiki_search_icon.click()

enter_text_element1 = driver.find_element(By.LINK_TEXT, 'Selenium')
enter_text_element1.click()


#enter_history_disp = driver.find_element(By.ID, 'toc-History')
#enter_history_disp.click()

current_page_title = driver.title
print("current_page_title:", current_page_title)
driver.window_handles
#driver.switch_to.window(window_name)
total_windows = driver.window_handles 
print(total_windows)
total_windows[4]
driver.switch_to.window(total_windows[4])
driver.switch_to.window()
current_page_title = driver.title
print("current_page_title:", current_page_title)
enter_history_disp = driver.find_element(By.ID, 'toc-History')
enter_history_disp.click()
current_page_title = driver.title
print("current_page_title:", current_page_title)