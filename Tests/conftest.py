import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Pages.TestData import Data
@pytest.fixture()
def setup(browser):
    if browser=="chrome":

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get(Data.BASE_URL)
        return driver
    elif browser == "firefox":
        driver= webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(Data.BASE_URL)
        return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

