from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Задание: поиск элемента по XPath
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
# при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit",
# и наша задача нажать в коде именно на неё.

link = "http://suninjuly.github.io/find_xpath_form"

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[contains(text(),"Submit")]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла