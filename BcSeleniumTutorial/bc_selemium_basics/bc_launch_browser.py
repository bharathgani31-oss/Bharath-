'''
Created on 11 Apr 2026

@author: Bharath.c
'''
#1
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#
driver = webdriver.Chrome(options)
# 2
driver.get("https://www.youtube.com/")
#3
current_page_title = driver.title
print("current_page_title:", current_page_title)




