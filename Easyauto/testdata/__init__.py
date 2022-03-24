try:
    from faker import Faker
except ModuleNotFoundError:
    raise ModuleNotFoundError('Please install the library. https://faker.readthedocs.io/en/master/index.html')
# from Easyauto.running.config import FakerConfig

fake = Faker('zh_CN')



def first_name_female(number=None):
    '''
        返回一个女性的firstname
    '''
    if not number or number == 1:
        return fake.first_name_female()
    else:
        if not isinstance(number, int):
            return fake.first_name_female()
    return (fake.first_name_female() for _ in range(number))


def first_name_male(number=None):
    '''
        返回一个男性的firstname
    '''
    if not number or number == 1:
        return fake.first_name_male()
    else:
        if not isinstance(number, int):
            return fake.first_name_male()
    return (fake.first_name_male() for _ in range(number))


def last_name_female(number=None):
    '''
        返回一个女性的lastname
    '''
    if not number or number == 1:
        return fake.last_name_female()
    else:
        if not isinstance(number, int):
            return fake.last_name_female()
    return (fake.last_name_female() for _ in range(number))


def last_name_male(number=None):
    '''
        返回一个男性的lastname
    '''
    if not number or number == 1:
        return fake.last_name_male()
    else:
        if not isinstance(number, int):
            return fake.last_name_male()
    return (fake.last_name_male() for _ in range(number))


def username(number=None):
    '''
        返回一个普通的名字
    '''
    if not number or number == 1:
        return fake.name()
    else:
        if not isinstance(number, int):
            return fake.name()
    return (fake.name() for _ in range(number))


def address(number=None):
    '''
        返回一个地址: 
        ex:澳门特别行政区台北市平山陈街G座 418897
    '''
    if not number or number == 1:
        return fake.address()
    else:
        if not isinstance(number, int):
            return fake.address()
    return (fake.address() for _ in range(number))


def city(number=None):
    '''
        返回一个城市名字
    '''
    if not number or number == 1:
        return fake.city()
    else:
        if not isinstance(number, int):
            return fake.city()
    return (fake.city() for _ in range(number))


def country(number=None):
    '''
        返回一个国家名字
    '''
    if not number or number == 1:
        return fake.country()
    else:
        if not isinstance(number, int):
            return fake.country()
    return (fake.country() for _ in range(number))


def street_address(number=None):
    '''
        返回一个街道地址
    '''
    if not number or number == 1:
        return fake.street_address()
    else:
        if not isinstance(number, int):
            return fake.street_address()
    return (fake.street_address() for _ in range(number))


def company_name(number=None):
    '''
        返回一个公司名字
    '''
    if not number or number == 1:
        return fake.company()
    else:
        if not isinstance(number, int):
            return fake.company()
    return (fake.company() for _ in range(number))


def date_time(number=None, **kwargs):
    '''
        返回一个格式化日期
        date_time(pattern: str = '%Y-%m-%d', 
        end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = None
        ) → str 
    '''
    if not number or number == 1:
        return fake.date(**kwargs)
    else:
        if not isinstance(number, int):
            return fake.date(**kwargs)
    return (fake.date(**kwargs) for _ in range(number))


def date_of_birth(number=None, **kwargs):
    '''
        返回一个生日日期
        date_of_birth(tzinfo: Optional[datetime.tzinfo] = None,
        minimum_age: int = 0, maximum_age: int = 115
        ) → datetime.date
    '''
    if not number or number == 1:
        return fake.date_of_birth(**kwargs)
    else:
        if not isinstance(number, int):
            return fake.date_of_birth(**kwargs)
    return (fake.dadate_of_birthte(**kwargs) for _ in range(number))


def future_datetime(number=None, **kwargs):
    '''
        返回一个未来的时间
        future_datetime(end_date: Union[datetime.date, 
        datetime.datetime, datetime.timedelta, str, int] = '+30d', tzinfo: Optional[datetime.tzinfo] = None
        ) → datetime.datetime

    '''
    if not number or number == 1:
        return fake.future_datetime(**kwargs)
    else:
        if not isinstance(number, int):
            return fake.future_datetime(**kwargs)
    return (fake.future_datetime(**kwargs) for _ in range(number))


def past_datetime(number=None, **kwargs):
    '''
        返回一个过去的时间
        past_datetime(start_date: Union[datetime.date,
        datetime.datetime, datetime.timedelta, str, int] = '-30d', tzinfo: Optional[datetime.tzinfo] = None
        ) → datetime.datetime

    '''
    if not number or number == 1:
        return fake.past_datetime(**kwargs)
    else:
        if not isinstance(number, int):
            return fake.past_datetime(**kwargs)
    return (fake.past_datetime(**kwargs) for _ in range(number))


def file_extension(number=None, **kwargs):
    '''
        返回一个随机的文件后缀
        If category is None, a random category will be used. 
        The list of valid categories include: 'audio', 'image', 'office', 'text', and 'video'
        file_extension(category: Optional[str] = None) → str
    '''
    if not number or number == 1:
        return fake.file_extension(**kwargs)
    else:
        if not isinstance(number, int):
            return fake.file_extension(**kwargs)
    return (fake.file_extension(**kwargs) for _ in range(number))


def email(number=None):
    '''
        返回一个随机的email
    '''

    if not number or number == 1:
        return fake.free_email()
    else:
        if not isinstance(number, int):
            return fake.free_email()
    return (fake.free_email() for _ in range(number))

def http_method(number=None):
    '''
        返回一个http请求方式
    '''
    if not number or number == 1:
        return fake.http_method()
    else:
        if not isinstance(number, int):
            return fake.http_method()
    return (fake.http_method() for _ in range(number))


def ipv4(number=None):
    '''
        返回一个ipv4
        ipv4(network: bool = False, address_class: Optional[str] = None,
        private: Optional[str] = None) → str
    '''
    if not number or number == 1:
        return fake.ipv4()
    else:
        if not isinstance(number, int):
            return fake.ipv4()
    return (fake.ipv4() for _ in range(number))

def ipv6(number=None):
    '''
        返回一个ipv6
        ipv6(network: bool = False) → str
    '''
    if not number or number == 1:
        return fake.ipv6()
    else:
        if not isinstance(number, int):
            return fake.ipv6()
    return (fake.ipv6() for _ in range(number))

    
print(fake.file_path(depth=4))


