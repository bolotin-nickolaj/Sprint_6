import allure
from pages.base_page import BasePage

class HeadPage(BasePage):
    @allure.step('Найти элемент-вопрос в разделе Вопросы о важном и кликнуть на нем')
    def find_row_and_click(self, locator):
        self.find_element_located_with_scroll_click(locator=locator)

    @allure.step('Найти открывшийся после клика на вопросе элемент-ответ в разделе Вопросы о важном')
    def find_row_answer(self, locator):
        return self.find_element_locator(locator)

    @allure.step('Найти элемент и кликнуть на нем')
    def find_element_and_click(self, locator):
        self.find_element_located_with_scroll_click(locator=locator)
