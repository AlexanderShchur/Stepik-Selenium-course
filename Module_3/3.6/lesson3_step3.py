from telnetlib import EC

import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data_test = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def send_answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize('link', data_test)
def test_optional_feedback(browser, link):
    browser.get(link)
    answer = send_answer()
    WebDriverWait(browser, 7).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "textarea.string-quiz__textarea.ember-text-area.ember-view"))
    )
    text_input = browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view")
    text_input.send_keys(str(answer))
    tap_button = browser.find_element_by_class_name("submit-submission")
    tap_button.click()

    hint = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    alert = hint.text
    assert alert == "Correct!", f"Alert '''{alert}''' don't match with correct string"




