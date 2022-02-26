
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

from pages.launch_page import LaunchPage
from pages.update_page import Mile_update
from pages.sign_in_page import signin
from pages.select_stop_page import SelectStop
from utilities.utilitie import utlit
import softest






@pytest.mark.usefixtures("setup")
class Test_searching(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp=LaunchPage(self.driver)
        self.mi=Mile_update(self.driver)
        self.cs=signin(self.driver)
        self.ss=SelectStop(self.driver)
        self.ut=utlit()
    def test_demo_search(self):
        self.lp.test_search_flight("ORD","DEL")
        self.mi.Enter_mile()
        self.mi.Enter_update()
        self.cs.closesign()
        self.ss.stopup()
        searchstop=self.lp.wait_elements_to_be_clickable(By.XPATH, "//ul[@id='flight-result-list-revised']/li")
        self.ss.page_scroll()
        self.ut.assertlistitems(searchstop,"stops")
        print("test completed successfully")

