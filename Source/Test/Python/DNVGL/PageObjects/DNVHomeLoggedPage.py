import allure
from Source.Framework.BasePage import BasePage
from Source.Test.Python.DNVGL.PageObjects.DNVServicesPage import DNVServicesPage
import time


""" Path to the objects """
header_xpath = "//header[contains(@class, 'vui-header')]"
logged_button_xpath = "//*[@id=\"app\"]//button/div[contains(text(), \"t\")]"
services_button_xpath = "//*[@id=\"app\"]//li[2]//a[contains(@class, \"_item_0fd02\")]"


class DNVHomeLoggedPage(BasePage):
    """Page Object of DNV Logged Home Page"""

    def wait_until_loaded(self):
        """ wait until login icon is loaded """
        time.sleep(3)
        self.driver.find_element_by_xpath(header_xpath)

    @allure.step ("Check if user is logged.")
    def is_user_logged(self):
        """ return true is user is logged """
        return self.driver.find_element_by_xpath(header_xpath).is_displayed()

    @allure.step("Click on services home page button.")
    def click_services_button(self):
        """ go to services page and return page"""
        self.driver.find_element_by_xpath(services_button_xpath).click()
        service_page = DNVServicesPage(self.driver)
        service_page.wait_until_loaded()
        return service_page
