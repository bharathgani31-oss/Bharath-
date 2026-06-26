'''
Created on 30 Apr 2026

@author: Bharath.c
'''
import time
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
switch_video = driver.find_element(By.LINK_TEXT, 'Video')
switch_video.click()

go_to = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[7]/ul/li[1]/a')
go_to.click()

iframe_chk = driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/iframe')
driver.switch_to.frame(iframe_chk)

video_clk = driver.find_element(By.CSS_SELECTOR,'#player-controls > ytm-custom-control > ytm-watch-player-controls > cued-overlay > button > c3-icon > span > div > svg > path.logo-arrow')
action.move_to_element(video_clk).perform()
action.click(video_clk).perform()
# switch_to = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[7]/a')
# switch_to.click()
# time.sleep(10)
# switch_back = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[7]/a')
# action.move_to_element(switch_back).perform()
# vidoe_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[7]/ul/li[2]/a')
# vidoe_clk.click()
