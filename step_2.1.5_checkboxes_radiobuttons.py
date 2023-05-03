from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу
# для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
#
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()