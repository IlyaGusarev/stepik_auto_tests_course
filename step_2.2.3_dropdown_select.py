from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота,
# чтобы он справился с новым заданием.
#
# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

link = "https://suninjuly.github.io/selects1.html"

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)
    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(x+y))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()