from selenium.webdriver.common.by import By


class MainPageLocators():
    OPEN_LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, '[class^= "responseHead-module-button"]')
    LOGIN_FORM_HEADER = (By.CSS_SELECTOR, '[class^= "authForm-module-title"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class^= "authForm-module-button"]')
    USER_WRAP = (By.CSS_SELECTOR, '[class^= "right-module-userNameWrap"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[href= "/logout"]')
    AUTHORIZATION_USER_TITLE = (By.CSS_SELECTOR, '[class^="instruction-module-title"]')
    SEGMENTS_ICON = (By.CSS_SELECTOR, '[href="/segments"]')
    STATISTICS_ICON = (By.CSS_SELECTOR, '[href="/statistics"]')


class ConstactInformationPageLocators():
    NAME_FIELD = (By.CSS_SELECTOR, '[data-name="fio"] .input__inp')
    PHONE_FIELD = (By.CSS_SELECTOR, '[data-name="phone"] .input__inp')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[class="button button_submit"]')
    CONTACT_INFO_TITLE = (By.CSS_SELECTOR, '[data-translated="Contact information"]')
    SUCCESS_TEXT = (By.CSS_SELECTOR, '[data-class-name="SuccessView"] > ._notification__content')