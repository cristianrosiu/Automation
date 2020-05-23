from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()


class CsBot(object):
    def __init__(self):
        self.url = 'https://www.csgoroll.com/en/roll'
        self.steam_url = 'https://api.csgoroll.com/auth/steam?redirectUri=/en/roll'
        pass

    def site_login(self, username, password):
        driver.get(self.url)
        driver.get(self.steam_url)
        driver.find_element_by_id("steamAccountName").send_keys(username)
        driver.find_element_by_id("steamPassword").send_keys(password)
        driver.find_element_by_id("imageLogin").click()


bot = CsBot()

bot.site_login('loolz3r', 'Banimurdari1.')
