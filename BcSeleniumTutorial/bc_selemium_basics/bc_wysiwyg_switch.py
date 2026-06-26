'''
Created on 30 Apr 2026

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
wysiwyg_clk = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[8]/a')
wysiwyg_clk.click()
tiny_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[8]/ul/li[1]/a')
tiny_clk.click()
wysiwyg_clk = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[8]/a')
action.move_to_element(wysiwyg_clk).perform()
ck_editor = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[8]/ul/li[2]/a')
ck_editor.click()
wysiwyg_clk = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[8]/a')
action.move_to_element(wysiwyg_clk).perform()
summer_note = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[8]/ul/li[3]/a')
summer_note.click()
wysiwyg_clk = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[8]/a')
action.move_to_element(wysiwyg_clk).perform()
code_edk = driver.find_element(By.LINK_TEXT,'CodeMirror')
code_edk.click()
wysiwyg_clk = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[8]/a')
action.move_to_element(wysiwyg_clk).perform()
