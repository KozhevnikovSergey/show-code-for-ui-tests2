import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.page import MainPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def main_page(driver):
    yield MainPage(driver).open()
    driver.delete_all_cookies()
    driver.refresh()


@pytest.fixture(scope="function")
def main_page_with_task(main_page):
    """
    Подготовка страницы(наполнение) для проведение тестов.
    """
    tasks = ['Test1', 'Test3{{]]', 'Test4sdsad//__']
    for task in tasks:
        main_page.added_task(task)
    return main_page
