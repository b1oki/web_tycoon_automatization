# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

GAME_LOGIN = ''
GAME_PASSWORD = ''


class Browser(object):
    browser = None
    visible = None

    def create_browser(self):
        chrome_options = Options()
        if not self.visible:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def __init__(self, visible=False):
        self.visible = bool(visible)
        self.create_browser()

    def close_browser(self):
        if self.browser:
            self.browser.close()
            self.browser = None

    def cleanup(self):
        self.close_browser()

    def close(self):
        self.cleanup()

    def __del__(self):
        self.cleanup()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()
