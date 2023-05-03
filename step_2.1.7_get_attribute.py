from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с
# изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(browser.find_element(By.ID, "treasure").get_attribute('valuex')))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()