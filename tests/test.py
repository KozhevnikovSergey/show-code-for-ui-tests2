from src.common import search_element, complete_all_tasks, check_that_all_tasks_completed


class TestTodomvc(object):

    def test_added_task(self, driver, main_page):
        """
        Добавление задачи
        """
        text = 'Test'
        main_page.added_task(text)
        driver.add_cookie({'domain': '.todomvc.com', 'name': '123', 'value': '231241'})
        assert text in driver.page_source, f'Недобавилась задача: {text}'
        assert search_element(driver, 'xpath', '//div/label').text == text, 'Некорректно добавилась задача'

    def test_complete_all_task(self, main_page_with_task):
        """
        Завершение всех задач
        """
        complete_all_tasks(main_page_with_task)
        assert check_that_all_tasks_completed(main_page_with_task)

