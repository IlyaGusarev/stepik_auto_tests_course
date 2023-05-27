from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

#pytest -s -v --browser_name=chrome section_3/test_lesson_6_step_7_choose_browser.py
#pytest -s -v --browser_name=firefox section_3/test_lesson_6_step_7_choose_browser.py

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")