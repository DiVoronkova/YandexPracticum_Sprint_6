import pytest
import allure
from locators.question_locators import QuestionLocators
from data import ExpectedAnswers


class TestQuestions:

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном на соответствие вопросов с ответами')
    @pytest.mark.parametrize('question, answer, expected_answer', zip(QuestionLocators.QUESTIONS, QuestionLocators.ANSWERS, ExpectedAnswers.expected_answers))
    def test_questions_page(self, questions_page, question, answer, expected_answer):
        text_result = questions_page.get_answer(question, answer)
        assert text_result == expected_answer
