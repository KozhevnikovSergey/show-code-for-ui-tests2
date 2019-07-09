from selenium.webdriver.common.keys import Keys

from src.common import search_element


class MainPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://todomvc.com/examples/react/#/")
        return self

    def added_task(self, text):
        search_element(self.driver, 'css', 'new-todo').send_keys(text)
        search_element(self.driver, 'css', 'new-todo').send_keys(Keys.ENTER)

