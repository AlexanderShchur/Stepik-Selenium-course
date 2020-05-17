from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    select_checkbox = browser.find_element_by_id("robotCheckbox")
    select_checkbox.click()
    select_checkbox = browser.find_element_by_id("robotsRule")
    select_checkbox.click()
    # button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
