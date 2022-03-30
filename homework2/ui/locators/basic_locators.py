from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_WRAP = (By.CSS_SELECTOR, '[class^= "right-module-userNameWrap"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[href= "/logout"]')
    SEGMENTS_ICON = (By.CSS_SELECTOR, '[href="/segments"]')


class LoginPageLocators(BasePageLocators):
    OPEN_LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, '[class^= "responseHead-module-button"]')
    LOGIN_FORM_HEADER = (By.CSS_SELECTOR, '[class^= "authForm-module-title"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class^= "authForm-module-button"]')
    WRONG_USERNAME_TITLE = (By.CSS_SELECTOR, '[class^="notify-module-content"]')


class SegmentsPageLocators(BasePageLocators):
    SEGMENTS_PAGE_TITLE = (By.CSS_SELECTOR, '.page_segments__title')
    SEGMENT_NAME = (By.CSS_SELECTOR, '.input_create-segment-form input')
    CREATE_NEW_SEGMENT_BUTTON = (By.CSS_SELECTOR, '.js-create-button-wrap')
    ADD_SEGMENT_MENU_TITLE = (By.CSS_SELECTOR, '.js-modal-title')
    APPS_AND_GAME_FIELD = (By.CSS_SELECTOR, '.adding-segments-item:nth-child(8)')
    CHECKBOX = (By.CSS_SELECTOR, '.js-main-source-checkbox')
    ADD_SEGMENT_BUTTON = (By.CSS_SELECTOR, '.js-add-button')
    FINISH_CREATING_SEGMENT_BUTTON = (By.CSS_SELECTOR, '.button_submit')
    SEARCH_FIELD = (By.CSS_SELECTOR, '[class*="searchInput"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '[class*="suggester-module-optionList"]')
    SEARCH_RESULT_NOTHING = (By.CSS_SELECTOR, '[data-test="nothing"]')
    CREATED_SEGMENT_TITLE = (By.CSS_SELECTOR, '[class*="cells-module-nameCell-zlAsWX"] a')
    REMOVE_ICON = (By.CSS_SELECTOR, '[class*="cells-module-removeCell"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '[class*="button_confirm-remove button_general"]')


class MainPageLocators(BasePageLocators):
    AUTHORIZATION_USER_TITLE = (By.CSS_SELECTOR, '[class^="instruction-module-title"]')
    CREATE_NEW_COMPANY_BUTTON = (By.CSS_SELECTOR, '[class^="dashboard-module-createButtonWrap"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[class*="toast-module-successIcon"]')


class CreateCompanyPage(BasePageLocators):
    CREATE_COMPANY_TITLE = (By.CSS_SELECTOR, '.breadcrumbs__text')
    TRAFFIC_ICON = (By.CSS_SELECTOR, '[class*="traffic"]')
    LINK_FIELD = (By.CSS_SELECTOR, '[data-gtm-id="ad_url_text"]')
    BANNER_ICON = (By.CSS_SELECTOR, '[id*="patterns_banner"]')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, '[data-test="image_240x400"]')
    SAVE_IMAGE_BUTTON = (By.CSS_SELECTOR, '[data-translated-lit="Save image"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.js-save-button-wrap')