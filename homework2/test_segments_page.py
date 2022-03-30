import allure
import pytest
import random
from base import BaseCase


class TestCreateNewSegmentPage(BaseCase):

    SEGMENT_NAME = ''.join([random.choice(list('abcdefgh'))
                           for x in range(12)])

    @allure.epic("Аудитории")
    @allure.feature("Создание нового сегмента")
    @allure.story("Появление созданого сегмента в списке")
    @pytest.mark.UI
    def test_user_create_segment(self):
        self.main_page.should_be_create_company_button()
        self.segments_page = self.main_page.go_to_segments_page()
        self.segments_page.should_be_segments_page_title()
        self.segments_page.should_create_new_segment_button()
        self.segments_page.click_create_segment_button()
        self.segments_page.should_be_add_menu_title()
        self.segments_page.enter_apps_and_game_field()
        self.segments_page.should_be_checkbox()
        self.segments_page.enter_checkbox()
        self.segments_page.click_add_segment_button()
        self.segments_page.should_be_finish_creating_button()
        self.segments_page.set_company_name(self.SEGMENT_NAME)
        self.segments_page.click_finish_create_button()
        self.segments_page.should_create_new_segment_button()
        self.segments_page.search_segment(self.SEGMENT_NAME)
        self.segments_page.should_be_search_result()
        self.segments_page.click_on_search_result()
        self.segments_page.should_be_founded_segment(self.SEGMENT_NAME)

    @allure.epic("Аудитории")
    @allure.feature("Удаление сегмента")
    @allure.story("Отсутсвие удаленного сегмента в результатах поиска")
    @pytest.mark.UI
    def test_user_delete_segment(self):
        self.main_page.should_be_create_company_button()
        self.segments_page = self.main_page.go_to_segments_page()
        self.segments_page.should_be_segments_page_title()
        self.segments_page.should_create_new_segment_button()
        self.segments_page.click_create_segment_button()
        self.segments_page.should_be_add_menu_title()
        self.segments_page.enter_apps_and_game_field()
        self.segments_page.should_be_checkbox()
        self.segments_page.enter_checkbox()
        self.segments_page.click_add_segment_button()
        self.segments_page.should_be_finish_creating_button()
        self.segments_page.set_company_name(self.SEGMENT_NAME)
        self.segments_page.click_finish_create_button()
        self.segments_page.should_create_new_segment_button()
        self.segments_page.search_segment(self.SEGMENT_NAME)
        self.segments_page.should_be_search_result()
        self.segments_page.click_on_search_result()
        self.segments_page.should_be_founded_segment(self.SEGMENT_NAME)
        self.segments_page.click_to_remove_icon()
        self.segments_page.should_be_confirm_button()
        self.segments_page.click_to_confirm_button()
        self.segments_page.should_be_segments_page_title()
        self.segments_page.click_on_segment_icon()
        self.segments_page.should_be_segments_page_title()
        self.segments_page.search_segment(self.SEGMENT_NAME)
        self.segments_page.should_be_nothing_search_result()