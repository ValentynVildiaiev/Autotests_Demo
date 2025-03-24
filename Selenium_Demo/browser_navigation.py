from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://www.google.com/"
URL2 = "https://www.wikipedia.org/"



class TestBrowserNavigation:

    def setup_method(self, method):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver: RemoteWebDriver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_back_button(self):
        self.driver.get(URL)
        self.driver.get(URL2)
        self.driver.back()
        title = self.driver.title
        assert title == "Google"

    def test_forward_button(self):
        self.driver.get(URL)
        self.driver.get(URL2)
        self.driver.back()
        self.driver.forward()
        title = self.driver.title
        assert title == "Wikipedia"





