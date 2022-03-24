class Easyauto:
    """
    Easyauto browser driver
    """
    driver = None
    timeout = 10
    debug = False
    base_url = None


class BrowserConfig:
    """
    Define run browser config
    """
    NAME = None
    REPORT_PATH = None
    REPORT_TITLE = "Easyauto Test Report"
    LOG_PATH = None

class FakerConfig:
    '''
       Define Faker language
    '''
    LANGUAGE = 'zh_CN'
