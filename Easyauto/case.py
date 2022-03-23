import unittest

from Easyauto.webdriver import WebDriver

from Easyauto.running.config import Easyauto





class TestCase(unittest.TestCase, WebDriver):

    def start_class(self):
        """
        Hook method for setting up class fixture before running tests in the class.
        """
        pass

    def end_class(self):
        """
        Hook method for deconstructing the class fixture after running all tests in the class.
        """
        pass

    @classmethod
    def setUpClass(cls):
        cls().start_class()

    @classmethod
    def tearDownClass(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        pass

    def end(self):
        """
        Hook method for deconstructing the test fixture after testing it.
        """
        pass

    def setUp(self):
        self.images = []
        self.start()

    def tearDown(self):
        self.end()

    @property
    def driver(self):
        """
        return browser driver
        """
        return Easyauto.driver
