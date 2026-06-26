'''
Created on 5 May 2026

@author: Bharath.c
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_wrt = driver.find_element(By.NAME, 'username')
user_wrt.send_keys('Admin')
pass_word = driver.find_element(By.NAME,'password')
pass_word.send_keys('admin123')
login_clk = driver.find_element(By.TAG_NAME,'button')
login_clk.click()
current_page_title = driver.title
print("current_page_title",current_page_title)
current_page_url = driver.current_url
print(driver.current_url)
if "dashboard" in current_page_url:
    print("login passed")
else:
    print("login failed")
# dash_board = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
# dash_board.click()
# admin_locate = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
# admin_locate.click()