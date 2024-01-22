import allure
import pytest
from pages.head_page import HeadPage
from urls import Url
from constants import Constant



class TestAccordion:
    @allure.story("Главная страница")
    @allure.feature("Тестирование раздела Вопросы о важном")
    @pytest.mark.parametrize('locator_find, locator_check, check_text', Constant.accordion_rows_params)
    def test_arrows(self, driver, locator_find, locator_check, check_text):
        hp = HeadPage(driver)
        hp.go_to_site(Url.base_url)
        hp.find_row_and_click(locator=locator_find)
        assert hp.find_row_answer(locator=locator_check).text == check_text
