from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"] # кнопка "Заказать" внизу страницы
    text_locator = lambda text: [By.XPATH, f".//*[text()='{text}']"]
