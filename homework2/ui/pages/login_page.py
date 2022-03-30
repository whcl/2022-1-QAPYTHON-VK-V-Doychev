import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators()
    url = 'https://target.my.com/'

    @allure.step("Клик по кнопке 'Войти'")
    def open_login_form(self):
        self.click(self.locators.OPEN_LOGIN_FORM_BUTTON)

    @allure.step("Заполнение полей email и password")
    def login(self, username, password):
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.send_keys(username)
        password_field = self.find(self.locators.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)
        return MainPage(self.driver)

    @allure.step("Ожидание появления кнопки для открытия формы авторизации")
    def should_be_open_login_form_button(self):
        assert self.is_element_present(*self.locators.OPEN_LOGIN_FORM_BUTTON),\
            "Login form button is not presented"

    @allure.step("Ожидание появления формы авторизации")
    def should_be_login_form(self):
        assert self.is_element_present(*self.locators.LOGIN_FORM_HEADER),\
            "Login form header is not presented"

    @allure.step("Ожидание появления сообщения об ошибке введеного имени")
    def should_be_wrong_username_title(self):
        assert self.is_element_present(*self.locators.WRONG_USERNAME_TITLE), \
            "wrong username is not presented"