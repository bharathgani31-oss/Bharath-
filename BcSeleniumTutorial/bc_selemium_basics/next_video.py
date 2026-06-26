'''
Created on 9 May 2026

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
switch_video = driver.find_element(By.LINK_TEXT, 'Video')
switch_video.click()
next_video_clk = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[7]/ul/li[2]/a')
next_video_clk.click()
iframe_ckl = driver.find_element(By.XPATH,'//*[@id="foo"]')
driver.switch_to.frame(iframe_ckl )

video_ckl = driver.find_element(By.CSS_SELECTOR,'#player')
action.move_to_element(video_ckl).perform()
action.click(video_ckl).perform()
