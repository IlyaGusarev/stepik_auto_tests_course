from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание: поиск элемента по тексту в ссылке
# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
# Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
# Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов.
# Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут
# проходить только с определенным языком интерфейса. Применяйте этот метод с осторожностью и помните про возможные
# ограничения.


link = "http://suninjuly.github.io/find_link_text"

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла