import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Checkpoint function used in-dev to pause the script and examine.
# Checkpoint will allow to pause while the script is being worked, while Quit will just tell the driver to quit.
# They can work with Selenium commands but i wanted to just have them like a small function.
def checkpoint():
    time.sleep(10)

def quit():
    driver.quit()

# Opening of the website and declaration of the driver
driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com')
time.sleep(2)

# 1. A/B Testing

# Find the element using the relative XPath
element = driver.find_element(By.XPATH, "//a[contains(text(),'A/B Testing')]")

# Perform actions on the element, if needed
# For example, click on the element
element.click()
time.sleep(2)
driver.back()

#checkpoint()
#quit()

# 2. Add/Remove Elements
element = driver.find_element(By.XPATH,  "//a[contains(text(),'Add/Remove Elements')]")
element.click()
time.sleep(2)
add_element_button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
add_element_button.click()
time.sleep(2)
delete_button = driver.find_element(By.CSS_SELECTOR, "button.added-manually")
delete_button.click()
driver.back()
#checkpoint()
#quit()

# 3. Basic Auth
# stuck here (?)
element = driver.find_element(By.XPATH,"//a[contains(text(),'Basic Auth')]")
element.click()
time.sleep(2)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("admin")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("admin")
password_field.send_keys(Keys.RETURN)
driver.implicitly_wait(10)