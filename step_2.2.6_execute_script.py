from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
# который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()