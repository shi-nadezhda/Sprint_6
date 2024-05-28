import allure
from data import Urls
from pages.order_page import OrderPage
from pages.main_page import MainPage
from user import User_1, User_2

class TestOrder:
    @allure.title('Успешное оформление заказа через кнопку в шапке')
    @allure.description('Проверяем оформление заказа через кнопку "Заказать" в шапке страницы')    
    def test_order_from_the_button_header(self, driver):
        orderPage = OrderPage(driver)                
        orderPage.getUrl(Urls.base_url)
        orderPage.click_order_button()
        orderPage.order_process(User_1)
        
        assert orderPage.check_order_complete_modal_header()
    
    
    @allure.title('Успешное оформление заказа через кнопку внизу страницы')
    @allure.description('Проверяем оформление заказа через кнопку "Заказать" внизу страницы')     
    def test_order_from_button_finish(self, driver):
        main_page = MainPage(driver)        
        main_page.getUrl(Urls.base_url)
        main_page.click_finish_order_button()        
        orderPage = OrderPage(driver)
        orderPage.order_process(User_2)
        
        assert orderPage.check_order_complete_modal_header()
