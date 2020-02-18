from Source.Framework.seleniumFrm import *
from Source.Test.Python.DNVGL.Test.basetest import login


class TestClass:

    @allure.epic('EPIC DNV TEST')
    @allure.description('REMOVE SERVICE TEST')
    @allure.feature('FEATURE SERVICES')
    @allure.story('STORY 3 (REMOVE SERVICE)')
    def test(self):
        try:
            logged_home_page = login(Selenium.driver)
            service_page = logged_home_page.click_services_button()
            service_page.remove_service()
            check(service_page.is_void_service_image_appears(), Selenium.driver)

        finally:
            Selenium.close()

