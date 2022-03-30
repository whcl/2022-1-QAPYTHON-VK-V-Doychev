import os
import allure
import pytest
from base import BaseCase


class TestCreateNewCompanyPage(BaseCase):

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'banner.png')

    @allure.epic("Компании")
    @allure.feature("Создание новой компании")
    @allure.story("Появление новой компании в списке созданных")
    @pytest.mark.UI
    def test_user_create_new_company(self, file_path):
        self.main_page.should_be_create_company_button()
        self.create_company_page = self.main_page.\
            go_to_create_company_page()
        self.create_company_page.should_be_create_company_title()
        self.create_company_page.click_traffic_icon()
        self.create_company_page.should_be_link_field()
        self.create_company_page.write_company_url()
        self.create_company_page.should_be_banner_icon()
        self.create_company_page.click_banner_icon()
        self.create_company_page.should_be_upload_button()
        self.create_company_page.upload_banner(file_path)
        self.create_company_page.should_be_save_img_button()
        self.create_company_page.save_image()
        self.create_company_page.should_be_submit_button()
        self.create_company_page.click_submit_button()
        self.create_company_page.should_be_create_company_title()
        self.main_page.should_be_create_company_button()
        self.main_page.should_be_success_message()