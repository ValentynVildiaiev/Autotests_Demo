from selenium.webdriver.common.by import By

from Autotests_Demo.ui_automation.pages.home_page import HomePage


button_selector = (By.ID, "submit-id-submit")

class SimpleCheckPage(HomePage):
    def __init__(self,browser):
        super().__init__(browser)

    def button(self):
        return self.find(button_selector)