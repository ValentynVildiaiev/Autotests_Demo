from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Autotests_Demo.Selenium_Demo.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.lambdatest.com/selenium-playground/"



class TestTheInternetWebSite:

    def setup_method(self, method):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver: RemoteWebDriver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_check_url(self):
        self.driver.get(URL)
        assert self.driver.current_url == "https://www.lambdatest.com/selenium-playground/"

    def test_open_url(self):
        self.driver.get(URL)
        assert self.driver.title == 'Selenium Grid Online | Run Selenium Test On Cloud'

    def test_one_checkbox(self):
        self.driver.get(URL)
        page = MainPage(self.driver)
        page.click_checkbox_demo()
        self.driver.find_element(By.XPATH,"//input[@id='isAgeSelected']").click()
        checked = self.driver.find_element(By.XPATH,"//div[@id='txtAge']").text
        assert checked == "Checked"
        self.driver.find_element(By.XPATH, "//input[@id='isAgeSelected']").click()

    def test_check_all_checkboxes(self):
        self.driver.get(URL)
        page = MainPage(self.driver)
        page.click_checkbox_demo()
        self.driver.find_element(By.XPATH,"//input[@id='box']").click()
        uncheck_all_button = self.driver.find_element(By.XPATH,"//input[@value='Uncheck All']").get_attribute("value")
        assert uncheck_all_button == "Uncheck All"

    def test_auto_healing(self):
        self.driver.get(URL)
        page = MainPage(self.driver)
        page.click_auto_healing()
        page_title = self.driver.find_element(By.XPATH,"//h1[normalize-space()='Auto Healing']")
        assert page_title.text == "Auto Healing"



    def test_auto_heal_filling_form_login(self):
        self.driver.get(URL)
        page = MainPage(self.driver)
        page.click_auto_healing()
        user_name_field = self.driver.find_element(By.XPATH, '//input[@id="username"]')
        user_name_field.click()
        user_name_field.send_keys("abc")

    def test_auto_heal_filling_pass(self):
        self.driver.get(URL)
        page = MainPage(self.driver)
        page.click_auto_healing()
        user_name_field = self.driver.find_element(By.XPATH, '//input[@id="username"]')
        user_name_field.click()
        user_name_field.send_keys("abc")
        user_name_field = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        user_name_field.click()
        user_name_field.send_keys("cba")
        user_name_field.send_keys(Keys.ENTER)
        success_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Login Successful']"))
        )
        assert success_element.text == "Login Successful"








