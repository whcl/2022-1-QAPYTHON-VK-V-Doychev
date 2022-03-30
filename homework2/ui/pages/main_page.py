import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentsPage
from ui.pages.create_company_page import CreateCompanyPage


class MainPage(BasePage):

    locators = basic_locators.MainPageLocators()
    url = 'https://target.my.com/dashboard'

    @allure.step("Переход на страницу 'Аудитории'")
    def go_to_segments_page(self):
        self.click(self.locators.SEGMENTS_ICON)
        return SegmentsPage(self.driver)

    @allure.step("Ожидание появления кнопки 'Cоздать новую компанию")
    def should_be_create_company_button(self):
        assert self.is_element_present(*self.locators.CREATE_NEW_COMPANY_BUTTON), \
            "create company button is not presented"

    @allure.step("Ожидание появления надписи об успешном создании компании")
    def should_be_success_message(self):
        assert self.is_element_present(*self.locators.SUCCESS_MESSAGE), \
            "succes message is not presented"

    @allure.step("Ожидание появления иконки 'Аудитории'")
    def should_be_segments_icon(self):
        assert self.is_element_present(*self.locators.SEGMENTS_ICON), \
            "segments icon is not presented"

    @allure.step("Переход на страницу 'Компании'")
    def go_to_create_company_page(self):
        self.click(self.locators.CREATE_NEW_COMPANY_BUTTON)
        return CreateCompanyPage(self.driver)