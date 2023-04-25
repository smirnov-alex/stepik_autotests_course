import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
#print(current_dir)

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("smolensk@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
