from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    # Locators
    ACCOUNT_ICON = (By.XPATH, "(//*[@id='iconContext-account-circle'])[2]")
    ACCOUNT_NAME = (By.XPATH, "(//span[text()='ali'])[2]")
    TITLE_OF_THE_MOVIE = (By.XPATH, "(//span[@data-testid])[1]")
    ADD_TO_WATHCLIST_BTN = (By.XPATH, "(//*[@id='iconContext-add'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def does_account_icon_exist(self):
        return self.is_visible(self.ACCOUNT_ICON)

    def get_account_name_value(self):
        return self.get_element_text(self.ACCOUNT_NAME)

    def get_title_of_the_movie(self):
        return self.get_element_text(self.TITLE_OF_THE_MOVIE)

    def add_movie_to_watchlist(self):
        return self.click(self.ADD_TO_WATHCLIST_BTN)
