import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action = 'store',
        default = 'chrome',
        help = 'Choose browser'
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")
        service = FirefoxService(driver_loc)
        opts = webdriver.FirefoxOptions()
        opts.binary_location = binary_loc
        opts.set_preference("dom.webdriver.enabled", False)
        browser = webdriver.Firefox(service=service, options=opts)
    else:
        raise pytest.UsageError(
            '--browser_name should be chrome or firefox'
        )
    yield browser
    browser.quit()