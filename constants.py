from locators.head_page_locators import HeadPageLocators
from locators.order_page_locators import OrderPageLocators

class Constant:
    accordion_rows_params = [
        (HeadPageLocators.how_much_is_it, HeadPageLocators.it_is_400_in_day, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (HeadPageLocators.i_want_some_scooter, HeadPageLocators.one_order_one_scooter, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (HeadPageLocators.how_is_the_rental_time_calculated, HeadPageLocators.you_are_placing_an_order_for_may_8th, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (HeadPageLocators.can_i_order_scooter_right_for_today, HeadPageLocators.only_starting_tomorrow, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (HeadPageLocators.can_i_extend_the_order_or_return_the_scooter_earlier, HeadPageLocators.not_yet, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (HeadPageLocators.do_you_bring_the_charger_along_with_the_scooter, HeadPageLocators.you_will_not_need_to_charge, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (HeadPageLocators.can_i_cancel_the_order, HeadPageLocators.until_the_scooter_arrived, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (HeadPageLocators.i_live_behind_the_MKAD, HeadPageLocators.yes_absolutely, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]
    pers_data = [
        ('Петр', 'Петров', 'Москва', 'Войковская', '+79167654321', '11.01.2024', OrderPageLocators.rental_period_3, OrderPageLocators.color_black, '3-й подъезд'),
        ('Иван', 'Иванов', 'Москва', 'Маяковская', '+79031234567', '21.01.2024', OrderPageLocators.rental_period_2, OrderPageLocators.color_grey, 'ТОЦ "Рога и копыта"')
    ]