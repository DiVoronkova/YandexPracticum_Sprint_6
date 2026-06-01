import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    
    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step('Ожидать элемент по локатору: {locator}')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Нажать на элемент по локатору: {locator}')
    def click_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Прокрутить элемент по локатору: {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Заполнить поле по локатору: {locator}')
    def send_keys_to_field(self, locator, keys):
        field = self.wait_for_element(locator)
        return field.send_keys(keys)

    @allure.step('Получить текст по локатору: {locator}')
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключbnmcz на новую вкладку')
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step('Ожидаnm появления части url')
    def wait_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))
    
    
    
   