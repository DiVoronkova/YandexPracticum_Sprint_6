import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from url import MAIN_URL
from locators.order_locators import OrderLocators
from helpers import generate_random_credentials


class OrderPage(BasePage):
        
    URL = MAIN_URL
    
    @allure.step('Нажать на кнопку Заказать')
    def push_order_button(self, locator_order_button):
        if locator_order_button == OrderLocators.FOOTER_ORDER_BUTTON:
            self.scroll_to_element(locator_order_button)
        self.click_element(locator_order_button)

    @allure.step('Заполнить поле Имя')
    def send_keys_to_name_field(self, name):
        self.send_keys_to_field(OrderLocators.NAME_FIELD, name)

    @allure.step('Заполнить поле Фамилия')
    def send_keys_to_surname_field(self, surname):
        self.send_keys_to_field(OrderLocators.SURNAME_FIELD, surname)

    @allure.step('Заполнить поле Адрес')
    def send_keys_to_address_field(self, address):
        self.send_keys_to_field(OrderLocators.ADDRESS_FIELD, address)

    @allure.step('Заполнить поле Станция метро')
    def send_keys_to_station_field(self, station):
        self.click_element(OrderLocators.STATION__FIELD)
        self.send_keys_to_field(OrderLocators.STATION__FIELD, station)
        self.wait_for_element(OrderLocators.STATION_DROPDOWN_LIST)
        # Нажатие стрелки вниз (выбор первого элемента в списке)
        self.send_keys_to_field(OrderLocators.STATION__FIELD, Keys.DOWN)
        # Нажатие Enter для подтверждения выбора
        self.send_keys_to_field(OrderLocators.STATION__FIELD, Keys.ENTER)

    @allure.step('Заполнить поле Номер телефона')
    def send_keys_to_phone_field(self, phone):
        self.send_keys_to_field(OrderLocators.PHONE_FIELD, phone)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные на странице Для кого самокат и нажать на кнопку Далее')
    def fill_in_the_users_details(self, name, surname, address, station, phone):
        self.send_keys_to_name_field(name)
        self.send_keys_to_surname_field(surname)
        self.send_keys_to_address_field(address)
        self.send_keys_to_station_field(station)
        self.send_keys_to_phone_field(phone)
        self.click_next_button()

    @allure.step('Заполнить поле Когда привезти заказ')
    def send_keys_to_deliver_order_field(self, date):
        date_field = self.wait_for_element(OrderLocators.DATE_FIELD)
        date_field.click()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    @allure.step('Заполнить поле Срок аренды')
    def choose_rental_period(self, duration):
        self.click_element(OrderLocators.DURATION_FIELD)
        self.click_element(duration)

    @allure.step('Выбрать цвет самоката')
    def choose__scooter_colour(self, colour_scooter):
        self.click_element(colour_scooter)

    @allure.step('Заполнить поле Комментарий')
    def send_keys_to_comment_field(self, comment):
        self.send_keys_to_field(OrderLocators.COMMENT_FIELD, comment)

    @allure.step('Нажать на кнопку Заказать')
    def click_order_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON)

    @allure.step('Заполнить данные формы Про аренду и нажать кнопку Заказать')
    def fill_in_rental_details(self, date, duration, colour_scooter, comment=""):
        self.send_keys_to_deliver_order_field(date)
        self.choose_rental_period(duration)
        self.choose__scooter_colour(colour_scooter)
        self.send_keys_to_comment_field(comment)
        self.click_order_button()

    @allure.step('Нажать на кнопку Да')
    def click_yes_button(self):
        self.click_element(OrderLocators.YES_BUTTON)

    @allure.step('Заполнить форму заказа и нажать Да')
    def order_scooter(self, station, duration, colour_scooter):
        name, surname, address, phone, date, comment = generate_random_credentials()
        self.fill_in_the_users_details(name, surname, address, station, phone)
        self.wait_for_element(OrderLocators.DATE_FIELD)
        self.fill_in_rental_details(date, duration, colour_scooter, comment)
        self.wait_for_element(OrderLocators.YES_BUTTON)
        self.click_yes_button()

    @allure.step("Проверить отображение Popup")
    def popup_is_displayed(self):
        return self.is_element_displayed(OrderLocators.ORDER_CONFIRMED_POPUP)