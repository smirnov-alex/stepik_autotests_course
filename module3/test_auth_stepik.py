import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905',]


@pytest.mark.parametrize('lesson', lessons)
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1?auth=login"
    browser.get(link)
    time.sleep(10)
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys('a.smirnov@mail.ru')
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys('1234567890')
    button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button.click()
    time.sleep(5)
    answer = math.log(int(time.time()))
    input_answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    input_answer.send_keys(str(answer))
    button_ans = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button_ans.click()
    time.sleep(5)
    feedback_elt = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    feedback_text = feedback_elt.text
    time.sleep(5)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == feedback_text, f"feedback is not correct: {feedback_text}"
