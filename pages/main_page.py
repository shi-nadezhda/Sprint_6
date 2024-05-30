import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_finish_order_button(self):
        self.scroll_to_element(MainPageLocators.order_button)
        self.wait_visible_element_on_screen(MainPageLocators.order_button)
        self.driver.find_element(*MainPageLocators.order_button).click()
    
    @allure.step('Проверяем наличие вопроса')
    def check_question_exists(self, question_locator):
        self.wait_visible_element_on_screen(question_locator)
        return self.driver.find_element(*question_locator).is_displayed()
    
    @allure.step('Кликаем по вопросу')
    def click_question(self, question_locator):
        self.driver.find_element(*question_locator).click()
    
    @allure.step('Проверяем наличие ответа')
    def check_answer_exists(self, answer_locator):
        return self.driver.find_element(*answer_locator).is_displayed()
