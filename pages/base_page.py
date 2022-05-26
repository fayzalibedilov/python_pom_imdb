from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_list_elements_text(self, by_locator):
        elements = [element.text for element in
                    WebDriverWait(self.driver, 1000).until(EC.visibility_of_all_elements_located(by_locator))]
        return elements

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 1000).until(EC.title_is(title))
        return self.driver.title
