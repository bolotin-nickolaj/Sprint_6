from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы полей ввода 1-ой группы
    input_field_first_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_field_last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_field_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_field_subway_station = (By.XPATH, "//input[@placeholder='* Станция метро']")
    input_field_subway_station_item = (By.XPATH, "//div[@class='select-search__select']/ul/li[1]")
    input_field_phone_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Локатор кнопки Далее
    button_then = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для полей ввода 2-ой группы
    input_field_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    input_field_rental_period = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    input_checkbox_rental_period = (By.XPATH, "//div[@class='Dropdown-menu']")
    input_field_color_black = (By.XPATH, "//input[@id='black']")
    input_field_color_gray = (By.XPATH, "//input[@id='gray']")
    input_field_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Локатор для кнопки Заказать
    button_to_order = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Локатор для кнопки ДА
    button_yes = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div[@class='Order_Buttons__1xGrp']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Локатор для текста Статус
    order_status = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    button_show_status = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div[@class='Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Локаторы значений срока аренды
    rental_period_1 = (By.XPATH, "//div[text()='сутки']")
    rental_period_2 = (By.XPATH, "//div[text()='двое суток']")
    rental_period_3 = (By.XPATH, "//div[text()='трое суток']")
    rental_period_4 = (By.XPATH, "//div[text()='четверо суток']")
    rental_period_5 = (By.XPATH, "//div[text()='пятеро суток']")
    rental_period_6 = (By.XPATH, "//div[text()='шестеро суток']")

    # Локаторы значений цвета самоката
    color_black = (By.ID, "black")
    color_grey = (By.ID, "grey")
