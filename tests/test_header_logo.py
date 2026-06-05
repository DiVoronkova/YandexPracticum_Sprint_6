import allure
from url import MAIN_URL


class TestLogo:
    
    @allure.title('Проверка, что при нажатии на логотип Самокат, происходит переход на главную страницу Самоката')
    def test_if_click_scooter_logo_main_page_opens(self, logo_page):
        logo_page.click_order_button()
        logo_page.click_scooter_logo()
        assert logo_page.check_opened_page() == f"{MAIN_URL}/"

    @allure.title('Проверка, что при нажатии на логотип Яндекс, происходит переход на главную страница Дзена')
    def test_if_click_yandex_logo_dzen_page_opens(self, logo_page):
        logo_page.click_yandex_logo()
        logo_page.switch_to_next_tab()
        logo_page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in logo_page.check_opened_page()
