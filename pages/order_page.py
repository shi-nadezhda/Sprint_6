import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Заполняем поле Имя')        
    def set_name(self, value):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(value)
    
    @allure.step('Заполняем поле Фамилия')      
    def set_surname(self, value):
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(value)

    @allure.step('Заполняем поле Адрес') 
    def set_adress(self, value):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(value)
    
    @allure.step('Заполняем поле Станция метро')              
    def set_metro(self, value):
        self.driver.find_element(*OrderPageLocators.metro_input).click()
        self.wait_visible_element_on_screen(OrderPageLocators.metro_input_dropdown)        
        self.driver.find_element(By.XPATH, f".//*[text()='{value}']").click()
    
    @allure.step('Заполняем поле Телефон')    
    def set_phone(self, value):
        self.driver.find_element(*OrderPageLocators.phone_input).send_keys(value)
    
    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()
    
    @allure.step('Заполняем поле Когда привезти самокат')    
    def set_date_input(self, value):
        self.driver.find_element(*OrderPageLocators.date_input).send_keys(value)
    
    @allure.step('Заполняем поле Срок аренды')      
    def set_rental_period(self, value):
        self.driver.find_element(*OrderPageLocators.rental_period).click()
        self.wait_visible_element_on_screen(OrderPageLocators.rental_period_dropdown)
        self.driver.find_element(By.XPATH, f".//*[text()='{value}']").click()
    
    @allure.step('Выбираем цвет самоката')      
    def set_color_selection(self, value):
        self.driver.find_element(By.ID, value).click()
    
    @allure.step('Заполняем поле Комментарий для курьера')      
    def set_comment_input(self, value):
        self.driver.find_element(*OrderPageLocators.comment_input).send_keys(value)
    
    @allure.step('Кликаем на кнопку "Заказать"')    
    def click_form_order_button(self):
        self.driver.find_element(*OrderPageLocators.form_order_button).click()
    
    @allure.step('Проверяем наличие окна "Хотите оформить заказ"')    
    def check_order_confirm_modal_header(self):
        self.driver.find_element(*OrderPageLocators.order_confirm_modal_header).is_displayed()
    
    @allure.step('Кликаем на кнопку "Да"')    
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()
    
    @allure.step('Проверяем наличие окна "Заказ оформлен"')
    def check_order_complete_modal_header(self):
        return self.driver.find_element(*OrderPageLocators.order_complete_modal_header).is_displayed()

    @allure.step('Заполняем форму заказа')    
    def order_process(self, user):
        # Ожидаем первый элемент формы
        self.wait_visible_element_on_screen(OrderPageLocators.name_input)
        # Заполняем форму
        self.set_name(user.name)
        self.set_surname(user.surname)
        self.set_adress(user.address)
        self.set_metro(user.metro)
        self.set_phone(user.phone)
        self.click_next_button()
        
        # Ожидаем загрузку второй страницы формы
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.date_input))
        self.wait_visible_element_on_screen(OrderPageLocators.date_input) 
        
        # Продолжаем заполнять форму
        self.set_date_input(user.date)
        self.set_rental_period(user.rental_day)
        self.set_color_selection(user.color_scooter)
        self.set_comment_input(user.comment)
        
        self.click_form_order_button()
        
        # Ожидаем окно подтверждения заказа
        self.wait_visible_element_on_screen(OrderPageLocators.order_confirm_modal_header)
        
        self.click_yes_button()
        
        # Ожидаем окно удачного заказа
        self.wait_visible_element_on_screen(OrderPageLocators.order_complete_modal_header)
