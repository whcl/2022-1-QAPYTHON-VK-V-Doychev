import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CreateCompanyPage(BasePage):

    locators = basic_locators.CreateCompanyPage()
    url = 'https://target.my.com/campaign/new'

    @allure.step("Ожидание появления надписи 'Создать компанию'")
    def should_be_create_company_title(self):
        assert self.is_element_present(*self.locators.CREATE_COMPANY_TITLE), \
            "create company title is not presented"

    @allure.step("Клик на цель 'Трафик'")
    def click_traffic_icon(self):
        self.click(self.locators.TRAFFIC_ICON)

    @allure.step("Клик на формат 'Баннер'")
    def click_banner_icon(self):
        self.click(self.locators.BANNER_ICON)

    @allure.step("Ожидание появления поля для ввода ссылки")
    def should_be_link_field(self):
        assert self.is_element_present(*self.locators.LINK_FIELD), \
            "field for link of company is not presented"

    @allure.step("Ввод ссылки")
    def write_company_url(self):
        link_field = self.find(self.locators.LINK_FIELD)
        link_field.send_keys("https://github.com/")

    @allure.step("Ожидание появления иконки баннера")
    def should_be_banner_icon(self):
        assert self.is_element_present(*self.locators.BANNER_ICON), \
            "banner icon is not presented"

    @allure.step("Ожидания появления кнопки для добавления картинки")
    def should_be_upload_button(self):
        assert self.is_element_present(*self.locators.UPLOAD_BUTTON), \
            "upload button is not presented"

    @allure.step("Ожидания появления кнопки для сохранения картинки")
    def should_be_save_img_button(self):
        assert self.is_element_present(*self.locators.SAVE_IMAGE_BUTTON), \
            "save image button is not presented"

    @allure.step("Ожидания появления кнопки для завершения создания компании")
    def should_be_submit_button(self):
        assert self.is_element_present(*self.locators.SUBMIT_BUTTON), \
            "submit button is not presented"

    @allure.step("Загрузка изображения баннера")
    def upload_banner(self, file_path):
        upload_button = self.find(self.locators.UPLOAD_BUTTON)
        upload_button.send_keys(file_path)

    @allure.step("Нажатие на кнопку 'Сохранить изображение'")
    def save_image(self):
        self.click(self.locators.SAVE_IMAGE_BUTTON)

    @allure.step("Нажатие на кнопку 'Создать компанию'")
    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)