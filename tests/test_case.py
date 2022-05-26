import unittest
from config.config import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.watchlist_page import WatchlistPage
from selenium import webdriver


class ImdbAddMovie(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    def test_login_page_title(self):

        self.lp = LoginPage(self.driver)
        login_title = self.lp.get_title(TestData.LOGIN_PAGE_TITLE)
        assert login_title == TestData.LOGIN_PAGE_TITLE
        print(login_title)

        self.lp.login(TestData.USER_NAME, TestData.PASSWORD)

        hp = HomePage(self.driver)
        home_title = hp.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE
        print(home_title)
        assert hp.does_account_icon_exist()

        movie_title1 = hp.get_title_of_the_movie()
        print(movie_title1)
        hp.add_movie_to_watchlist()

        wp = WatchlistPage(self.driver)
        wp.go_to_watchlist()

        watchlist_title = wp.get_watchlist_page_title(TestData.WATCHLIST_PAGE_TITLE)
        assert watchlist_title == TestData.WATCHLIST_PAGE_TITLE
        print(watchlist_title)

        movie_list = wp.get_list_of_movies()
        print(movie_list)

        if movie_title1 in movie_list:
            print(movie_title1 + " is in the Watchlist")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
