import allure
from locators.order_locators import OrderLocators
import pytest


class TestOrderPage:

    @allure.title('Проверка, что появилось всплывающее окно с сообщением об успешном создании заказа при нажатии на кнопки Заказать в разных частях страницы')
    @pytest.mark.parametrize("BUTTON_ORDER, STATION, DURATION, COLOUR_LOCATOR", [
        (OrderLocators.HEADER_ORDER_BUTTON, 'Черкизовская', OrderLocators.DURATION_TWO_DAYS, OrderLocators.BLACK_SCOOTER_CHECKBOX),
        (OrderLocators.HEADER_ORDER_BUTTON, 'Сокол', OrderLocators.DURATION_THREE_DAYS, OrderLocators.GREY_SCOOTER_CHECKBOX)
        ])
    def test_order_scooter(self, order_page, BUTTON_ORDER, STATION, DURATION, COLOUR_LOCATOR):
        order_page.push_order_button(BUTTON_ORDER)
        order_page.order_scooter(STATION, DURATION, COLOUR_LOCATOR)
        popup_text = order_page.get_text_from_element(OrderLocators.ORDER_CONFIRMED_POPUP)
        assert order_page.popup_is_displayed()
        assert "Заказ оформлен" in popup_text
        