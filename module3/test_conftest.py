'''
 у тестов будет доступ к фикстуре browser. Фикстура передается в тестовый метод в качестве аргумента
'''

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")