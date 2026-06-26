'''
Created on 23 Apr 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.page_load_strategy = "normal"
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=5)
driver.get("https://testautomationpractice.blogspot.com/")
current_page_title = driver.title
print("current_page_title:", current_page_title)
enter_name_wiki = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
enter_name_wiki.send_keys("selenium")
wiki_search_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
wiki_search_icon.click()
enter_text_element1 = driver.find_element(By.LINK_TEXT, 'Selenium')
enter_text_element1.click()
total_windows = driver.window_handles 
print(total_windows)
total_windows[1]
driver.switch_to.window(total_windows[1])
wait.until(EC.title_contains(""))
current_page_title = driver.title
print("current_page_title:", current_page_title)
enter_history_disp = driver.find_element(By.ID, 'toc-History')
enter_history_disp.click()