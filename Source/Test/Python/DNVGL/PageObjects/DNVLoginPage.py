import allure
from Source.Framework.BasePage import BasePage
from Source.Test.Python.DNVGL.PageObjects.DNVHomeLoggedPage import DNVHomeLoggedPage


""" Path to the objects """
login_icon_xpath = "//*[@id=\"header\"]/img"
user_xpath = "//*[@id=\"userNameInput\"]"
psw_xpath = "//*[@id=\"passwordInput\"]"
submit_button_xpath = "//*[@id=\"submitButton\"]"


class DNVLoginPage(BasePage):
    """Page Object of DNV Login Page"""

    def wait_until_loaded(self):
        """ wait until login icon is loaded """
        self.driver.find_element_by_xpath(login_icon_xpath)

    @allure.step ("Checking if logging page is loaded.")
    def is_login_page_is_loaded(self):
        """ return true is login page is loaded """
        return self.driver.find_element_by_xpath(login_icon_xpath).is_displayed()

    @allure.step("Login user: $1")
    def login(self, usr, psw):
        """ Log the user and return next page"""
        self.driver.find_element_by_xpath(user_xpath).send_keys(usr)
        self.driver.find_element_by_xpath(psw_xpath).send_keys(psw)
        self.driver.find_element_by_xpath(submit_button_xpath).click()

        home_logged_page = DNVHomeLoggedPage(self.driver)
        home_logged_page.wait_until_loaded()
        return home_logged_page
