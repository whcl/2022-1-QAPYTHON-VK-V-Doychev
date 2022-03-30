import pytest
import random
import allure
from base import BaseCase
from userinfo import USERNAME, PASSWORD


class TestLogin(BaseCase):

    authorize = False
    WRONG_VALUE = ''.join([random.choice(list('abcdefgh'))
                           for x in range(12)])

    @allure.epic("Авторизация")
    @allure.feature("Ошибка авторизации при неккоректных данных")
    @allure.story("Переход на сайт для ввода корректных данных"
                  "при ошибке ввода пароля")
    @pytest.mark.UI
    def test_user_authorization_negative_wrong_passw(self):
        self.login_page.should_be_open_login_form_button()
        self.login_page.open_login_form()
        self.login_page.should_be_login_form()
        self.main_page = self.login_page.login(USERNAME, self.WRONG_VALUE)
        self.main_page.should_be_wrong_url()

    @allure.epic("Авторизация")
    @allure.feature("Ошибка авторизации при неккоректных данных")
    @allure.story("Вывод сообщения о необходимости ввести почту или телефон"
                  "при ошибке ввода")
    @pytest.mark.UI
    def test_user_authorization_negative_wrong_username(self):
        self.login_page.should_be_open_login_form_button()
        self.login_page.open_login_form()
        self.login_page.should_be_login_form()
        self.login_page.login(self.WRONG_VALUE, PASSWORD)
        self.login_page.should_be_wrong_username_title()