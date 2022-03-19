import pytest
from ui.locators import MainPageLocators, ConstactInformationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from userinfo import PASSWORD, LOGIN
import random


class BaseCase:
    driver = None
    NUMBERS_FOR_RANDOM_VALUE = '123456789'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver


    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def go_to_page(self, link):
        self.driver.get(link)


    def find(self, locator):
        return self.driver.find_element(*locator)


    def open_login_form(self):
        login_form_button = self.find(MainPageLocators.OPEN_LOGIN_FORM_BUTTON)
        login_form_button.click()


    def autorizathion(self):
        email_field = self.find(MainPageLocators.EMAIL_FIELD)
        email_field.send_keys(LOGIN)
        password_field = self.find(MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD)
        login_button = self.find(MainPageLocators.LOGIN_BUTTON)
        login_button.click()


    def open_user_wrap(self):
        user_wrap = self.find(MainPageLocators.USER_WRAP)
        user_wrap.click()


    def logout(self):
        logout_button = self.find(MainPageLocators.LOGOUT_BUTTON)
        logout_button.click()


    def change_contact_information(self):
        name_field = self.find(ConstactInformationPageLocators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(''.join([random.choice(list(self.NUMBERS_FOR_RANDOM_VALUE)) for x in range(12)]))
        phone_field = self.find(ConstactInformationPageLocators.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(''.join([random.choice(list(self.NUMBERS_FOR_RANDOM_VALUE)) for x in range(12)]))
        save_button = self.find(ConstactInformationPageLocators.SAVE_BUTTON)
        save_button.click()


    def go_to_new_page(self, locator):
        new_page_button = self.find(locator)
        new_page_button.click()


    def should_be_correct_url(self, url):
        assert url in self.driver.current_url, f'current url has no {url} element'


    def should_be_contact_info_title(self):
        assert self.is_element_present(*ConstactInformationPageLocators.CONTACT_INFO_TITLE),\
            "Contact information title text is not presented"


    def should_be_success_text(self):
        assert self.is_element_present(*ConstactInformationPageLocators.SUCCESS_TEXT),\
            "Success text is not presented"


    def should_be_logout_button(self):
        assert self.is_element_present(*MainPageLocators.LOGOUT_BUTTON),\
            "Logout form button is not presented"


    def should_be_open_login_form_button(self):
        assert self.is_element_present(*MainPageLocators.OPEN_LOGIN_FORM_BUTTON),\
            "Login form button is not presented"


    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM_HEADER),\
            "Login form header is not presented"


    def should_be_authorization_user_title(self):
        assert self.is_element_present(*MainPageLocators.AUTHORIZATION_USER_TITLE), \
            "authorization title is not presented"