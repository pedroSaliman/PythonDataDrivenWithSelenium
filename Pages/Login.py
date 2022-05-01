from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.base import Base
class Login(Base):

    def __init__(self, driver):
        super().__init__(driver)
    Email_id = (By.ID,"Email")
    Password_id = (By.ID,"Password")
    btnlogin = (By.XPATH,"//button[text()='Log in']")
    btnlogout=(By.XPATH,"//a[text()='Logout']")




    def enterinfo(self,email,password):

        self.clear(self.Email_id)
        self.type(self.Email_id,email)
        self.clear(self.Password_id)
        self.type(self.Password_id,password)
        self.click(self.btnlogin)
        self.click(self.btnlogout)





