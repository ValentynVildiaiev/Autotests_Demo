from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Autotests_Demo.ui_automation.pages.home_page import HomePage


class TextInputPage(HomePage):
    def __init__(self,browser):
        super().__init__(browser)



    def email_field_tab(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Text input']").click()

    def simple_button_tab(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Email field']").click()

    def password_field_tab(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Email field']").click()

    def text_field_input(self):
        input_field = self.browser.find_element(By.ID, "id_text_string")
        input_field.click()

    def send_enter_key(self):
        input_field = self.browser.find_element(By.ID, "id_text_string")
        input_field.send_keys(Keys.ENTER)





