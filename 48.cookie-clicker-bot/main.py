from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r'C:\Development\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
big_cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in store]


timeout = time.time() + 5
five_min = time.time() + 5*60

game_on = True
while game_on:
    big_cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split(" - ")[1].replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        affordable_items = []
        for cost, id in cookie_upgrades.items():
            if money >= cost:
                affordable_items.append(cookie_upgrades[cost])

        purchase_item = driver.find_element(By.ID, affordable_items[-1])
        purchase_item.click()

        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break



