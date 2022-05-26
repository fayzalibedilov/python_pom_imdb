from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import TestData


class LoginPage(BasePage):

    # Locators
    LOGIN_LINK = (By.XPATH, "//div[@class='nav__userMenu navbar__user sc-kLgntA iHaOcn']")
    SIGN_IN_WITH_IMDB_BTN = (By.XPATH, "//span[contains(text(),'Sign in with IMDb')]")
    EMAIL_FIELD = (By.ID, "ap_email")
    PASSWORD_FIELD = (By.ID, "ap_password")
    SIGN_IN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.click(self.SIGN_IN_WITH_IMDB_BTN)
        self.send_keys(self.EMAIL_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BTN)
