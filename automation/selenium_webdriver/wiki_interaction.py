from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# select and click
# stats = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
# stats.click()
# print(stats.text)

# fill forms
search = driver.find_element(By.NAME, "search")
search.send_keys("python", Keys.ENTER)

driver.quit()
