import allure
from pages.base_page import BasePage
from url import MAIN_URL
from locators.question_locators import Question_Locators


class QuestionsPage(BasePage):

    URL = MAIN_URL

    @allure.step('Прокрутить до заголовка Вопросы о важном')
    def scroll_to_questions(self):
        self.scroll_to_element(Question_Locators.QUESTIONS_TITLE)

    @allure.step('Нажать на вопрос')
    def click_question(self, question):
        self.click_element(question)

    @allure.step('Получить ответ на вопрос')
    def get_answer(self, question, answer):
        self.scroll_to_questions()
        self.click_question (question)
        answer_text = self.get_text_from_element(answer)
        return answer_text  


        






