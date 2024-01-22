from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_locator(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Element not found in {locator}')

    def find_element_located_click(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Element not found in {locator}').click()

    def find_element_locator_with_scroll(self, locator, time=3):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element), message=f'Element not found in {locator}')

    def find_element_located_with_scroll_click(self, locator, time=3):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element), message=f'Element not found in {locator}').click()

    def get_current_page(self):
        return self.driver.current_url

    def wait_for_dzen(self):
        return WebDriverWait(self.driver, 3).until(EC.url_contains('https://dzen.ru/'))
