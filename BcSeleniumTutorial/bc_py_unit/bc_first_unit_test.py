'''
Created on 31 May 2026

@author: Bharath.c
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginPage(unittest.TestCase):


    def test_navigate_to_login_page(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")

        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        current_page_url = driver.current_url
        self.assertIn("login",current_page_url, 'Navigation failed')


    def test_login_to_orangehrm(self):
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
        self.assertIn("dashboard",current_page_url, 'login failed')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()