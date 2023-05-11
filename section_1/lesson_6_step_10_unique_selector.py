from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Вам дана страница с формой регистрации. Проверьте, что можно зарегистрироваться на сайте, заполнив только
# обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей может быть любым.
# Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
# с текстом на странице, которая открывается после регистрации.

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Test')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Test')
    browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('test@test.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()