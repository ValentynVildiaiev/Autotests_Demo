from selenium.webdriver.common.by import By


class MainPage:
    check_box_demo = (By.XPATH,"//a[normalize-space()='Checkbox Demo']")
    auto_healing = (By.XPATH, "//a[normalize-space()='Auto Healing']")
    geo_location = (By.XPATH, "//a[normalize-space()='Auto Healing']")

    def __init__(self, driver):
        self.driver = driver

    def click_checkbox_demo(self):
        self.driver.find_element(*self.check_box_demo).click()

    def click_auto_healing(self):
        self.driver.find_element(*self.auto_healing).click()

