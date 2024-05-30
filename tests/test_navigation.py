import allure
from data import Urls
from pages.base_page import BasePage
from data import Urls

class TestNavigation:
    @allure.title('Проверка перехода при клике на лого Яндекс')
    @allure.description('При клике на лого Яндекс ожидаем переход на главную страницу dzen.ru')
    def test_click_on_yandex_opens_dzen_success(self, driver):
        dzen_page = BasePage(driver) 
        dzen_page.getUrl(Urls.base_url)
        dzen_page.check_yandex_logo_exists()
        dzen_page.click_yandex_logo()
        dzen_page.new_tab_switch()
        
        assert dzen_page.check_url_after_request(Urls.dzen_url)


    @allure.title('Проверка перехода при клике на лого Самокат')
    @allure.description('При клике на лого Самокат ожидаем переход на главную страницу Яндекс Самокат')        
    def test_click_on_scooter_opens_scooter_success(self, driver):
        scooter_page = BasePage(driver)
        scooter_page.getUrl(Urls.order_url)
        scooter_page.check_scooter_logo_exists()
        scooter_page.click_scooter_logo()

        assert scooter_page.check_url_after_request(Urls.base_url)
