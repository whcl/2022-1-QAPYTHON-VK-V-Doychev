import os
import shutil
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.create_company_page import CreateCompanyPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.segments_page import SegmentsPage
from userinfo import USERNAME, PASSWORD


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    service = Service(ChromeDriverManager().install())
    if browser == 'chrome':
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)


@pytest.fixture
def create_company_page(driver):
    return CreateCompanyPage(driver=driver)


@pytest.fixture(scope='session')
def credentials():
    return USERNAME, PASSWORD


def get_driver(browser_name):
    if browser_name == 'chrome':
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.should_be_open_login_form_button()
    login_page.open_login_form()
    login_page.should_be_login_form()
    login_page.login(*credentials)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies