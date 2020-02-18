from Source.Framework.seleniumFrm import *
from Source.Test.Python.DNVGL.Test.basetest import go_login_page
from Source.Framework import myconfig


class TestClass:

    @allure.epic('EPIC DNV TEST')
    @allure.description('LOGIN TEST')
    @allure.feature('FEATURE LOGIN')
    @allure.story('STORY 1 (LOGIN)')
    def test(self):
        try:
            login_page = go_login_page(Selenium.driver)
            home_logged_page = login_page.login(myconfig.default_email, myconfig.default_psw)
            check(home_logged_page.is_user_logged(), Selenium.driver)

        finally:
            Selenium.close()
