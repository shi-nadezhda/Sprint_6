from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Форма заказа - Для кого самокат"""
    name_input = [By.XPATH, ".//input[contains(@placeholder, 'Имя')]"] # поле ввода имени
    surname_input = [By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]"] # поле ввода фамилии
    address_input = [By.XPATH, ".//input[contains(@placeholder, 'Адрес: куда привезти заказ')]"] # поле ввода адреса
    metro_input = [By.XPATH, ".//input[contains(@placeholder, 'Станция метро')]"] # поле ввода станции метро
    metro_input_dropdown = [By.CLASS_NAME, "select-search__select"] # вывод списка станций метро
    phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон: на него позвонит курьер')]"] # поле ввода номера телефона
    next_button = [By.XPATH, ".//button[text()='Далее']"] # кнопка "Далее"
    
    """Форма заказа - Про аренду"""
    date_input = [By.XPATH, ".//input[contains(@placeholder, 'Когда привезти самокат')]"] # поле ввода даты доставки
    
    # срок аренды
    rental_period = [By.XPATH, ".//div[contains(text(), 'Срок аренды')]/parent::div[contains(@class, 'Dropdown-control')]//*[@class='Dropdown-arrow']"] # поле срок аренды
    rental_period_dropdown = [By.CLASS_NAME, "Dropdown-menu"] # выводим список срока аренды
    
    comment_input = [By.XPATH, ".//input[contains(@placeholder, 'Комментарий для курьера')]"] # поле ввода комментария для курьера
    back_button = [By.XPATH, ".//button[text()='Назад']"] # кнопка "Назад"
    form_order_button = [By.XPATH, ".//div[contains(@class, 'Order_Content')]//button[text()='Заказать']"] # кнопка "Заказать"
    
    """Окно подтверждения заказа"""
    order_modal_xpath = ".//div[contains(@class, 'Order_Modal')]"
    order_confirm_modal_header = [By.XPATH, order_modal_xpath + "//*[text()='Хотите оформить заказ?']"] # окно "Хотите оформить заказ?"
    no_button = [By.XPATH, order_modal_xpath + "//button[text()='Нет']"] # кнопка "Нет"
    yes_button = [By.XPATH, order_modal_xpath + "//button[text()='Да']"] # кнопка "Да"
    order_complete_modal_header = [By.XPATH, order_modal_xpath + "//*[text()='Заказ оформлен']"] # окно "Заказ оформлен"
    status_button = [By.XPATH, order_modal_xpath + "//button[text()='Посмотреть статус']"] # кнопка "Посмотреть статус"
