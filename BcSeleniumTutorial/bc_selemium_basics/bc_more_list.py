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
more_clk = driver.find_element(By.LINK_TEXT, 'More')
more_clk.click()
chart_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/ul/li[1]/a')
chart_clk.click()
move_ckl = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/a')
action.move_to_element(move_ckl).perform()

dynamic_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/ul/li[2]/a')
dynamic_clk.click()
action.scroll_by_amount(0,2500).perform()
clk_btn = driver.find_element(By.XPATH,'//*[@id="save"]')
clk_btn.click()
#action.scroll_by_amount(0,12000).perform()
#more_go = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/a')
#action.move_to_element(more_go).perform()
move_ckl = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/a')
action.move_to_element(move_ckl).perform()
#file_uplo = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[9]/ul/li[4]/a')
#file_uplo.click()
#upload_fill = driver.find_element(By.ID,'input-4')
#upload_fill.click()
action.scroll_by_amount(0,3000).perform()
loader_clk = driver.find_element(By.LINK_TEXT,'Loader')
loader_clk.click()
#action.scroll_by_amount(0,2500).perform()
run_clk = driver.find_element(By.XPATH,'//*[@id="loader"]')
run_clk.click()
close_btn = driver.find_element(By.XPATH,'//*[@id="myModal"]/div/div/div[3]/button[1]')
close_btn.click()