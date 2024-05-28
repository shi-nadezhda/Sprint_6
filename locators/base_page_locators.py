from selenium.webdriver.common.by import By

class BasePageLocators:
    """Шапка страницы"""
    header_xpath = ".//div[contains(@class, 'Header_Header')]"
    logo_yandex_link = [By.XPATH, header_xpath + "//img[@alt='Yandex']/parent::a"] # ссылка лого Яндекс
    logo_scooter_link = [By.XPATH, header_xpath + "//img[@alt='Scooter']/parent::a"] # ссылка лого Самокат
    header_order_button = [By.XPATH, header_xpath + "//button[text()='Заказать']"] # кнопка "Заказать" в шапке страницы
    order_status_button = [By.XPATH, header_xpath + "//button[text()='Статус заказа']"] # кнопка "Статус заказа"
    
    """Куки"""
    cookies_acept_button = [By.XPATH, ".//button[text()='да все привыкли']"] # кнопка "Да все привыкли"
