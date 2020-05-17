from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    num2 = int(num2.text)
    summary = str(num1 + num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summary)

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
