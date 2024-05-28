import allure
import pytest
from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import QuestionsAnswers

class TestMainPage:
    @allure.title('При клике на вопрос "{question}" открывается ответ "{answer}"')
    @allure.description('Проверка соответствия вопросов ответам')
    @pytest.mark.parametrize('question, answer', QuestionsAnswers.qa_dict)
    def test_question_answer(self, driver, question, answer):
        answers_page = MainPage(driver)
        answers_page.getUrl(Urls.base_url)
        
        question_locator = MainPageLocators.text_locator(question)
        answer_locator = MainPageLocators.text_locator(answer)
        
        answers_page.scroll_to_element(question_locator)
        answers_page.check_question_exists(question_locator)
        answers_page.click_question(question_locator) 
        
        assert answers_page.check_answer_exists(answer_locator)
