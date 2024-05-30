# Тесты для сайта Яндекс Самокат.
https://qa-scooter.praktikum-services.ru/

## Структура
- tests/ - автотесты
    - test_main_page.py - тесты для проверки соответствия вопросов ответам
    - test_navigation.py - тесты для проверки переходов по страницам
    - test_order.py - тесты заказа самоката
- conftest.py - фикстуры
- locators/ - локаторы
- user.py - пользователи для заказа
- pages/ - POM
- data.py - файл с данными

### Запуск тестов: 
`pytest -v --alluredir=allure_results`

### Просмотр отчета
`allure serve allure_results`
