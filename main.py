import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login = "https://ch.acconversion.cibc.com/cholder/welcome.action?request_locale=en"
username = ""
pwd = ""
vbv_pwd = ""


class Main:
    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': os.getcwd()}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)

    def login(self):
        self.driver.get(login)

        fill_user = self.driver.find_element_by_id("userId")
        fill_user.clear()
        fill_user.send_keys(username)

        fill_pwd = self.driver.find_element_by_id("userPassword")
        fill_pwd.clear()
        fill_pwd.send_keys(pwd)

        fill_pwd.send_keys(Keys.RETURN)

    def load(self):
        load_link = self.driver.find_element_by_link_text("Load Funds")
        load_link.click()

        time.sleep(3)

        amount = self.driver.find_element_by_class_name("input-right")
        amount.clear()
        amount.send_keys("100.00")

        cad = self.driver.find_element_by_class_name("chosen-single")
        cad.click()

        search = self.driver.find_element_by_id("chosensearchfieldfromAccount")
        search.send_keys("CAD")
        search.send_keys(Keys.RETURN)

        self.driver.find_element_by_id("calculateButton").click()

        time.sleep(1)

        self.driver.find_element_by_id("addToCartButton").click()

        time.sleep(1)

        self.driver.find_element_by_class_name("iCheck-helper").click()
        self.driver.find_element_by_id("next").click()
        time.sleep(3)

    def pay(self):
        self.driver.find_element_by_class_name("iCheck-helper").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="payment-form"]/div/div[7]/div/input').click()

    def rbc_vbv(self):
        time.sleep(5)
        p = self.driver.find_element_by_id("Password")
        p.send_keys(vbv_pwd)
        p.send_keys(Keys.RETURN)

    def full_run(self):
        self.login()
        self.load()
        self.pay()
        # self.rbc_vbv()


Main().full_run()
