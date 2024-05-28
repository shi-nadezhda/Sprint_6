import allure
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим вниз до нужного элемента')
    def scroll_to_element(self, locator):     
        element = self.wait_visible_element_on_screen(locator)
        self.wait_visible_element_on_screen(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Ожидаем появление элемента на экране')    
    def wait_visible_element_on_screen(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return (wait.until(expected_conditions.visibility_of_element_located(locator)) and 
                wait.until(expected_conditions.element_to_be_clickable(locator)))
    
    @allure.step('Переходим по {url} и ожидаем завершения перехода')
    def getUrl(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))
        self.driver.find_element(*BasePageLocators.cookies_acept_button).click()
    
    @allure.step('Переключаемся на вторую вкладку')
    def new_tab_switch(self):
        second_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(second_tab)
    
    @allure.step('Проверяем наличие логотипа Яндекс') 
    def check_yandex_logo_exists(self):
        return self.driver.find_element(*BasePageLocators.logo_yandex_link).is_displayed()
    
    @allure.step('Кликаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.logo_yandex_link).click()
    
    @allure.step('Проверяем наличие логотипа Самокат')
    def check_scooter_logo_exists(self):
        return self.driver.find_element(*BasePageLocators.logo_scooter_link).is_displayed()
    
    @allure.step('Кликаем на логотип Самокат')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.logo_scooter_link).click()
    
    @allure.step('Проверяем наличие кнопки "Заказать" в шапке')
    def check_order_button_exists(self):
        return self.driver.find_element(*BasePageLocators.header_order_button).is_displayed()
    
    @allure.step('Кликаем по кнопке "Заказать" в шапке')
    def click_order_button(self):
        self.wait_visible_element_on_screen(BasePageLocators.header_order_button)
        self.driver.find_element(*BasePageLocators.header_order_button).click() 
        
    @allure.step('Проверяем, что адрес соответствует {url}')
    def check_url_after_request(self, url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_contains(url))
        
        return url in self.driver.current_url
