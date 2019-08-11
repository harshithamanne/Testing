""" Class definition of custom WebDriver for functional testing """

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class WebDriver(webdriver.Chrome):
    """
    Extend webdrivers to encapsulate helper methods

    Hierarchy:
        ChromeWebDriver
              |
          WebDriver
    """
    SLEEP_TIME = 5
    period = 0.25

    def __init__(self):
        """ Initializes the selected driver """
        webdriver.Chrome.__init__(self)

    def wait_until_clickable(self, by, value, timeout=2):
        """ Block until the element described by the CSS selector is clickable. """
        return WebDriverWait(self, timeout).until(ec.element_to_be_clickable((by, value)))

    def wait_for_condition(self, condition, sleep_time=SLEEP_TIME):
        """ Wait for condition over element. """
        return WebDriverWait(self, sleep_time * 4).until(condition)

    def wait_until_visible(self, by, value, sleep_time=SLEEP_TIME):
        """ Wait for element. """
        return WebDriverWait(self, sleep_time).until(ec.visibility_of_element_located((by, value)))

    def wait_until_invisible(self, by, value, sleep_time=SLEEP_TIME):
        """ Wait for element. """
        return WebDriverWait(self, sleep_time).until(ec.invisibility_of_element_located((by, value)))
