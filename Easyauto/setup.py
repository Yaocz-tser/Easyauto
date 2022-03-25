# coding=utf-8
import re
import ast
from setuptools import setup, find_packages
from os.path import dirname, join, abspath

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('Easyauto/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='Easyauto',
    version=version,
    url='https://github.com/Yaocz-tser/Easyauto_1/',
    license='BSD',
    author='itser',
    author_email='Yaocz-tser@163.com',
    description='WebUI/HTTP automation testing framework based on unittest.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'selenium>=4.0.0',
        'XTestRunner>=1.3.1',
        'parameterized==0.8.1',
        'loguru>=0.4.1',
        'openpyxl>=3.0.3',
        'pyyaml>=5.1',
        'requests>=2.22.0',
        'jsonschema>=3.2.0',
        'jmespath>=0.10.0',
        'webdriver-manager>=3.5.0',
        'pymysql>=1.0.0',
        'Faker==13.3.3'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        Easyauto=Easyauto.cli:main
    '''
)