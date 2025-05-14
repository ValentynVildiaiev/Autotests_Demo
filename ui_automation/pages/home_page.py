from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,browser):
        self.browser = browser

    def find_element(self,args):
        return self.browser.find_element(*args)

    def open_page_simple_button(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Simple button']").click()

    def open_page_text_input(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Text input']").click()

    def open_page_single_check_box(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Single checkbox']").click()

    def open_page_text_area(self):
        self.browser.find_element(By.XPATH, "//a[@href='/elements/textarea/single']").click()

    def open_page_select_input(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Select input']").click()









