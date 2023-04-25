import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Ответ")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

