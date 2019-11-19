import requests
from selenium import webdriver
import functools
import lxml.etree as le
import time

def mkLogger(item):
    def logger(func, item = item):
        @functools.wraps(logger)
        def wrapper(*args, **kwargs):
            print(f'Getting {item}...')
            func(*args, **kwargs)
        return wrapper
    return logger

htmlLogger = mkLogger('HTML')
titleLogger = mkLogger('title')
abstractLogger = mkLogger('abstract')
textLogger = mkLogger('text')
videoLogger = mkLogger('video')

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

class News(object):

    def __init__(self, url):
        self.url = url
        self.get_html()
        self.get_title()
        self.get_abstract()
        self.get_text()
    
    @htmlLogger
    def get_html(self):
        self.html = le.HTML(requests.get(self.url, headers=headers).text)
    
    @titleLogger
    def get_title(self):
        pass

    @abstractLogger
    def get_abstract(self):
        pass

    @textLogger
    def get_text(self):
        pass