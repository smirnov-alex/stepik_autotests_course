from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

