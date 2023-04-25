import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = ' https://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "num1")
    x2 = browser.find_element(By.ID, "num2")
    y = int(x1.text) + int(x2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))  # ищем элемент с текстом "Python"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
