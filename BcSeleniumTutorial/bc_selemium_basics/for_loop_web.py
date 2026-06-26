'''
Created on 6 May 2026

@author: Bharath.c
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")


# rows = driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
# for i in range (0,6):
#     print(rows[i].text)
# cols = rows.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]')
# for col in cols(0,4):
#     print(cols.text,end = "|")
# print()
'''
rows = driver.find_elements(By.NAME,'BookTable')
for i in range(len(rows)):
    print(rows[i].text)
cols = driver.find_elements(By.TAG_NAME,'td')
for j in range(0):
    print(cols[j].text,end=" ")
print()

rows = driver.find_elements(By.ID,'taskTable')
for i in range(len(rows)):
    print(rows[i].text)
cols = driver.find_elements(By.TAG_NAME,'td')
for j in range(0):
    print(cols[j].text,end=" ")
print()

rows = driver.find_elements(By.ID,'productTable')
for i in range(len(rows)):
    print(rows[i].text)
cols = driver.find_elements(By.TAG_NAME,'td')
for j in range(0):
    print(cols[j].text,end=" ")
print()
'''
book_name = input("enter the book name:")
# match book_name:
#     case 1:
#         print("Sunday")
#
#     case 2:
#         print("Monday")
#
#     case 3:
#         print("Tuesday")
#
#     case 4:
#         print("Wednesday")
#
#     case 5:
#         print("Thursday")
#
#     case 6:
#         print("Friday")
#
#     case 7:
#         print("Saturday")
#
#     case _:
#         print("Please enter the correct number 1-7")

cols = driver.find_elements(By.NAME, 'BookTable')
print(len(cols))
for j in range(len(cols)):
    print(cols[j].text)
print()