import allure
from pages.head_page import HeadPage
from urls import Url
from locators.head_page_locators import HeadPageLocators


class TestLogoClick:
    @allure.story("Главная страница")
    @allure.feature("Тестирование нажатия на логотип Самоката")
    def test_scooter_logo(self, driver):
        hp = HeadPage(driver)
        hp.go_to_site(Url.base_url)
        hp.find_element_located_with_scroll_click(locator=HeadPageLocators.scooter_logo)
        assert hp.get_current_page() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.feature("Тестирование нажатия на логотип Яндекса")
    def test_yandex_logo(self, driver):
        hp = HeadPage(driver)
        hp.go_to_site(Url.base_url)
        hp.find_element_located_with_scroll_click(locator=HeadPageLocators.yandex_logo)
        driver.switch_to.window(driver.window_handles[1])
        hp.wait_for_dzen()
        assert 'https://dzen.ru/' in hp.get_current_page()
