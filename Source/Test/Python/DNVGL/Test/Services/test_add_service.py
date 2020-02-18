from Source.Framework.seleniumFrm import *
from Source.Test.Python.DNVGL.Test.basetest import login


class TestClass:

    @allure.epic('EPIC DNV TEST')
    @allure.description('ADD SERVICE TEST')
    @allure.feature('FEATURE SERVICES')
    @allure.story('STORY 2 (ADD SERVICE)')
    def test(self):
        try:
            logged_home_page = login(Selenium.driver)
            service_page = logged_home_page.click_services_button()
            add_service_page = service_page.click_add_service()
            add_service_page.add_first_service()
            check(add_service_page.is_service_added(), Selenium.driver)

        finally:
            Selenium.close()
