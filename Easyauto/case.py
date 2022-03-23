import unittest
from Easyauto.webdriver import WebDriver
from Easyauto.running.config import Easyauto
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase, WebDriver):

    def start_class(self):
        '''
        Hook method for setting up class fixture before running tests in the class.
        '''
        pass

    def end_class(self):
        '''
        Hook method for deconstructing the class fixture after running all tests in the class.
        '''
        pass

    @classmethod
    def setUpClass(cls):
        cls().start_class()

    @classmethod
    def tearDownClass(cls):
        cls().end_class()

    def start(self):
        '''
        Hook method for setting up the test fixture before exercising it.
        '''
        pass

    def end(self):
        '''
        Hook method for deconstructing the test fixture after testing it.
        '''
        pass

    def setUp(self):
        self.images = []
        self.start()

    def tearDown(self):
        self.end()

    @property
    def driver(self):
        '''
        return browser driver
        '''
        return Easyauto.driver


    def assertTitle(self,title=None,msg=None):
        '''
           通过网页当前title来断言
           使用方式:
                self.assertTitle('title')
        '''
        if title is None:
            raise AssertionError('The assertion title cannot be empty.')
        
        try:
            flag = wait(Easyauto.driver,timeout=Easyauto.timeout).until(EC.title_is(title))
        except TimeoutException:
            flag = False
        self.assertTrue(flag,msg=msg)


    def assertInTitle(self,title=None,msg=None):
        '''
           通过网页当前title部分来断言
           使用方式:
                self.assertInTitle('title')
        '''
        if title is None:
            raise AssertionError('The assertion title cannot be empty.')
        
        try:
            flag = wait(Easyauto.driver,timeout=Easyauto.timeout).until(EC.title_contains(title))
        except TimeoutException:
            flag = False
        self.assertTrue(flag,msg=msg)

    

    def assertUrl(self,url=None,msg=None):
        '''
           通过网页当前url来断言
           使用方式:
                self.assertUrl('url')
        '''

        if url is None:
            raise AssertionError('The assertion url cannot be empty.')
        
        try:
            flag = wait(Easyauto.driver,timeout=Easyauto.timeout).until(EC.url_matches(url))
        except TimeoutException:
            flag = False
        self.assertTrue(flag,msg=msg)

    

    def assertInUrl(self,url=None,msg=None):
        '''
           通过网页当前url部分来断言
           使用方式:
                self.assertInUrl('url')
        '''

        if url is None:
            raise AssertionError('The assertion url cannot be empty.')
        
        try:
            flag = wait(Easyauto.driver,timeout=Easyauto.timeout).until(EC.url_contains(url))
        except TimeoutException:
            flag = False
        self.assertTrue(flag,msg=msg)

    
    def assertText(self, text=None, msg=None):
        '''
            通过html中的text来断言
            使用方式:
                self.assertText('text')
        '''
        if text is None:
            raise AssertionError('The assertion text cannot be empty.')

        try:
            flag = wait(Easyauto.driver,timeout=Easyauto.timeout).until(EC.text_to_be_present_in_element((
                By.TAG_NAME,'html'
            ), text))
        except TimeoutException:
            flag = False
        self.assertTrue(flag,msg=msg)
    

    

    def assertAlertText(self, text=None, msg=None):
        '''
            通过Alert中的text来断言
            使用方式:
                self.assertAlertText('text')
        '''
        if text is None:
            raise AssertionError('The assertion text cannot be empty.')

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        self.assertEqual(alert_text, text, msg=msg)

    

    def assertConfirmText(self, text=None, msg=None):
        '''
            通过Confirm中的text来断言
            使用方式:
                self.assertConfirmText('text')
        '''
        if text is None:
            raise AssertionError('The assertion text cannot be empty.')

        alert_text = Easyauto.driver.switch_to.alert.text
        self.assertEqual(alert_text, text, msg=msg)

    def assertElement(self,index=0,msg=None, **kwargs):

        '''
            通过元素是否存在来断言
            使用方式:
                self.assertElement(css="#id") 
        '''

        
        if not len(kwargs):
            raise AssertionError('The assertion kwargs cannot be empty.')   
        try:
            self.get_element(index=index, **kwargs)
            elem = True  
        except Exception:
            elem = False
    
        self.assertTrue(elem, msg=msg)