import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver import Keys

class OrderPage(BasePage):
    @allure.step("Заполнить Имя")
    def set_firstname(self, value):
        self.find_element_locator(OrderPageLocators.input_field_first_name).send_keys(value)

    @allure.step("Заполнить Фамилию")
    def set_lastname(self, value):
        self.find_element_locator(OrderPageLocators.input_field_last_name).send_keys(value)

    @allure.step("Заполнить Адрес")
    def set_address(self, value):
        self.find_element_locator(OrderPageLocators.input_field_address).send_keys(value)

    @allure.step("Заполнить станцию")
    def set_subway_station(self, value):
        station = self.find_element_locator(OrderPageLocators.input_field_subway_station)
        station.click()
        station.send_keys(value)
        self.find_element_located_click(OrderPageLocators.input_field_subway_station_item)

    @allure.step("Заполнить телефон")
    def set_phone(self, value):
        self.find_element_locator(OrderPageLocators.input_field_phone_number).send_keys(value)

    @allure.step("Заполнить блок персональных данных")
    def set_pers_data(self, firstname, lastname, address, subway_station, phone):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_address(address)
        self.set_subway_station(subway_station)
        self.set_phone(phone)

    @allure.step("Далее")
    def click_then(self):
        self.find_element_located_click(OrderPageLocators.button_then)

    @allure.step("Заполнить дату заказа")
    def set_order_date(self, value):
        order_date = self.find_element_locator(OrderPageLocators.input_field_date)
        order_date.send_keys(value)
        order_date.send_keys(Keys.ESCAPE)

    @allure.step("Заполнить количество дней")
    def set_rental_period(self, rental_period_locator):
        self.find_element_located_click(OrderPageLocators.input_field_rental_period)
        self.find_element_locator(OrderPageLocators.input_checkbox_rental_period)
        self.find_element_located_click(rental_period_locator)

    @allure.step("Заполнить цвет самоката")
    def set_color(self, color_locator):
        self.find_element_located_click(color_locator)

    @allure.step("Заполнить комментарий")
    def set_comment(self, value):
        self.find_element_locator(OrderPageLocators.input_field_comment).send_keys(value)

    @allure.step("Заполнить блок Про аренду")
    def set_rental_data(self, order_date, rental_period, color, comment):
        self.set_order_date(order_date)
        self.set_color(color)
        self.set_comment(comment)
        self.set_rental_period(rental_period)

    @allure.step("Заказать")
    def click_to_order(self):
        self.find_element_located_click(OrderPageLocators.button_to_order)

    @allure.step("ДА")
    def click_yes(self):
        self.find_element_located_click(OrderPageLocators.button_yes)

    @allure.step("Статус заказа")
    def click_show_order_status(self):
        self.find_element_located_click(OrderPageLocators.button_show_status)

    @allure.step("Статус заказа")
    def get_order_status(self):
        return self.find_element_locator(OrderPageLocators.order_status).text