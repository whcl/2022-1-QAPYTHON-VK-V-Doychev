import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    locators = basic_locators.BasePageLocators()
    url = 'https://target.my.com/dashboard'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step("Нажатие на иконку пользователя")
    def open_user_wrap(self):
        user_wrap = self.find(self.locators.USER_WRAP)
        user_wrap.click()

    @allure.step("Разлогирование")
    def logout(self):
        logout_button = self.find(self.locators.LOGOUT_BUTTON)
        logout_button.click()

    def is_element_present(self, how, what, timeout=90):
        try:
            self.wait(timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step("Проверка на совпадение url с текущим")
    def should_be_correct_url(self, url):
        assert url in self.driver.current_url, f'current url has no {url} element'

    @allure.step("Проверка на несовпадение url c текущим")
    def should_be_wrong_url(self):
        assert self.url != self.driver.current_url, f'current url should be not {self.url}'