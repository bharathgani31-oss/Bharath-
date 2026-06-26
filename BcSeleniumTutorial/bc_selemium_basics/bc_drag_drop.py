'''
Created on 12 May 2026

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
driver.get("https://testautomationpractice.blogspot.com/")
#3
action = ActionChains(driver)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
action.drag_and_drop(source, target).perform()
action.scroll_by_amount(0,200).perform()

slider_moev = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
action.click_and_hold(slider_moev).drag_and_drop_by_offset(slider_moev, 40, 0)
action.click_and_hold(slider_moev).drag_and_drop_by_offset(slider_moev, -40, 0)
action.scroll_by_amount(0,200).perform()

second_slide = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
action.click_and_hold(second_slide).drag_and_drop_by_offset(second_slide, 40, 0)
action.click_and_hold(second_slide).drag_and_drop_by_offset(second_slide, -40, 0)
action.scroll_by_amount(0,200).perform()


# source = driver.find_element(By.ID, "angular")
# target = driver.find_element(By.ID, "droparea")
# action.drag_and_drop(source, target).perform()