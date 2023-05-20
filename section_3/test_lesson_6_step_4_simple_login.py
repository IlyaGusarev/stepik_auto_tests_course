from selenium.webdriver.common.by import By

link = 'https://stepik.org/lesson/236895/step/1'

def test_login_on_stepik(browser):
    browser.implicitly_wait(60)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('username')
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
