# Sprint_6
## Тестирование функционала сервиса "Яндекс.Самокат"

Сервис "Яндекс.Самокат" это сервис для заказа самокатов заказчику.

Адрес сервиса: https://qa-scooter.praktikum-services.ru/

Описание реализованных для проверки сервиса тестов:

| Наименование файла | Название теста             | Описание теста                                                                                         |
|-------------------:|:---------------------------|:-------------------------------------------------------------------------------------------------------|
|  test_head_page.py | TestAccordion | Тестирует выпадающий список в разделе "Вопросы о важном": При нажатии на стрелочку, открывается текст. |
|test_logo_click.py| test_yandex_logo | Тестирование нажатия на логотип Яндекса. Должна открыться страница Яндекс.Дзен                         |
| test_logo_click.py| test_scooter_logo| Тестирование нажатия на логотип Самоката. Должна открыться главная страница сервиса.                   |
| test_order_page.py| test_scooter_to_order | Тест проверяет заполнение данных пользователем и успешное оформление заказа.                           |