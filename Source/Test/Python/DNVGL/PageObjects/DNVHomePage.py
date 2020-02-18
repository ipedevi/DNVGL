import allure
from Source.Framework.BasePage import BasePage
from Source.Test.Python.DNVGL.PageObjects.DNVLoginPage import DNVLoginPage


""" Path to the objects """
login_button_xpath = "//*[@id=\"dnvgl\"]/header/section/a"


class DNVHomePage(BasePage):
    """Page Object of DNV Home Page"""

    @allure.step
    def initiate(self, url):
        """ Initiate page object """
        self.driver.get(url)

    @allure.step
    def click_login_button(self):
        """ click on login button and return next page """
        element = self.driver.find_element_by_xpath(login_button_xpath)
        element.click()
        login_page = DNVLoginPage(self.driver)
        login_page.wait_until_loaded()
        return login_page
