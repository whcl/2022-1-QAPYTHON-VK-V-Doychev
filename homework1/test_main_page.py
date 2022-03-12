import pytest
from selenium.webdriver.common.by import By

from BaseCase import BaseCase


MAIN_PAGE_LINK = "https://target.my.com/"
CONTACT_INFO_PAGE_LINK = "https://target.my.com/profile/contacts"

class TestExample(BaseCase):

    @pytest.mark.UI
    def test_user_authorization(self):
        self.go_to_page(MAIN_PAGE_LINK)
        self.should_be_open_login_form_button()
        self.open_login_form()
        self.should_be_login_form()
        self.autorizathion()
        self.should_be_authorization_user_title()


    @pytest.mark.UI
    def test_user_logout(self):
        self.go_to_page(MAIN_PAGE_LINK)
        self.should_be_open_login_form_button()
        self.open_login_form()
        self.should_be_login_form()
        self.autorizathion()
        self.should_be_authorization_user_title()
        self.open_user_wrap()
        self.should_be_logout_button()
        self.logout()
        self.should_be_open_login_form_button()


    @pytest.mark.UI
    def test_user_change_contact_information(self):
        self.go_to_page(MAIN_PAGE_LINK)
        self.should_be_open_login_form_button()
        self.open_login_form()
        self.should_be_login_form()
        self.autorizathion()
        self.should_be_authorization_user_title()
        self.go_to_page(CONTACT_INFO_PAGE_LINK)
        self.should_be_contact_info_title()
        self.change_contact_information()
        self.should_be_success_text()


    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator, url',
        [
            pytest.param
            (
                (By.CSS_SELECTOR, '[href="/segments"]'), 'segments'
            ),
            pytest.param(
                (By.CSS_SELECTOR, '[href="/statistics"]'), 'statistics'
            ),
        ],
    )
    def test_go_to_new_page(self, locator, url):
        self.go_to_page(MAIN_PAGE_LINK)
        self.should_be_open_login_form_button()
        self.open_login_form()
        self.should_be_login_form()
        self.autorizathion()
        self.should_be_authorization_user_title()
        self.go_to_new_page(locator)
        self.should_be_correct_url(url)










