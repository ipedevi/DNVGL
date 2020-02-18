import allure
from Source.Framework.BasePage import BasePage
import time

""" Path to the objects """
add_first_services_button = "//article/a/img[contains(@src, 'DPCap.jpg')]"
add_service_button = "//a[contains(@ng-click, 'AddClick')]"
service_added = "//h3[contains(text(), 'DP Capability')]"


class DNVAddServicesPage(BasePage):
    """Page Object of DNV Logged Home Page"""

    def wait_until_loaded(self):
        """ wait until login icon is loaded """
        time.sleep(3)
        self.driver.find_element_by_xpath(add_first_services_button)

    @allure.step("Add DP Capability Assessment service.")
    def add_first_service(self):
        """ Add first Service """
        self.driver.find_element_by_xpath(add_first_services_button).click()
        ''' TODO: Need to be changed by other type of wait'''
        time.sleep(3)
        self.driver.find_element_by_xpath(add_service_button).click()
        ''' TODO: Need to be changed by other type of wait'''
        time.sleep(3)

    @allure.step("Check if service is added")
    def is_service_added(self):
        """ Check if service is added """
        return self.driver.find_element_by_xpath(service_added).is_displayed()