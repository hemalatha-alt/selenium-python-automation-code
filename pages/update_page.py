import time
from selenium.webdriver.common.by import By
from base.page_scroll import BaseDriver


class Mile_update(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # locator
    def locator_mile(self):
        return self.wait_element_to_be_clickable(By.CSS_SELECTOR, "#radiofield-item-id-milesOrMoney-1")
    def locator_update(self):
        return self.wait_element_to_be_clickable(By.XPATH, "//button[@class='atm-c-btn atm-c-btn--secondary']//span[1]")
    def Enter_mile(self):
        self.locator_mile().click()
    def Enter_update(self):
        self.locator_update().click()

    # def miles(self):
    #     mile=self.wait_element_to_be_clickable(By.CSS_SELECTOR, "#radiofield-item-id-milesOrMoney-1")
    #     mile.click()

    # def updates(self):
    #     update = self.wait_element_to_be_clickable(By.XPATH, "//button[@class='atm-c-btn atm-c-btn--secondary']//span[1]")
    #     update.click()
        time.sleep(3)


