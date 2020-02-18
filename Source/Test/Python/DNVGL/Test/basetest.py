from Source.Test.Python.DNVGL.PageObjects.DNVHomePage import DNVHomePage
from Source.Framework import myconfig


def go_login_page(driver):
    """ Go to login page"""
    home_page = DNVHomePage(driver)
    home_page.initiate(myconfig.urlInicial)
    return home_page.click_login_button()


def login(driver):
    """ Go logged page  """
    login_page = go_login_page(driver)
    return login_page.login(myconfig.default_email, myconfig.default_psw)
