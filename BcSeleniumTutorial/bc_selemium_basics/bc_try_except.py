'''
Created on 26 May 2026

@author: Bharath.c

//div[@class="grippy-host"]//following-sibling::div[contains(@id, 'aswift_') and contains(@id, '_host')]

//div[@class="grippy-host"]//following-sibling::div
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=10)
driver.get("https://demo.automationtesting.in/Frames.html")
action = ActionChains(driver)
reg_name = driver.find_element(By.LINK_TEXT, 'Register')
reg_name.click()

try:
    # time.sleep(5)
    shadow_host_ele = driver.find_element(By.CLASS_NAME, 'grippy-host')
    shadow_root_auto = shadow_host_ele.shadow_root
    chose_fil = shadow_root_auto.find_element(By.CSS_SELECTOR,'ins > span > svg > g')
    print(chose_fil.get_dom_attribute("class"))
    print(chose_fil.get_dom_attribute("stroke-linecap"))
    wait.until(EC.element_to_be_clickable(chose_fil))
    action.click(chose_fil).perform()
    print("ad is closed")
except:
    print("there is no ad")
first_name = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')
first_name.send_keys('abc')
last_name = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')
last_name.send_keys('bcd')
address_write = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[2]/div/textarea')
address_write.send_keys('#123 GT road bopal')
email_write = driver.find_element(By.XPATH,'//*[@id="eid"]/input')
email_write.send_keys('abc@gmail.com')
phone_type = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[4]/div/input')
phone_type.send_keys('1234567890')
gender_clk = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input')
gender_clk.click()
hobbies_check = driver.find_element(By.ID,'checkbox1')
hobbies_check.click()
# action.scroll_by_amount(0,200).perform()


try:
    language_list = driver.find_element(By.ID,'msdd')
    language_list.click()
    lang_clk = driver.find_element(By.LINK_TEXT,'Arabic')
    wait.until(EC.element_to_be_clickable(lang_clk))
    lang_clk.click()
    
    

except:
    shadow_host_ele = driver.find_element(By.CLASS_NAME, 'grippy-host')
    shadow_root_auto = shadow_host_ele.shadow_root
    chose_fil = shadow_root_auto.find_element(By.CSS_SELECTOR,'ins > span > svg > g')
    # print(chose_fil.get_dom_attribute("class"))
    # print(chose_fil.get_dom_attribute("stroke-linecap"))
    wait.until(EC.element_to_be_clickable(chose_fil))
    action.click(chose_fil).perform()
    print("ad is closed")
    # time.sleep(2)
    wait.until(EC.none_of(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='grippy-host']//following-sibling::div[contains(@id, 'aswift_') and contains(@id, '_host')]")))
    )
    language_list = driver.find_element(By.ID,'msdd')
    language_list.click()
    lang_clk = driver.find_element(By.LINK_TEXT,'Arabic')
    wait.until(EC.element_to_be_clickable(lang_clk))
    lang_clk.click()
skill_name = driver.find_element(By.XPATH,'//*[@id="Skills"]/option[4]')
skill_name.click()
select_country = driver.find_element(By.XPATH,'//*[@id="country"]/option[6]')
select_country.click()
yrar_clk = driver.find_element(By.ID,'yearbox')
yrar_clk.click()
year_clk = driver.find_element(By.XPATH,'//*[@id="yearbox"]/option[75]')
year_clk.click()
month_clk = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
month_clk.click()
mon_clk = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[11]/div[2]/select/option[8]')
mon_clk.click()
day_box = driver.find_element(By.ID,'daybox')
day_box.click()
num_clk = driver.find_element(By.XPATH,'//*[@id="daybox"]/option[16]')
num_clk.click()
pass_word = driver.find_element(By.ID,'firstpassword')
pass_word.send_keys('*/12a3*/45/*$!?')
conf_pass = driver.find_element(By.ID,'secondpassword')
conf_pass.send_keys('*/12a3*/45/*$!?')
# action.scroll_by_amount(0,200).perform()
sub_btn = driver.find_element(By.ID,'submitbtn')
sub_btn.click()
# re_fresh = driver.find_element(By.ID,'Button1')
# re_fresh.click()
chose_file = driver.find_element(By.ID,'imagesrc')
chose_file.send_keys(r'C:\Users\Bharath.c\Pictures\Screenshots\Screenshot 2023-05-12 094144.png')



