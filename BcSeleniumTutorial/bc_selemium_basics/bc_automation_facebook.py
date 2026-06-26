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
driver.get("https://www.facebook.com/")

action = ActionChains(driver)

create_account = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[5]/div/a/div/div[1]/div/span/span')
create_account.click()
first_name = driver.find_element(By.ID,'_R_1cl2p4jikacppb6amH1_')
first_name.send_keys("Bharath")
sub_name = driver.find_element(By.ID,'_R_1kl2p4jikacppb6amH1_')
sub_name.send_keys('Chandrashekara')
dob_check = driver.find_element(By.XPATH,'//*[@id="_r_3_"]/div')
dob_check.click()
date_clk = driver.find_element(By.XPATH,'//*[@id="facebook"]/body/script[86]')
date_clk.click()
# mail_id = driver.find_element(By.ID,'_R_6ad8p4jikacppb6amH1_')
# mail_id.send_keys('bharathgani31@gmail.com')
# password_write = driver.find_element(By.ID,'_R_clap4jikacppb6amH1_')
# password_write.send_keys('/1/*2b3,0o1a2**76q2&1g2./')
#submit_clk = driver.find_element(By.CSS_SELECTOR,'x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft')
#submit_clk.click()
