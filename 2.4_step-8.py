from selenium.webdriver.common.by import By     # ПРОГРАММА НАЖИМАЕТ КНОПКУ, КОГДА ЦЕНА ДОСТИГАЕТ НУЖНОЙ ОТМЕТКИ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button.click()

    x = browser.find_element_by_id("input_value").text

    inp = browser.find_element_by_id("answer")
    inp.send_keys(str(log(abs(12 * sin(int(x))))))

    btn = browser.find_element_by_id("solve")
    btn.click()

except Exception as error:
    print(f"ошибка: {error}")

finally:
    time.sleep(5)
    browser.quit()
