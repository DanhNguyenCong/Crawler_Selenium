import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
# Declare browser
driver = webdriver.Chrome(service= Service("D:/chromedriver-win32/chromedriver.exe"))

driver.get("https://xe.chotot.com/mua-ban-oto-cu-sdca1")
sleep(random.randint(5,10))


# ================================ GET Link
elems_link = driver.find_elements("xpath", '//*[@id="__next"]/div/div[4]/div[1]/div[3]/main/div[1]/div[4]/div/div[1]/ul/div[1]/div/li/a')
links = [elem_link for elem_link in elems_link]

# ================================ GET title
elems = driver.find_elements(By.CSS_SELECTOR , ".ard7gu7")
title = [elem.text for elem in elems]
# ================================ GET price
elems_price = driver.find_elements(By.CSS_SELECTOR , ".szp40s8 r9vw5if .bfe6oav")
price = [elem_price.text for elem_price in elems_price]



print(links)
print("\n", title)
print("\n", price)