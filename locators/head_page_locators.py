from selenium.webdriver.common.by import By

class HeadPageLocators:
    # Локаторы "аккордеону"
    # Локатор к 1-ой стрелке "аккордеона" - Сколько это стоит? И как оплатить?
    how_much_is_it = (By.ID, 'accordion__heading-0')
    it_is_400_in_day = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    # Локатор ко 2-ой стрелке "аккордеона" - Хочу сразу несколько самокатов! Так можно?
    i_want_some_scooter = (By.ID, 'accordion__heading-1')
    one_order_one_scooter = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    # Локатор к 3-ой стрелке "аккордеона" - Как рассчитывается время аренды?
    how_is_the_rental_time_calculated = (By.ID, 'accordion__heading-2')
    you_are_placing_an_order_for_may_8th = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    # Локатор к 4-ой стрелке "аккордеона" - Можно ли заказать самокат прямо на сегодня? Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    can_i_order_scooter_right_for_today = (By.ID, 'accordion__heading-3')
    only_starting_tomorrow = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    # Локатор к 5-ой стрелке "аккордеона" - Можно ли продлить заказ или вернуть самокат раньше? Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    can_i_extend_the_order_or_return_the_scooter_earlier = (By.ID, 'accordion__heading-4')
    not_yet = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    # Локатор к 6-ой стрелке "аккордеона" - Вы привозите зарядку вместе с самокатом? Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.
    do_you_bring_the_charger_along_with_the_scooter = (By.ID, 'accordion__heading-5')
    you_will_not_need_to_charge = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    # Локатор к 7-ой стрелке "аккордеона" - Можно ли отменить заказ? Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
    can_i_cancel_the_order = (By.ID, 'accordion__heading-6')
    until_the_scooter_arrived = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    # Локатор к 8-ей стрелке "аккордеона" - Я жизу за МКАДом, привезёте?
    i_live_behind_the_MKAD = (By.ID, 'accordion__heading-7')
    yes_absolutely = (By.XPATH, "//div[@id='accordion__panel-7']/p")

    # Локаторы логотипов
    # Локатор логотипа Яндекса
    yandex_logo = (By.XPATH, "//img[@src='/assets/ya.svg']")
    # Локатор логотипа Самоката
    scooter_logo = (By.XPATH, "//img[@src='/assets/scooter.svg']")

    # Локаторы кнопок Заказать
    # Локатор верхней кнопки Заказать
    to_order_button_up = (By.XPATH, "div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']")
    # Локатор нижней кнопки Заказать
    to_order_button_down = (By.XPATH, "div[@class='Home_FinishButton__1_cWm']/button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
