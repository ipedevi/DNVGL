import allure
import time
from Source.Framework.BasePage import BasePage
from Source.Test.Python.DNVGL.PageObjects.DNVAddServicesPage import DNVAddServicesPage


""" Path to the objects """
service_image = "//img[contains(@src, '/content/images/dashboard-pictogram.png')]"
add_services_button = "//button[contains(@ng-click, 'addService')]"
customization_button = "id('customizebtn')"
remove_button = "//a[contains(@ng-click, 'remove')]"
finalization_button = "id('donebtn')"


class DNVServicesPage(BasePage):
    """Page Object of DNV Logged Home Page"""

    def wait_until_loaded(self):
        """ wait until login icon is loaded """
        time.sleep(3)
        self.driver.find_element_by_xpath(add_services_button)

    @allure.step("Click on Add Service")
    def click_add_service(self):
        """ Add first Service """
        self.driver.find_element_by_xpath(add_services_button).click()
        time.sleep(3)
        add_service_page = DNVAddServicesPage(self.driver)
        add_service_page.wait_until_loaded()
        return add_service_page

    @allure.step("Remove Service")
    def remove_service(self):
        """ Remove previous selected service """
        self.driver.find_element_by_xpath(customization_button).click()
        ''' TODO: Need to be changed by other type of wait'''
        time.sleep(3)
        self.driver.find_element_by_xpath(remove_button).click()
        ''' TODO: Need to be changed by other type of wait'''
        time.sleep(3)
        self.driver.find_element_by_xpath(finalization_button).click()

    @allure.step("Check if services pages doesn't contains any service")
    def is_void_service_image_appears(self):
        return self.driver.find_element_by_xpath(service_image).is_displayed()
