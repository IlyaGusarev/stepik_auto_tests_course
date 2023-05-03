from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver
# на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.window(browser.window_handles[1])
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()