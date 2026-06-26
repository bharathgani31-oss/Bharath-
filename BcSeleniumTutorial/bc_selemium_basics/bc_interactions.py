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

inter_action = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[6]/a')
inter_action.click()
drop_dowm = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
drop_dowm.click()
static_move = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a')
static_move.click()

source = driver.find_element(By.ID, "angular")
target = driver.find_element(By.ID, "droparea")
action.drag_and_drop(source, target).perform()

source = driver.find_element(By.ID,"mongo")
target = driver.find_element(By.ID,"droparea")
action.drag_and_drop(source, target).perform()

source = driver.find_element(By.ID,"node")
target = driver.find_element(By.ID,"droparea")
action.drag_and_drop(source, target).perform()

switch_inteact = driver.find_element(By.LINK_TEXT,'Interactions')
action.move_to_element(switch_inteact).perform()
drop_dowm = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
drop_dowm.click()
dynamic_move = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[2]/a')
dynamic_move.click()

source = driver.find_element(By.ID, "angular")
target = driver.find_element(By.ID, "droparea")
action.drag_and_drop(source, target).perform()

source = driver.find_element(By.ID,"mongo")
target = driver.find_element(By.ID,"droparea")
action.drag_and_drop(source, target).perform()

source = driver.find_element(By.ID,"node")
target = driver.find_element(By.ID,"droparea")
action.drag_and_drop(source, target).perform()

switch_inteact = driver.find_element(By.LINK_TEXT,'Interactions')
action.move_to_element(switch_inteact).perform()

selectables_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[2]/a')
selectables_clk.click()

default_fun = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
default_fun.click()

saki_clk = driver.find_element(By.XPATH,'//*[@id="Default"]/ul/li[1]')
saki_clk.click()

default_fun = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
action.move_to_element(default_fun).perform()

sara_clk = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
sara_clk.click()

switch_inteact = driver.find_element(By.LINK_TEXT,'Interactions')
action.move_to_element(switch_inteact).perform()

re_size = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[3]/a')
re_size.click()
#go_into = driver.find_element(By.XPATH,'//*[@id="resizable"]')
#driver.switch_to.frame(go_into)
resize_handle = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
ActionChains(driver).drag_and_drop_by_offset(resize_handle, 300, 300).perform()