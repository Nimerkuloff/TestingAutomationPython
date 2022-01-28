import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button = browser.find_element_by_css_selector('[id="book"]')
    button.click()

    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input_element = browser.find_element_by_css_selector('[id="answer"]')
    input_element.send_keys(y)


    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()



finally:
    time.sleep(4)
    browser.quit()

# не забываем оставить пустую строку в конце файла
