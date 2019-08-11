from page_objects import PageObject
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage(PageObject):
    def get_element(self, identifier, css=None):
        """
        Automatically wait until element exists and get web element based on the given identifier or css
        :param identifier:
        :param css:
        :return:
        """
        css_selector = self._get_css_selector(identifier, css)
        try:
            self.w.wait_until_visible(By.CSS_SELECTOR, css_selector)
        except:  # pylint: disable=bare-except
            pass
        return self.w.find_element_by_css_selector(css_selector)

    def get_elements(self, identifier, css=None):
        """
        Automatically wait until element exists and get web elements based on the given identifier or css
        :param identifier:
        :param css:
        :return:
        """
        css_selector = self._get_css_selector(identifier, css)
        try:
            self.w.wait_until_visible(By.CSS_SELECTOR, css_selector)
        except:  # pylint: disable=bare-except
            pass
        return self.w.find_elements_by_css_selector(css_selector)

    def _get_css_selector(self, identifier, css):
        css_selector = getattr(self, identifier, css)
        if css_selector is None:
            id_or_css = css if css else identifier
            raise NoSuchElementException(id_or_css + ' cannot be found in this page')
        return css_selector

    def send_keys_to_element(self, text, identifier, css=None):
        """send keys to input and auto wait """
        css_selector = self._get_css_selector(identifier, css)
        self.w.wait_until_visible(By.CSS_SELECTOR, css_selector)
        self.w.find_element_by_css_selector(css_selector).send_keys(text)
        self.w.wait_for_condition(
            lambda _: self.w.find_element_by_css_selector(css_selector).get_attribute('value') == text)

    @staticmethod
    def get_text(element):
        """
        Returns element text value.
        el.text doesn't work in Chrome, but works in IE and el.get_attribute works in all browser but behavior in
        Chrome differs from that of IE (where text not displayed on page is returned).
        """

        return element.text if element.text else element.get_attribute('innerText')

    def click_element(self, identifier, css=None):
        """Auto wait before click the element"""
        css_selector = self._get_css_selector(identifier, css)
        self.w.wait_until_clickable(By.CSS_SELECTOR, css_selector)
        self.w.find_element_by_css_selector(css_selector).click()
