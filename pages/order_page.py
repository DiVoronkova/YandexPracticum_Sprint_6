import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from url import MAIN_URL
from locators.order_locators import Order_Locators
from helpers import generate_random_credentials

class OrderPage(BasePage):
        
    URL = MAIN_URL

    @allure.step('Принять cookie')
    def accept_cookies(self):
        if self.driver.find_element(*Order_Locators.COOKIE_BUTTON):
            self.driver.find_element(*Order_Locators.COOKIE_BUTTON).click()

    @allure.step('Проверить текущий URL')
    def check_open_page(self):
        return self.get_current_url()
    
    @allure.step('Нажать на кнопку Заказать')
    def push_order_button(self, locator_order_button):
        if locator_order_button == Order_Locators.FOOTER_ORDER_BUTTON:
            self.scroll_to_element(locator_order_button)
        self.click_element(locator_order_button)

    @allure.step('Заполнить поле Имя')
    def send_keys_to_name_field(self, name):
        self.send_keys_to_field(Order_Locators.NAME_FIELD, name)

    @allure.step('Заполнение поле Фамилия')
    def send_keys_to_surname_field(self, surname):
        self.send_keys_to_field(Order_Locators.SURNAME_FIELD, surname)

    @allure.step('Заполненить поле Адрес')
    def send_keys_to_address_field(self, address):
        self.send_keys_to_field(Order_Locators.ADDRESS_FIELD, address)


    @allure.step('Заполненить поле Станция метро')
    def send_keys_to_station_field(self, station):
        self.click_element(Order_Locators.STATION__FIELD)
        self.send_keys_to_field(Order_Locators.STATION__FIELD, station)
        self.click_element(Order_Locators.METRO_STATION)


    @allure.step('Заполненить поле Номер телефона')
    def send_keys_to_phone_field(self, phone):
        self.send_keys_to_field(Order_Locators.PHONE_FIELD, phone)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        self.click_element(Order_Locators.NEXT_BUTTON)

    @allure.step('Заполнить данные на странице Для кого самокат и нажать на кнопку далее')
    def fill_in_the_users_details(self, name, surname, address, station, phone):
        self.send_keys_to_name_field(name)
        self.send_keys_to_surname_field(surname)
        self.send_keys_to_address_field(address)
        self.send_keys_to_station_field(station)
        self.send_keys_to_phone_field(phone)
        self.click_next_button()

    @allure.step('Заполненить поле Когда привезти заказ')
    def send_keys_to_deliver_order_field(self, date):
        date_field = self.wait_for_element(Order_Locators.DATE_FIELD)
        date_field.click()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    @allure.step('Заполненить поле Срок аренды')
    def choose_rental_period(self):
        self.click_element(Order_Locators.DURATION_FIELD)
        self.click_element(Order_Locators.DURATION_THREE_DAYS)

    @allure.step('Выбрать цвет самоката')
    def choose__scooter_colour(self, colour_scooter):
        self.click_element(colour_scooter)

    @allure.step('Заполнить поле Комментарий')
    def send_keys_to_comment_field(self, comment):
        self.send_keys_to_field(Order_Locators.COMMENT_FIELD, comment)

    @allure.step('Нажать на кнопку Заказать')
    def click_order_button(self):
        self.click_element(Order_Locators.ORDER_BUTTON)

    @allure.step('Заполненить данные формы Про аренду и нажать кнопку Заказать')
    def fill_in_rental_details(self, date, colour_scooter, comment=""):
        self.send_keys_to_deliver_order_field(date)
        self.choose_rental_period()
        self.choose__scooter_colour(colour_scooter)
        self.send_keys_to_comment_field(comment)
        self.click_order_button()

    @allure.step('Нажать на кнопку Да')
    def click_yes_button(self):
        self.click_element(Order_Locators.YES_BUTTON)

    @allure.step('Заполненить форму заказа и нажать да')
    def order_scooter(self, colour_scooter):
        name, surname, address, station, phone, date, comment = generate_random_credentials()
        self.fill_in_the_users_details(name, surname, address, station, phone)
        self.wait_for_element(Order_Locators.DATE_FIELD)
        self.fill_in_rental_details(date, colour_scooter, comment)
        self.wait_for_element(Order_Locators.YES_BUTTON)
        self.click_yes_button()
        return self.wait_for_element(Order_Locators.ORDER_CONFIRMED_POPUP).is_displayed() 
    

