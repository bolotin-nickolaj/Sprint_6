import allure
import pytest

from pages.order_page import OrderPage
from urls import Url
from constants import Constant

class TestOrderPage:
    @allure.story("Страница заказа")
    @allure.feature("Тестирование страницы заказа")
    @pytest.mark.parametrize('firstname, lastname, address, subway_station, phone, order_date, rental_period_locator, color_locator, comment', Constant.pers_data)
    def test_scooter_to_order(self, driver, firstname, lastname, address, subway_station, phone, order_date, rental_period_locator, color_locator, comment):
        order = OrderPage(driver=driver)
        order.go_to_site(Url.order_url)
        order.set_pers_data(firstname, lastname, address, subway_station, phone)
        order.click_then()
        order.set_rental_data(order_date, rental_period_locator, color_locator, comment)
        order.click_to_order()
        order.click_yes()
        assert 'Заказ оформлен' in order.get_order_status()