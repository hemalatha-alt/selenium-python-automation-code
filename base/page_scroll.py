import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class BaseDriver():
    def __init__(self,driver):
        self.driver=driver
    def page_scroll(self):
        pageLength = self.driver.execute_script(
           "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
            time.sleep(4)
    def wait_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        list_of_element= wait.until(EC.presence_of_element_located((locator_type,locator)))
        return list_of_element
    def wait_elements_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return elements
