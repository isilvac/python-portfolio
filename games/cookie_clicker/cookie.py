from selenium import webdriver
from selenium.webdriver.common.by import By
import re

PLAY_TURNS = 15

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# elements
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")


def get_store() -> list:
    """ Gets available products for purchase """
    store = driver.find_element(By.XPATH, '// *[ @ id = "store"]')

    sellable_items = []
    for product_item in store.find_elements(By.TAG_NAME, "b"):
        # print(f"product available: {product_item.text}")
        element = product_item.text.split(" - ")
        if len(element) > 1:
            sellable_items.append({"product_name": element[0], "cost": re.sub(',', '', element[1])})
    # print(f"Offer: {sellable_items}")
    return sellable_items


def get_priciest_option(products: list) -> str:
    """ Gets the highest price product available for purchase """
    option = products[0]
    print(f"Money account: {int(money.text)}")

    for item in products:
        if int(option["cost"]) <= int(item["cost"]) < int(money.text):
            option = item
    return option["product_name"]


while True:
    # click the cookie for 30 sec
    for _ in range(0, 100):
        cookie.click()
    # get offers
    options = get_store()

    # purchase the highest price product
    purchase = get_priciest_option(options)
    product = driver.find_element(By.ID, f"buy{purchase}")
    print(f"{purchase} purchased")
    product.click()
    if PLAY_TURNS >= 0:
        PLAY_TURNS -= 1
    else:
        break

driver.quit()
