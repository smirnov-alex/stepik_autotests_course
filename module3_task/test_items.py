from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.get(link)
    # Задержка, чтобы проверить, что язык изменился:
    # time.sleep(15)
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button_add_to_basket, 'Button "Add to basket" not found!'


