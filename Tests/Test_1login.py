import openpyxl
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Tests import read
from utilities.looger import LogGen

from Pages.Login import Login
from Pages.TestData import Data
class TestLogin:
    path = "C:\\Users\\LORD TRADE\\PycharmProjects\\pythonProject3\\Tests\\admin.xlsx"




    def test_login(self,setup):


        self.driver=setup
        self.log = Login(self.driver)
        self.rows = read.getRowCount(self.path, 'Sheet1')
        for r in range(2, self.rows + 1):
            self.email = read.readData(self.path, 'Sheet1', r, 1)
            self.password = read.readData(self.path, 'Sheet1', r, 2)


            self.log.enterinfo(self.email,self.password)


        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")


        self.driver.close()