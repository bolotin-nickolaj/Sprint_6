import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service(executable_path="/snap/bin/geckodriver")
    driver = webdriver.Firefox(service=service)
#    driver = webdriver.Chrome() # Для хрома
    yield driver
    driver.quit()


