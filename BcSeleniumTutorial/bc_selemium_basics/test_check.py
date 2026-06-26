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

switch_widges = driver.find_element(By.LINK_TEXT, 'Widgets')
switch_widges.click()
accordion_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[1]/a')
accordion_clk.click()
group_one_clk = driver.find_element(By.XPATH,'//*[@id="Functionality"]/div/div/div/div[1]/div[1]/h4/a')
group_one_clk.click()
group_two_clk = driver.find_element(By.XPATH,'//*[@id="Functionality"]/div/div/div/div[2]/div[1]/h4/a')
group_two_clk.click()
group_three_clk = driver.find_element(By.XPATH,'//*[@id="Functionality"]/div/div/div/div[3]/div[1]/h4/a')
group_three_clk.click()
group_four_clk = driver.find_element(By.XPATH,'//*[@id="Functionality"]/div/div/div/div[4]/div[1]/h4/a')
group_four_clk.click()
switch_widges = driver.find_element(By.LINK_TEXT, 'Widgets')
action.move_to_element(switch_widges).perform()
auto_complete = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[2]/a')
auto_complete.click()
switch_widges = driver.find_element(By.LINK_TEXT, 'Widgets')
action.move_to_element(switch_widges).perform()
date_picker = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[3]/a')
date_picker.click()
date_pic = driver.find_element(By.ID,'datepicker1')
date_pic.click()
switch_widges = driver.find_element(By.LINK_TEXT, 'Widgets')
action.move_to_element(switch_widges).perform()
slider_move = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[4]/a')
slider_move.click()
