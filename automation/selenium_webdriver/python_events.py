from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
results = {}
position = 0
for item in events:
    element = {
        "time": item.find_element(By.TAG_NAME, "time").text,
        "name": item.find_element(By.TAG_NAME, "a").text
    }
    results[position] = element
    position += 1

# driver.close()
driver.quit()
pprint(results)
