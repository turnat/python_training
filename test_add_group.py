# -*- coding: utf-8 -*-
import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import geckodriver_autoinstaller
driver = webdriver.Chrome()
import unittest, time, re
from group import Group

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#driver.get("http://localhost/addressbook/")
#time.sleep(5)
class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        #self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
       
       


    def logaut(self):
        wd = self.wd
        wd.find_element_by_link_text("Выйти").click()
        time.sleep(5)

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        time.sleep(5)
        # развернуть браузер на весь экран
        wd.maximize_window()
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="NameG", header="header", footer="bla bla bla"))
        self.logaut()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logaut()


    def tearDown(self):
        self.wd.quit()
        driver.quit()


if __name__ == "__main__":
    unittest.main()






















































# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
