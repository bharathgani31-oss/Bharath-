from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome setup
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# Open site
driver.get("https://testautomationpractice.blogspot.com/")

print("Current Page Title:", driver.title)

# Store main window
main_window = driver.current_window_handle

# Click "New Tab" button
driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button').click()

# Click popup button
driver.find_element(By.ID, 'PopUp').click()

# Search Selenium in Wikipedia widget
driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input').send_keys("selenium")
driver.find_element(By.CLASS_NAME, 'wikipedia-search-button').click()

# Click "Selenium" link (opens new tab)
driver.find_element(By.LINK_TEXT, 'Selenium').click()

# Get all windows
all_windows = driver.window_handles
print("All Windows:", all_windows)

# Switch to new window (not main)
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

print("Switched Page Title:", driver.title)

# Example: interact in new tab (Wikipedia page)
# You may need to adjust locator depending on page structure
 driver.find_element(By.ID, 'toc-History').click()