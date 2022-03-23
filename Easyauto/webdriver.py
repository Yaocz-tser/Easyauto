# coding=utf-8
import os
import time
import platform
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from Easyauto.running.config import Easyauto
from Easyauto.logging.exceptions import NotFindElementError
from Easyauto.utils.webdriver_manager_extend import ChromeDriverManager

__all__ = ["WebDriver"]


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


class WebElement(object):

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        self.by, self.value = next(iter(kwargs.items()))
        try:
            LOCATOR_LIST[self.by]
        except KeyError:
            raise ValueError(
                "Element positioning of type '{}' is not supported. ".format(self.by))
        self.find_elem_info = None
        self.find_elem_warn = None

   

class WebDriver(object):
    """
        Easyauto framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """

   

    def __init__(self, index: int = 0, **kwargs):
        self.web_elem = WebElement(**kwargs)
        self.elem = self.web_elem.get_elements(index)
        self.web_elem.show_element(self.elem)

   
    @staticmethod
    def visit(url: str):
        """
        visit url.

        Usage:
            self.visit("https://www.baidu.com")
        """
        if isinstance(Easyauto.driver, SeleniumWebDriver) is False:
            Easyauto.driver = Chrome(
                executable_path=ChromeDriverManager().install())
        Easyauto.driver.get(url)

    def open(self, url: str):
        """
        open url.

        Usage:
            self.open("https://www.baidu.com")
        """
        self.visit(url)

   