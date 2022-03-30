import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):

    locators = basic_locators.SegmentsPageLocators()
    url = 'https://target.my.com/segments/segments_list'

    @allure.step("Ожидание появления надписи 'Список сегментов'")
    def should_be_segments_page_title(self):
        assert self.is_element_present(*self.locators.SEGMENTS_PAGE_TITLE), \
            "segments page title is not presented"

    @allure.step("Ожидание появления кнопки 'Создать новый сегмент'")
    def should_create_new_segment_button(self):
        assert self.is_element_present(*self.locators.CREATE_NEW_SEGMENT_BUTTON), \
            "create new segment button is not presented"

    @allure.step("Ожидание появления меню выбора типа сегмента")
    def should_be_add_menu_title(self):
        assert self.is_element_present(*self.locators.ADD_SEGMENT_MENU_TITLE), \
            "add segment menu title is not presented"

    @allure.step("Ожидание появления кнопки 'Создать сегмент'")
    def should_be_finish_creating_button(self):
        assert self.is_element_present(*self.locators.FINISH_CREATING_SEGMENT_BUTTON), \
            "finish creating button is not presented"

    @allure.step("Ожидание появления поля id для нового сегмента")
    def should_be_segment_id_title(self):
        assert self.is_element_present(*self.locators.FINISH_CREATING_SEGMENT_BUTTON), \
            "segment id title is not presented"

    @allure.step("Ожидание появления чекбокса для нажатия")
    def should_be_checkbox(self):
        assert self.is_element_present(*self.locators.CHECKBOX), \
            "checkbox is not presented"

    @allure.step("Ожидание появления выподающего списка с результатам поиска")
    def should_be_search_result(self):
        assert self.is_element_present(*self.locators.SEARCH_RESULT), \
            "search result is not presented"

    @allure.step("Ожидание появления надписи 'Ничего не найдено'")
    def should_be_nothing_search_result(self):
        assert self.is_element_present(*self.locators.SEARCH_RESULT_NOTHING), \
            "search nothing result is not presented"

    @allure.step("Ожидание появления кнопки 'Удалить'")
    def should_be_confirm_button(self):
        assert self.is_element_present(*self.locators.CONFIRM_BUTTON), \
            "confirm button is not presented"

    @allure.step("Ожидание появления найденого с помощью поиска сегмента")
    def should_be_founded_segment(self, segment_name):
        founded_segment_name = self.find(self.locators.CREATED_SEGMENT_TITLE).text
        assert founded_segment_name == segment_name, "segment was no created"

    @allure.step("Выбор поля 'Приложение и игры в соцсетях'")
    def enter_apps_and_game_field(self):
        self.click(self.locators.APPS_AND_GAME_FIELD)

    @allure.step("Нажатие на чекбокс")
    def enter_checkbox(self):
        checkbox = self.find(self.locators.CHECKBOX)
        checkbox.click()

    @allure.step("Нажатие на кнопку 'Создать сегмент'")
    def click_create_segment_button(self):
        self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON)

    @allure.step("Нажатие на кнопку 'Добавить сегмент'")
    def click_add_segment_button(self):
        self.click(self.locators.ADD_SEGMENT_BUTTON)

    @allure.step("Нажатие на кнопку 'Создать сегмент'")
    def click_finish_create_button(self):
        self.click(self.locators.FINISH_CREATING_SEGMENT_BUTTON)

    @allure.step("Ввести имя компании")
    def set_company_name(self, segment_name):
        name_field = self.find(self.locators.SEGMENT_NAME)
        name_field.clear()
        name_field.send_keys(segment_name)

    @allure.step("Поиск сегмента {name} среди созданных")
    def search_segment(self, name):
        search_field = self.find(self.locators.SEARCH_FIELD)
        search_field.send_keys(name)

    @allure.step("Нажатие на найденный с помощью поиска сегмент")
    def click_on_search_result(self):
        self.click(self.locators.SEARCH_RESULT)

    @allure.step("Нажатие на иконку 'Удалить сегмент'")
    def click_to_remove_icon(self):
        self.click(self.locators.REMOVE_ICON)

    @allure.step("Нажатие на кнопку 'Удалить'")
    def click_to_confirm_button(self):
        self.click(self.locators.CONFIRM_BUTTON)

    @allure.step("Нажатие на иконку 'Аудитории'")
    def click_on_segment_icon(self):
        self.click(self.locators.SEGMENTS_ICON)