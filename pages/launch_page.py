
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from base.page_scroll import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    #     locator
    oneway_Field='//*[@id="bookFlightForm"]/div[1]/fieldset/div/label[2]/span[2]'
    orgin_Field="bookFlightOriginInput"
    departure_Field="bookFlightDestinationInput"
    dates_Field="DepartDate"
    select_date_Field="//td[@aria-label='Thursday, April 7, 2022']"
    search_flight_Field="//button[@aria-label='Find flights']"

    def locator_oneway_Field(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.oneway_Field)
    def locator_orgin_Field(self):
        return self.wait_element_to_be_clickable(By.ID,self.orgin_Field)
    def locator_deparature_Field(self):
        return self.wait_element_to_be_clickable(By.ID,self.departure_Field)
    def locator_dates_Field(self):
        return self.wait_element_to_be_clickable(By.ID, self.dates_Field)
    def locator_select_date_Field(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.select_date_Field)
    def locator_flight_Field(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.search_flight_Field)

    def enteronewayfield(self):
        self.locator_oneway_Field().click()

    def enterorginfield(self,orginlocation):
        self.locator_orgin_Field().clear()
        self.locator_orgin_Field().send_keys(orginlocation)

    def enterdeparturefield(self,departurelocation):
        self.locator_deparature_Field().click()
        self.locator_deparature_Field().clear()
        self.locator_deparature_Field().send_keys(departurelocation)


    def enterdateField(self):
        self.locator_dates_Field().click()
        self.locator_select_date_Field().click()


    def entersearchflightField(self):
        self.locator_flight_Field().click()
    time.sleep(3)
    def test_search_flight(self,orginlocation,departurelocation):
        self.enteronewayfield()
        self.enterorginfield(orginlocation)
        self.enterdeparturefield(departurelocation)
        self.enterdateField()
        self.entersearchflightField()

