from selenium.webdriver.common.by import By
from base.page_scroll import BaseDriver
class signin(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def closesign(self):
        closesign1=self.wait_element_to_be_clickable(By.XPATH, "//button[@class='modalCloseImg simplemodal-close']")
        closesign1.click()