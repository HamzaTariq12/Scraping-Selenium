# Imports
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time

# search_text = str(input('Enter text you want to search: ')).title()

# Create Driver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()


page_url = "https://google.com"
driver.get(page_url)

WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'APjFqb')))

googleSearchBox = driver.find_element(By.ID, 'APjFqb')
googleSearchBox.clear()
googleSearchBox.send_keys('Amazon' + Keys.ENTER)

# WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, search_text)))

# amazon_link = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Amazon')
# for link in amazon_link:
#     print(link.text)
# for link in amazon_link:
#     url = link.get_attribute("href")
#     print(url)
# print(amazon_link)
# amazon_link.click()

time.sleep(10)
links = driver.find_elements(By.XPATH, "//div[@class='MjjYud']")
for link in links:
    link.find_element(By.XPATH, "//div/div/div/div/div/span/a/h3")
    print(link.text)
# print(links)




time.sleep(200)
# driver.quit()
print('-----Done-----')