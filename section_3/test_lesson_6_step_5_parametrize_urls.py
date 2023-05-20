import time
import math
import pytest
from selenium.webdriver.common.by import By

# декоратор pytest.mark.parametrize работает примерно так:
# list_elem = [
#     1, 2, 3
# ]
#
# def my_version_parametrize(list_elem):
#     def decorator_func(func):
#         def wrapper():
#             for elem in list_elem:
#                 func(elem)
#         return wrapper
#     return decorator_func
#
# @my_version_parametrize(list_elem)
# def my_func(elem):
#     print(elem)
#
# my_func()

#pytest -s -v --tb=no section_3/test_lesson_6_step_5_parametrize_urls.py

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1,'
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]

@pytest.mark.parametrize('link', links)
def test_lesson6_step5(browser,link):
    browser.implicitly_wait(60)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('username')
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
    time.sleep(10)
    textarea = browser.find_element(By.CSS_SELECTOR, '.quiz-component textarea')
    textarea.clear()
    textarea.send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    time.sleep(10)
    result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    print(f'РЕЗУЛЬТАТ {result}')
    assert result == 'Correct!', result
