from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WatchlistPage(BasePage):

    # Locators
    WATCHLIST_ICON = (By.ID, "iconContext-watchlist")
    LIST_OF_THE_MOVIE = (By.XPATH, "//h3[@class='lister-item-header']//a")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_watchlist(self):
        self.click(self.WATCHLIST_ICON)

    def get_watchlist_page_title(self, title):
        return self.get_title(title)

    def get_list_of_movies(self):
        return self.get_list_elements_text(self.LIST_OF_THE_MOVIE)
