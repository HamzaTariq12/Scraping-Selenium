# # Imports
# import pandas as pd
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# # Create Driver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# page_url = "https://witcher.fandom.com/wiki/Category:Characters_in_the_stories"

# driver.get(page_url)


# Imports
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
import time

# Create Driver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()


# page_url = "https://google.com"
page_url = "https://trytestingthis.netlify.app/index.html"
driver.get(page_url)

# -- Google Search
# googleSearchBox = driver.find_element(By.ID, 'APjFqb')
# googleSearchBox.send_keys("Linkedin")
# googleSearchBox.send_keys(Keys.RETURN)

# -- Automation Testing
# name fields
first_name = driver.find_element(By.ID, 'fname').send_keys("Hamza")
last_name = driver.find_element(By.ID, 'lname').send_keys("Tariq")
# gender
gender = driver.find_element(By.ID, 'male')
gender.click()
# dropdown
option_dropdown = driver.find_element(By.ID, "option")
option_dropdown = Select(option_dropdown)

option_dropdown.select_by_visible_text("Option 2")
# select multiple
multi_select_dropdown_element = driver.find_element(By.ID, "owc")
multi_select_dropdown = Select(multi_select_dropdown_element)

multi_select_dropdown.select_by_visible_text("Option 1")
multi_select_dropdown.select_by_visible_text("Option 2")
# select checkbox
checkbox_names = ["option1", "option2", "option3"]
for checkbox_name in checkbox_names:
    checkbox = driver.find_element(By.NAME, checkbox_name)
    checkbox.click()
# input answer
select_input_field = driver.find_element(By.XPATH, "//input[@name='Options']").send_keys("Chocolate")
# change color
color_input = driver.find_element(By.ID, "favcolor")
color_input.clear()
color_input.send_keys("#336699")
# change date
date_input = driver.find_element(By.ID, "day")
date_input.clear()
date_input.send_keys("07-02-2024")
# select scroll range
range_input = driver.find_element(By.ID, "a")
range_input.send_keys(Keys.ARROW_RIGHT * 25)
# select file
file_input = driver.find_element(By.ID, 'myfile')
file_path = r"C:\Users\hamza\OneDrive\Desktop\prep_sel\default.jpg"
file_input.send_keys(file_path)
# select quantity range
quantity_range = driver.find_element(By.ID, 'quantity').send_keys('5')
# select long message
long_message = driver.find_element(By.NAME, 'message')
long_message.clear()
long_message.send_keys('Hello this is my auto bot.')
# submit form
submit_btn = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
submit_btn.click()

time.sleep(20)
driver.quit()
print("Done")