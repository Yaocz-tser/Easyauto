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

    def __find_element(self, elem: tuple):
        """
        Find if the element exists.
        """
        for _ in range(Easyauto.timeout):
            elems = Easyauto.driver.find_elements(by=elem[0], value=elem[1])
            if len(elems) >= 1:
                self.find_elem_info = "Find {number} element: {by}={value} ".format(
                    number=str(len(elems)), by=elem[0], value=elem[1])
                break
            else:
                time.sleep(1)
        else:
            self.find_elem_warn = "❌ Find 0 element through: {by}={value}".format(
                by=elem[0], value=elem[1])

    def get_elements(self, index: int = None):
        """
        Judge element positioning way, and returns the element.
        """

        if self.by == "id_":
            self.__find_element((By.ID, self.value))
            elem = Easyauto.driver.find_elements(By.ID, self.value)
        elif self.by == "name":
            self.__find_element((By.NAME, self.value))
            elem = Easyauto.driver.find_elements(By.NAME, self.value)
        elif self.by == "class_name":
            self.__find_element((By.CLASS_NAME, self.value))
            elem = Easyauto.driver.find_elements(By.CLASS_NAME, self.value)
        elif self.by == "tag":
            self.__find_element((By.TAG_NAME, self.value))
            elem = Easyauto.driver.find_elements(By.TAG_NAME, self.value)
        elif self.by == "link_text":
            self.__find_element((By.LINK_TEXT, self.value))
            elem = Easyauto.driver.find_elements(By.LINK_TEXT, self.value)
        elif self.by == "partial_link_text":
            self.__find_element((By.PARTIAL_LINK_TEXT, self.value))
            elem = Easyauto.driver.find_elements(By.PARTIAL_LINK_TEXT, self.value)
        elif self.by == "xpath":
            self.__find_element((By.XPATH, self.value))
            elem = Easyauto.driver.find_elements(By.XPATH, self.value)
        elif self.by == "css":
            self.__find_element((By.CSS_SELECTOR, self.value))
            elem = Easyauto.driver.find_elements(By.CSS_SELECTOR, self.value)
           
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id_/name/class_name/tag/link_text/xpath/css'.")
        if index is None:
            return elem
        elif len(elem) == 0:
            raise NotFindElementError(self.find_elem_warn)
        else:
            return elem[index]
   

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

    @staticmethod
    def get_elements(**kwargs):
        """
        Get a set of elements

        Usage:
        ret = self.get_elements(css="#el")
        print(len(ret))
        """
        web_elem = WebElement(**kwargs)
        elems = web_elem.get_elements()
        if len(elems) == 0:
            # log.warn("{}.".format(web_elem.warn))
            pass
        else:
            # log.info("✅ {}.".format(web_elem.info))
            pass
        return elems

    @staticmethod
    def get_element(index: int = 0, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
    
        return elem