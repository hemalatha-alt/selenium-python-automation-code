from selenium.webdriver.common.by import By
from base.page_scroll import BaseDriver


class SelectStop(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def stopup(self):
        stopselect=self.wait_element_to_be_clickable(By.XPATH, "//span[normalize-space()='Stops']")
        stopselect.click()
