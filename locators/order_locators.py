from selenium.webdriver.common.by import By


class OrderLocators:

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    FOOTER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    STATION_DROPDOWN_LIST = (By.XPATH, ".//div[@class='select-search__select']")
    NAME_FIELD = (By.XPATH,'//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH,'//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH,'//input[@placeholder="* Адрес: куда привезти заказ"]')
    STATION__FIELD = (By.XPATH,'//input[@placeholder="* Станция метро"]')

    PHONE_FIELD = (By.XPATH,'//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH,'//button[text()="Далее"]')

    DATE_FIELD = (By.XPATH,'//input[@placeholder="* Когда привезти самокат"]')
    DURATION_FIELD = (By.XPATH,'//div[text()="* Срок аренды"]')
    DURATION_TWO_DAYS = (By.XPATH, "//div[text() = 'двое суток']")
    DURATION_THREE_DAYS = (By.XPATH, "//div[text() = 'трое суток']")
    BLACK_SCOOTER_CHECKBOX = (By.ID, "black")
    GREY_SCOOTER_CHECKBOX = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH,'//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]')
    
    CONFIRM_ORDER_POPUP_TITLE = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_CONFIRMED_POPUP = (By.XPATH, '//div[text()="Заказ оформлен"]')
