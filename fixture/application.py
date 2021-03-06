# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        # развернуть браузер на весь экран
        wd.maximize_window()
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
        driver.quit()


