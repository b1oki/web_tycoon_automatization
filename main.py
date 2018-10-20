# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

GAME_LOGIN = ''
GAME_PASSWORD = ''


class Browser(object):
    browser = None
    visible = None
    implicitly_wait = 10

    def create_browser(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        if not self.visible:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(self.implicitly_wait)

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


class GamePage(object):
    GAME_DOMAIN = 'game.web-tycoon.com'
    __browser = None

    @property
    def browser(self):
        """ :rtype: webdriver.Chrome"""
        if not self.__browser:
            self.__browser = Browser(visible=True)
        return self.__browser.browser

    def game_login(self, login, password):
        self.browser.get('https://{}'.format(self.GAME_DOMAIN))
        self.browser.find_element_by_link_text('Войти в аккаунт').click()
        input_login = self.browser.find_element_by_id('userEmail')
        input_password = self.browser.find_element_by_id('userPassword')
        input_login.clear()
        input_login.send_keys(login)
        input_password.clear()
        input_password.send_keys(password)
        self.browser.find_element_by_class_name('enterButton').click()


def main():
    page = GamePage()
    page.game_login(GAME_LOGIN, GAME_PASSWORD)
    """ TODO:
    пройти по сотрудникам
        занятость
        энергия
        профиль (максимальный скилл)
    пройти по сайтам
        дизайн, верстка, программирование, контент
            прогресс выполнения
            назначенный сотрудник
            если есть свободный профильный сотрудник, то назначить
        выпустить версию
        опубликовать контент
    если долго простаивает сотрудник, то назначаем на подходящую работу
    """


main()
