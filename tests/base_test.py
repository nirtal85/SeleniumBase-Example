from seleniumbase import BaseCase
from utils.config_parser import ConfigParserIni
import allure


class BaseTestCase(BaseCase):
    @allure.description("Open browser and navigate to base url")
    def setUp(self):
        super().setUp()
        config = ConfigParserIni("props.ini")
        base_url = config.config_section_dict("Base Url")["base_url"]
        self.maximize_window()
        self.open(base_url)

    @allure.description("Terminate test and close browser")
    def tearDown(self):
        self.save_teardown_screenshot()
        if self.has_exception():
            print("Test Failed!")
        else:
            print("Test Passed!")
        super().tearDown()
