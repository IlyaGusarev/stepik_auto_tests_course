import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# pytest -v --tb=line --language=es section_3/test_lesson_6_step_10_va_languages.py

def test_button_add_to_basket_on_page(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements(By.CSS_SELECTOR, '.add-to-basket button.btn-add-to-basket')
    assert button, 'No button on current page.'
