'''
Created on 4 Jun 2026

@author: Bharath.c
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPageST(unittest.TestCase):
    
    
    def setUp(self):
    
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")

        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



    def tearDown(self):
        pass

    
    def test_navigate_to_login_page(self):
        current_page_url = self.driver.current_url
        self.assertIn("login",current_page_url, 'Navigation failed')


    def test_login_to_orangehrm(self):
        user_wrt = self.driver.find_element(By.NAME, 'username')
        user_wrt.send_keys('Admin')
        pass_word = self.driver.find_element(By.NAME,'password')
        pass_word.send_keys('admin123')
        login_clk = self.driver.find_element(By.TAG_NAME,'button')
        login_clk.click()
        current_page_title = self.driver.title
        print("current_page_title",current_page_title)
        current_page_url = self.driver.current_url
        self.assertIn("dashboard",current_page_url, 'login failed')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()