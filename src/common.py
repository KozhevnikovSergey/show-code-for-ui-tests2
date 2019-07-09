from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def search_element(driver, locator, selector):
    """
    Поиск элементов, о разным локатарам, с ожиданием когда он будет кликабельный
    :return: найденный элемент
    """
    if locator == 'css':
        locator = By.CLASS_NAME
    elif locator == 'xpath':
        locator = By.XPATH
    return WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((locator, selector))
    )


def complete_all_tasks(main_page_with_task):
    for task in main_page_with_task.driver.find_elements_by_xpath("//input[@class='toggle']"):  # прогон по всем задачам
        task.click()  # завершение задачи


def check_that_all_tasks_completed(main_page_with_task):
    for task in main_page_with_task.driver.find_elements_by_xpath("//section/ul/li"):
        if not task.get_attribute("class") == 'completed':  # у атрибута class должен быть проставлен статус 'completed'
            return False
    return True
