from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.questions_page import QuestionsPage
from pages.order_page import OrderPage
from pages.header_logo_page import LogoPage
from locators.order_locators import Order_Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def questions_page(driver):
    questions_page = QuestionsPage(driver)
    questions_page.open()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Order_Locators.HEADER_ORDER_BUTTON))
    return questions_page

@pytest.fixture
def order_page(driver):
    o_page = OrderPage(driver)
    o_page.open()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Order_Locators.HEADER_ORDER_BUTTON))
    return o_page

@pytest.fixture
def logo_page(driver):
    logo_page = LogoPage(driver)
    logo_page.open()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Order_Locators.HEADER_ORDER_BUTTON))
    return logo_page

@pytest.fixture
def random_credentials():
    return generate_random_credentials()
