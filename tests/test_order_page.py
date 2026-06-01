import allure
from locators.order_locators import Order_Locators
import pytest


class TestOrderPage:
    @allure.title('Проверка, что появилось всплывающее окно с сообщением об успешном создании заказа при нажатии на кнопки Заказать в разных частях страницы')
    @pytest.mark.parametrize("BUTTON_ORDER, COLOUR_LOCATOR", [
        (Order_Locators.HEADER_ORDER_BUTTON, Order_Locators.BLACK_SCOOTER_CHECKBOX),
        (Order_Locators.HEADER_ORDER_BUTTON, Order_Locators.GREY_SCOOTER_CHECKBOX)
        ])
    def test_order_scooter(self, order_page, BUTTON_ORDER, COLOUR_LOCATOR):
        order_page.accept_cookies()
        order_page.push_order_button(BUTTON_ORDER)
        order_page.order_scooter(COLOUR_LOCATOR)
        popup_text = order_page.get_text_from_element(Order_Locators.ORDER_CONFIRMED_POPUP)
        assert "Заказ оформлен" in popup_text
        



